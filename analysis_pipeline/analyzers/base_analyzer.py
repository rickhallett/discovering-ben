#!/usr/bin/env python3
"""
Base Analyzer Class
===================

Abstract base class for all analyzers in the pipeline.
Enforces standard interface and provides common utilities.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import json
import logging


@dataclass
class AnalyzerMetadata:
    """Metadata for analyzer execution"""
    analyzer_name: str
    analyzer_type: str  # 'quantitative', 'claude_api', 'claude_cli'
    version: str
    description: str


@dataclass
class AnalysisConfig:
    """Configuration for analysis execution"""
    input_files: List[str]
    output_file: str
    parameters: Dict[str, Any]


class BaseAnalyzer(ABC):
    """
    Abstract base class for all analyzers.

    Subclasses must implement:
    - analyze() method
    - metadata property

    Provides:
    - Standard logging
    - Result formatting
    - Error handling
    - Configuration management
    """

    def __init__(self, config: AnalysisConfig):
        self.config = config
        self.logger = self._setup_logging()
        self.start_time = None
        self.end_time = None

    def _setup_logging(self) -> logging.Logger:
        """Setup analyzer-specific logging"""
        logger = logging.getLogger(self.__class__.__name__)
        logger.setLevel(logging.INFO)
        return logger

    @property
    @abstractmethod
    def metadata(self) -> AnalyzerMetadata:
        """Return analyzer metadata"""
        pass

    @abstractmethod
    def analyze(self, data: Any) -> Dict[str, Any]:
        """
        Perform the analysis.

        Args:
            data: Input data to analyze

        Returns:
            Analysis results as dictionary
        """
        pass

    def load_data(self) -> Any:
        """
        Load input data from configured files.

        Returns:
            Loaded data (format depends on analyzer)
        """
        self.logger.info(f"Loading data from {len(self.config.input_files)} file(s)")

        # Most analyzers work with conversations.json
        if len(self.config.input_files) == 1 and self.config.input_files[0].endswith('conversations.json'):
            with open(self.config.input_files[0]) as f:
                return json.load(f)

        # Custom loading logic can be overridden
        return self._load_custom_data()

    def _load_custom_data(self) -> Any:
        """Override this for custom data loading"""
        raise NotImplementedError("Custom data loading not implemented")

    def run(self) -> Dict[str, Any]:
        """
        Execute the full analysis workflow.

        Returns:
            Formatted analysis result
        """
        self.logger.info(f"Starting {self.metadata.analyzer_name}")
        self.start_time = datetime.now()

        try:
            # Load data
            data = self.load_data()

            # Run analysis
            results = self.analyze(data)

            # Format output
            output = self._format_output(results, success=True)

            # Save results
            self._save_results(output)

            self.end_time = datetime.now()
            execution_time = (self.end_time - self.start_time).total_seconds()
            self.logger.info(f"Completed in {execution_time:.2f}s")

            return output

        except Exception as e:
            self.logger.error(f"Analysis failed: {e}", exc_info=True)
            self.end_time = datetime.now()

            output = self._format_output(
                {"error": str(e)},
                success=False
            )

            self._save_results(output)
            raise

    def _format_output(self, results: Dict[str, Any], success: bool = True) -> Dict[str, Any]:
        """
        Format analysis results in standard format.

        Args:
            results: Raw analysis results
            success: Whether analysis succeeded

        Returns:
            Formatted output dictionary
        """
        execution_time = 0.0
        if self.start_time and self.end_time:
            execution_time = (self.end_time - self.start_time).total_seconds()

        return {
            "analyzer": self.metadata.analyzer_name,
            "type": self.metadata.analyzer_type,
            "version": self.metadata.version,
            "description": self.metadata.description,
            "timestamp": datetime.now().isoformat(),
            "success": success,
            "execution_time_seconds": execution_time,
            "config": {
                "input_files": self.config.input_files,
                "parameters": self.config.parameters
            },
            "results": results
        }

    def _save_results(self, output: Dict[str, Any]):
        """Save results to configured output file"""
        output_path = Path(self.config.output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w') as f:
            json.dump(output, f, indent=2)

        self.logger.info(f"Results saved to {output_path}")


class QuantitativeAnalyzer(BaseAnalyzer):
    """
    Base class for quantitative (regex/stats-based) analyzers.
    """

    @property
    def metadata(self) -> AnalyzerMetadata:
        return AnalyzerMetadata(
            analyzer_name="quantitative_base",
            analyzer_type="quantitative",
            version="1.0.0",
            description="Base class for quantitative analyzers"
        )

    def analyze(self, data: Any) -> Dict[str, Any]:
        """Override in subclass"""
        raise NotImplementedError()


class ClaudeAPIAnalyzer(BaseAnalyzer):
    """
    Base class for Claude API-based analyzers.
    """

    def __init__(self, config: AnalysisConfig, model: str = "claude-haiku-4-20250514"):
        super().__init__(config)
        self.model = model

    @property
    def metadata(self) -> AnalyzerMetadata:
        return AnalyzerMetadata(
            analyzer_name="claude_api_base",
            analyzer_type="claude_api",
            version="1.0.0",
            description="Base class for Claude API analyzers"
        )

    def analyze(self, data: Any) -> Dict[str, Any]:
        """Override in subclass"""
        raise NotImplementedError()


class SynthesisAnalyzer(BaseAnalyzer):
    """
    Base class for synthesis analyzers that combine multiple previous results.
    """

    @property
    def metadata(self) -> AnalyzerMetadata:
        return AnalyzerMetadata(
            analyzer_name="synthesis_base",
            analyzer_type="synthesis",
            version="1.0.0",
            description="Base class for synthesis analyzers"
        )

    def load_data(self) -> Dict[str, Any]:
        """Load multiple result files from previous analyses"""
        self.logger.info(f"Loading {len(self.config.input_files)} result files for synthesis")

        all_results = {}
        for filepath in self.config.input_files:
            path = Path(filepath)
            if path.exists():
                with open(path) as f:
                    result_data = json.load(f)
                    analyzer_name = result_data.get('analyzer', path.stem)
                    all_results[analyzer_name] = result_data
            else:
                self.logger.warning(f"Result file not found: {filepath}")

        return all_results

    def analyze(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Override in subclass to synthesize multiple results"""
        raise NotImplementedError()


# Example concrete implementation
class TemporalAnalyzer(QuantitativeAnalyzer):
    """
    Example: Temporal pattern analysis.
    """

    @property
    def metadata(self) -> AnalyzerMetadata:
        return AnalyzerMetadata(
            analyzer_name="temporal_analyzer",
            analyzer_type="quantitative",
            version="1.0.0",
            description="Analyzes temporal patterns in conversation data"
        )

    def analyze(self, conversations: List[Dict]) -> Dict[str, Any]:
        """Analyze temporal patterns"""
        from collections import defaultdict
        from datetime import datetime

        # Extract temporal data
        hourly_distribution = defaultdict(int)
        daily_distribution = defaultdict(int)

        for conv in conversations:
            created_at = conv.get('created_at')
            if created_at:
                dt = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
                hourly_distribution[dt.hour] += 1
                daily_distribution[dt.strftime('%A')] += 1

        return {
            "total_conversations": len(conversations),
            "hourly_distribution": dict(hourly_distribution),
            "daily_distribution": dict(daily_distribution),
            "peak_hour": max(hourly_distribution.items(), key=lambda x: x[1])[0] if hourly_distribution else None,
            "peak_day": max(daily_distribution.items(), key=lambda x: x[1])[0] if daily_distribution else None
        }


# Example usage
if __name__ == "__main__":
    # Example: Run temporal analyzer
    config = AnalysisConfig(
        input_files=["conversations.json"],
        output_file="results/temporal_analysis.json",
        parameters={}
    )

    analyzer = TemporalAnalyzer(config)
    results = analyzer.run()

    print(json.dumps(results, indent=2))
