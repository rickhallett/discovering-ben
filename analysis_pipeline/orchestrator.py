#!/usr/bin/env python3
"""
Analysis Pipeline Orchestrator
===============================

Coordinates execution of analysis waves (macro level), manages analyzer
execution (meso level), and handles Claude interactions (micro level).

Usage:
    python3 orchestrator.py --config config/pipeline_config.yaml
    python3 orchestrator.py --wave 1 --data-dir /path/to/export
    python3 orchestrator.py --dry-run
"""

import argparse
import json
import logging
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

import yaml


@dataclass
class AnalyzerConfig:
    """Configuration for a single analyzer"""
    name: str
    type: str  # 'quantitative', 'claude_api', 'claude_cli'
    script: Optional[str] = None
    model: Optional[str] = None
    prompt_template: Optional[str] = None
    params: Dict[str, Any] = None
    batch_size: int = 1


@dataclass
class WaveConfig:
    """Configuration for an analysis wave"""
    name: str
    parallel: bool
    analyzers: List[str]
    requires: List[str] = None


@dataclass
class AnalysisResult:
    """Result from a single analyzer execution"""
    analyzer: str
    wave: str
    success: bool
    result_path: Optional[str] = None
    error: Optional[str] = None
    execution_time: float = 0.0
    metadata: Dict[str, Any] = None


class PipelineOrchestrator:
    """
    Orchestrates the execution of analysis waves.

    Responsibilities:
    - Load and validate configuration
    - Execute waves in correct order (respecting dependencies)
    - Run analyzers in parallel when specified
    - Manage result caching
    - Generate execution reports
    """

    def __init__(self, config_path: str, data_dir: str, output_dir: str, use_cache: bool = True):
        self.config_path = Path(config_path)
        self.data_dir = Path(data_dir)
        self.output_dir = Path(output_dir)
        self.use_cache = use_cache

        # Setup logging
        self.setup_logging()

        # Load configuration
        self.config = self.load_config()
        self.waves = self.parse_waves()
        self.analyzers = self.parse_analyzers()

        # Create output directories
        self.output_dir.mkdir(parents=True, exist_ok=True)
        (self.output_dir / "logs").mkdir(exist_ok=True)
        (self.output_dir / "results").mkdir(exist_ok=True)
        (self.output_dir / "errors").mkdir(exist_ok=True)

        # Execution state
        self.completed_waves = set()
        self.results: List[AnalysisResult] = []

    def setup_logging(self):
        """Configure logging for pipeline execution"""
        log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        logging.basicConfig(
            level=logging.INFO,
            format=log_format,
            handlers=[
                logging.StreamHandler(sys.stdout),
                logging.FileHandler(
                    self.output_dir / "logs" / f"pipeline_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
                )
            ]
        )
        self.logger = logging.getLogger(__name__)

    def load_config(self) -> Dict:
        """Load pipeline configuration from YAML"""
        self.logger.info(f"Loading configuration from {self.config_path}")

        if not self.config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")

        with open(self.config_path) as f:
            config = yaml.safe_load(f)

        return config

    def parse_waves(self) -> List[WaveConfig]:
        """Parse wave configurations"""
        waves = []
        for wave_config in self.config.get('waves', []):
            waves.append(WaveConfig(
                name=wave_config['name'],
                parallel=wave_config.get('parallel', False),
                analyzers=wave_config['analyzers'],
                requires=wave_config.get('requires', [])
            ))
        return waves

    def parse_analyzers(self) -> Dict[str, AnalyzerConfig]:
        """Parse analyzer configurations"""
        analyzers = {}
        for name, analyzer_config in self.config.get('analyzers', {}).items():
            analyzers[name] = AnalyzerConfig(
                name=name,
                type=analyzer_config['type'],
                script=analyzer_config.get('script'),
                model=analyzer_config.get('model'),
                prompt_template=analyzer_config.get('prompt_template'),
                params=analyzer_config.get('params', {}),
                batch_size=analyzer_config.get('batch_size', 1)
            )
        return analyzers

    def check_dependencies(self, wave: WaveConfig) -> bool:
        """Check if wave dependencies are satisfied"""
        if not wave.requires:
            return True

        for required_wave in wave.requires:
            if required_wave not in self.completed_waves:
                self.logger.warning(f"Wave '{wave.name}' requires '{required_wave}' which hasn't completed")
                return False

        return True

    def run_analyzer(self, analyzer_name: str, wave_name: str) -> AnalysisResult:
        """Execute a single analyzer"""
        analyzer = self.analyzers[analyzer_name]
        self.logger.info(f"[{wave_name}] Running analyzer: {analyzer_name} (type: {analyzer.type})")

        start_time = time.time()
        result_path = self.output_dir / "results" / f"{wave_name}_{analyzer_name}.json"

        try:
            # Check cache
            if self.use_cache and result_path.exists():
                self.logger.info(f"[{wave_name}] Using cached result for {analyzer_name}")
                return AnalysisResult(
                    analyzer=analyzer_name,
                    wave=wave_name,
                    success=True,
                    result_path=str(result_path),
                    execution_time=0.0,
                    metadata={"cached": True}
                )

            # Execute based on analyzer type
            if analyzer.type == 'quantitative':
                result = self.run_quantitative_analyzer(analyzer, wave_name)
            elif analyzer.type == 'claude_api':
                result = self.run_claude_api_analyzer(analyzer, wave_name)
            elif analyzer.type == 'claude_cli':
                result = self.run_claude_cli_analyzer(analyzer, wave_name)
            else:
                raise ValueError(f"Unknown analyzer type: {analyzer.type}")

            # Save result
            with open(result_path, 'w') as f:
                json.dump(result, f, indent=2)

            execution_time = time.time() - start_time
            self.logger.info(f"[{wave_name}] Completed {analyzer_name} in {execution_time:.2f}s")

            return AnalysisResult(
                analyzer=analyzer_name,
                wave=wave_name,
                success=True,
                result_path=str(result_path),
                execution_time=execution_time,
                metadata={"cached": False}
            )

        except Exception as e:
            execution_time = time.time() - start_time
            self.logger.error(f"[{wave_name}] Failed {analyzer_name}: {str(e)}", exc_info=True)

            # Save error details
            error_path = self.output_dir / "errors" / f"{wave_name}_{analyzer_name}_error.txt"
            with open(error_path, 'w') as f:
                f.write(f"Analyzer: {analyzer_name}\n")
                f.write(f"Wave: {wave_name}\n")
                f.write(f"Error: {str(e)}\n")
                f.write(f"Execution time: {execution_time:.2f}s\n")

            return AnalysisResult(
                analyzer=analyzer_name,
                wave=wave_name,
                success=False,
                error=str(e),
                execution_time=execution_time
            )

    def run_quantitative_analyzer(self, analyzer: AnalyzerConfig, wave_name: str) -> Dict:
        """Run a quantitative (Python-based) analyzer"""
        import subprocess

        # Build command
        cmd = [
            "python3",
            analyzer.script,
            "--input", str(self.data_dir / "conversations.json"),
            "--output", str(self.output_dir / "results" / f"{wave_name}_{analyzer.name}.json")
        ]

        # Add parameters
        for key, value in analyzer.params.items():
            cmd.extend([f"--{key}", str(value)])

        # Execute
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)

        # Load and return result
        result_path = self.output_dir / "results" / f"{wave_name}_{analyzer.name}.json"
        with open(result_path) as f:
            return json.load(f)

    def run_claude_api_analyzer(self, analyzer: AnalyzerConfig, wave_name: str) -> Dict:
        """Run a Claude API-based analyzer"""
        from utils.claude_interface import ClaudeAPIInterface

        # Load prompt template
        with open(analyzer.prompt_template) as f:
            prompt_template = f.read()

        # Load data
        with open(self.data_dir / "conversations.json") as f:
            conversations = json.load(f)

        # Initialize Claude interface
        claude = ClaudeAPIInterface(model=analyzer.model)

        # Execute analysis
        results = claude.batch_analyze(
            conversations=conversations,
            prompt_template=prompt_template,
            batch_size=analyzer.batch_size
        )

        return results

    def run_claude_cli_analyzer(self, analyzer: AnalyzerConfig, wave_name: str) -> Dict:
        """Run a Claude CLI-based analyzer"""
        from utils.claude_interface import ClaudeCLIInterface

        # Load prompt template
        with open(analyzer.prompt_template) as f:
            prompt_template = f.read()

        # Load previous results for context
        context_data = self.gather_context_for_synthesis(wave_name)

        # Build full prompt
        full_prompt = prompt_template.format(
            data_dir=str(self.data_dir),
            context=json.dumps(context_data, indent=2)
        )

        # Initialize Claude interface
        claude = ClaudeCLIInterface(model=analyzer.model)

        # Execute
        result = claude.run_prompt(full_prompt)

        return {"synthesis": result}

    def gather_context_for_synthesis(self, wave_name: str) -> Dict:
        """Gather results from previous waves for synthesis"""
        context = {}

        for result in self.results:
            if result.success and result.result_path:
                with open(result.result_path) as f:
                    context[f"{result.wave}_{result.analyzer}"] = json.load(f)

        return context

    def run_wave(self, wave: WaveConfig) -> List[AnalysisResult]:
        """Execute a single wave of analysis"""
        self.logger.info(f"Starting wave: {wave.name} (parallel={wave.parallel})")

        if not self.check_dependencies(wave):
            raise RuntimeError(f"Dependencies not met for wave: {wave.name}")

        results = []

        if wave.parallel:
            # Run analyzers in parallel
            max_workers = self.config.get('pipeline', {}).get('parallel_workers', 4)

            with ProcessPoolExecutor(max_workers=max_workers) as executor:
                futures = {
                    executor.submit(self.run_analyzer, analyzer_name, wave.name): analyzer_name
                    for analyzer_name in wave.analyzers
                }

                for future in as_completed(futures):
                    analyzer_name = futures[future]
                    try:
                        result = future.result()
                        results.append(result)
                    except Exception as e:
                        self.logger.error(f"Exception in {analyzer_name}: {e}")
                        results.append(AnalysisResult(
                            analyzer=analyzer_name,
                            wave=wave.name,
                            success=False,
                            error=str(e)
                        ))
        else:
            # Run analyzers sequentially
            for analyzer_name in wave.analyzers:
                result = self.run_analyzer(analyzer_name, wave.name)
                results.append(result)

        self.completed_waves.add(wave.name)
        return results

    def run(self, wave_filter: Optional[int] = None) -> bool:
        """
        Execute the entire pipeline or a specific wave.

        Args:
            wave_filter: If specified, only run this wave number (1-indexed)

        Returns:
            True if all analyses succeeded, False otherwise
        """
        self.logger.info("="*80)
        self.logger.info("Starting Analysis Pipeline")
        self.logger.info(f"Data directory: {self.data_dir}")
        self.logger.info(f"Output directory: {self.output_dir}")
        self.logger.info(f"Cache enabled: {self.use_cache}")
        self.logger.info("="*80)

        start_time = time.time()

        # Filter waves if specified
        waves_to_run = self.waves
        if wave_filter is not None:
            if 1 <= wave_filter <= len(self.waves):
                waves_to_run = [self.waves[wave_filter - 1]]
            else:
                self.logger.error(f"Invalid wave number: {wave_filter} (valid: 1-{len(self.waves)})")
                return False

        # Execute waves
        for wave in waves_to_run:
            wave_results = self.run_wave(wave)
            self.results.extend(wave_results)

        total_time = time.time() - start_time

        # Generate summary
        self.generate_summary(total_time)

        # Check if all succeeded
        all_success = all(r.success for r in self.results)
        return all_success

    def generate_summary(self, total_time: float):
        """Generate execution summary report"""
        summary = {
            "pipeline_execution": {
                "start_time": datetime.now().isoformat(),
                "total_time_seconds": total_time,
                "total_analyzers": len(self.results),
                "successful": sum(1 for r in self.results if r.success),
                "failed": sum(1 for r in self.results if not r.success),
                "waves_completed": list(self.completed_waves)
            },
            "analyzer_results": [
                {
                    "analyzer": r.analyzer,
                    "wave": r.wave,
                    "success": r.success,
                    "execution_time": r.execution_time,
                    "result_path": r.result_path,
                    "error": r.error
                }
                for r in self.results
            ]
        }

        # Save summary
        summary_path = self.output_dir / f"execution_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(summary_path, 'w') as f:
            json.dump(summary, f, indent=2)

        # Print summary
        self.logger.info("="*80)
        self.logger.info("Pipeline Execution Summary")
        self.logger.info(f"Total time: {total_time:.2f}s")
        self.logger.info(f"Analyzers run: {len(self.results)}")
        self.logger.info(f"Successful: {sum(1 for r in self.results if r.success)}")
        self.logger.info(f"Failed: {sum(1 for r in self.results if not r.success)}")
        self.logger.info(f"Summary saved to: {summary_path}")
        self.logger.info("="*80)


def main():
    parser = argparse.ArgumentParser(description="Analysis Pipeline Orchestrator")
    parser.add_argument("--config", default="config/pipeline_config.yaml", help="Path to pipeline configuration")
    parser.add_argument("--data-dir", default=".", help="Directory containing data export files")
    parser.add_argument("--output-dir", default="./pipeline_results", help="Output directory for results")
    parser.add_argument("--wave", type=int, help="Run only specific wave (1-indexed)")
    parser.add_argument("--no-cache", action="store_true", help="Disable result caching")
    parser.add_argument("--dry-run", action="store_true", help="Show execution plan without running")

    args = parser.parse_args()

    # Create orchestrator
    orchestrator = PipelineOrchestrator(
        config_path=args.config,
        data_dir=args.data_dir,
        output_dir=args.output_dir,
        use_cache=not args.no_cache
    )

    if args.dry_run:
        print("Dry run - execution plan:")
        for i, wave in enumerate(orchestrator.waves, 1):
            print(f"\nWave {i}: {wave.name} (parallel={wave.parallel})")
            for analyzer_name in wave.analyzers:
                analyzer = orchestrator.analyzers[analyzer_name]
                print(f"  - {analyzer_name} ({analyzer.type})")
        return

    # Run pipeline
    success = orchestrator.run(wave_filter=args.wave)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
