#!/usr/bin/env python3
"""
Claude Interface Utilities
===========================

Provides unified interface for Claude interactions via:
1. Anthropic Python SDK (API)
2. Claude CLI

Handles batching, rate limiting, error recovery, and result formatting.
"""

import json
import os
import subprocess
import time
from typing import Dict, List, Any, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging


class ClaudeAPIInterface:
    """
    Interface for Claude via Anthropic Python SDK.

    Best for:
    - Batch processing (parallel API calls)
    - Programmatic control
    - Cost optimization (Haiku for simple tasks)
    """

    def __init__(self, model: str = "claude-haiku-4-20250514", max_tokens: int = 4096):
        try:
            from anthropic import Anthropic
        except ImportError:
            raise ImportError("anthropic package not installed. Run: pip install anthropic")

        self.model = model
        self.max_tokens = max_tokens
        self.client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
        self.logger = logging.getLogger(__name__)

    def analyze_single(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """
        Execute a single analysis prompt.

        Args:
            prompt: The analysis prompt
            system_prompt: Optional system prompt for context

        Returns:
            Claude's response as string
        """
        messages = [{"role": "user", "content": prompt}]

        kwargs = {
            "model": self.model,
            "max_tokens": self.max_tokens,
            "messages": messages
        }

        if system_prompt:
            kwargs["system"] = system_prompt

        self.logger.debug(f"Sending prompt to {self.model} (length: {len(prompt)} chars)")

        response = self.client.messages.create(**kwargs)

        return response.content[0].text

    def batch_analyze(
        self,
        conversations: List[Dict],
        prompt_template: str,
        batch_size: int = 20,
        max_workers: int = 4,
        system_prompt: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Analyze multiple conversations in parallel batches.

        Args:
            conversations: List of conversation objects to analyze
            prompt_template: Template with {conversation} placeholder
            batch_size: Number of conversations to process
            max_workers: Number of parallel API calls
            system_prompt: Optional system prompt

        Returns:
            Dictionary of results keyed by conversation UUID
        """
        self.logger.info(f"Starting batch analysis of {len(conversations)} conversations")
        self.logger.info(f"Model: {self.model}, Batch size: {batch_size}, Workers: {max_workers}")

        # Limit to batch_size conversations
        conversations_to_analyze = conversations[:batch_size]

        results = {}
        start_time = time.time()

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all analysis tasks
            future_to_conv = {}
            for conv in conversations_to_analyze:
                # Format prompt with conversation data
                conv_text = self._format_conversation(conv)
                prompt = prompt_template.format(conversation=conv_text)

                # Submit task
                future = executor.submit(self.analyze_single, prompt, system_prompt)
                future_to_conv[future] = conv

            # Collect results as they complete
            for i, future in enumerate(as_completed(future_to_conv), 1):
                conv = future_to_conv[future]
                conv_id = conv.get('uuid', f'conv_{i}')

                try:
                    result = future.result()
                    results[conv_id] = {
                        "conversation_name": conv.get('name', 'Untitled'),
                        "analysis": result,
                        "success": True
                    }
                    self.logger.info(f"Completed {i}/{len(conversations_to_analyze)}: {conv.get('name', 'Untitled')[:50]}")

                except Exception as e:
                    self.logger.error(f"Failed analysis for {conv_id}: {e}")
                    results[conv_id] = {
                        "conversation_name": conv.get('name', 'Untitled'),
                        "error": str(e),
                        "success": False
                    }

        elapsed = time.time() - start_time
        self.logger.info(f"Batch analysis completed in {elapsed:.2f}s")

        return {
            "model": self.model,
            "conversations_analyzed": len(conversations_to_analyze),
            "successful": sum(1 for r in results.values() if r.get('success')),
            "failed": sum(1 for r in results.values() if not r.get('success')),
            "execution_time_seconds": elapsed,
            "results": results
        }

    def _format_conversation(self, conv: Dict, max_messages: int = 50) -> str:
        """
        Format conversation for analysis prompt.

        Args:
            conv: Conversation object
            max_messages: Maximum messages to include (to avoid token limits)

        Returns:
            Formatted conversation text
        """
        messages = conv.get('chat_messages', [])[:max_messages]

        formatted = f"Conversation: {conv.get('name', 'Untitled')}\n"
        formatted += f"Date: {conv.get('created_at', 'Unknown')}\n"
        formatted += f"Messages: {len(messages)}\n\n"

        for msg in messages:
            sender = msg.get('sender', 'unknown').upper()
            text = msg.get('text', '')[:500]  # Limit message length
            formatted += f"{sender}: {text}\n\n"

        return formatted


class ClaudeCLIInterface:
    """
    Interface for Claude via CLI.

    Best for:
    - Complex synthesis tasks needing project context
    - Interactive-style prompts
    - Leveraging Claude CLI's conversation management
    """

    def __init__(self, model: Optional[str] = None):
        self.model = model
        self.logger = logging.getLogger(__name__)

        # Check if claude CLI is available
        try:
            subprocess.run(["claude", "--version"], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            raise RuntimeError("claude CLI not found. Install from: https://github.com/anthropics/anthropic-claude-cli")

    def run_prompt(self, prompt: str, project_context: Optional[str] = None) -> str:
        """
        Execute a prompt via Claude CLI.

        Args:
            prompt: The prompt to execute
            project_context: Optional project context to set

        Returns:
            Claude's response as string
        """
        self.logger.info(f"Executing Claude CLI prompt (length: {len(prompt)} chars)")

        cmd = ["claude", "-p", prompt]

        if self.model:
            cmd.extend(["-m", self.model])

        # Execute
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )

        return result.stdout

    def run_interactive_analysis(
        self,
        context_files: List[str],
        analysis_prompt: str
    ) -> str:
        """
        Run analysis with file context (like Claude Code does).

        Args:
            context_files: List of file paths to provide as context
            analysis_prompt: The analysis question/task

        Returns:
            Claude's response
        """
        # Build prompt with file context
        full_prompt = "Context files:\n"
        for filepath in context_files:
            full_prompt += f"- {filepath}\n"

        full_prompt += f"\nAnalysis task:\n{analysis_prompt}"

        return self.run_prompt(full_prompt)


class ClaudeInterfaceFactory:
    """
    Factory for creating appropriate Claude interface based on use case.
    """

    @staticmethod
    def create(
        interface_type: str,
        model: Optional[str] = None,
        **kwargs
    ):
        """
        Create Claude interface.

        Args:
            interface_type: 'api' or 'cli'
            model: Model to use
            **kwargs: Additional arguments for interface

        Returns:
            ClaudeAPIInterface or ClaudeCLIInterface
        """
        if interface_type == 'api':
            return ClaudeAPIInterface(model=model or "claude-haiku-4-20250514", **kwargs)
        elif interface_type == 'cli':
            return ClaudeCLIInterface(model=model)
        else:
            raise ValueError(f"Unknown interface type: {interface_type}")


# Example usage patterns
if __name__ == "__main__":
    # Example 1: Batch analysis via API
    print("Example 1: Batch API Analysis")
    print("-" * 50)

    api = ClaudeAPIInterface(model="claude-haiku-4-20250514")

    # Mock conversations
    conversations = [
        {
            "uuid": "conv-1",
            "name": "Test conversation 1",
            "chat_messages": [
                {"sender": "human", "text": "Hello"},
                {"sender": "assistant", "text": "Hi there!"}
            ]
        }
    ]

    prompt_template = """
Analyze this conversation for sentiment:

{conversation}

Provide sentiment (positive/negative/neutral) and confidence.
"""

    # results = api.batch_analyze(conversations, prompt_template, batch_size=5)
    # print(json.dumps(results, indent=2))

    # Example 2: Synthesis via CLI
    print("\nExample 2: Synthesis via CLI")
    print("-" * 50)

    cli = ClaudeCLIInterface(model="claude-sonnet-4-5-20250929")

    synthesis_prompt = """
Based on the analysis results in ./results/, generate a comprehensive
synthesis report covering:
1. Key patterns discovered
2. Notable anomalies
3. Recommendations for future analysis
"""

    # response = cli.run_prompt(synthesis_prompt)
    # print(response)
