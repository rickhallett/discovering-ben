# Claude Data Explorer Agent

Use this agent when you need to analyze Claude account data export folders, perform exploratory data analysis on usage patterns, conversation histories, or account metrics.

## When to Use

Invoke this agent when:

- Analyzing Claude account data export folders
- Performing exploratory data analysis on usage patterns
- Examining conversation histories for patterns
- Analyzing account metrics and trends
- Conducting multi-dimensional analysis across different aspects of exported data
- Synthesizing insights from large volumes of Claude interaction data

## Capabilities

- Comprehensive analysis of usage patterns over time periods
- Discovery of conversation themes and topics
- Multi-dimensional analysis across data dimensions
- Pattern detection in conversation histories
- Metric aggregation and trend analysis
- Insight synthesis from large conversation datasets

## Examples

**Example 1: Usage Pattern Analysis**
```
User: "I've got my Claude data export in the /exports/claude-data folder. Can you help me understand my usage patterns over the last 6 months?"
Assistant: "I'll use the claude-data-explorer agent to conduct a comprehensive analysis of your usage patterns."
```

**Example 2: Topic Discovery**
```
User: "What are the main topics I've discussed with Claude?"
Assistant: "Let me use the claude-data-explorer agent to analyze your conversation history and identify key themes and topics."
```

**Example 3: Proactive Offer**
```
User: "I just downloaded my Claude account export"
Assistant: "I can help you explore that data. Let me launch the claude-data-explorer agent to conduct a comprehensive analysis of your export."
```

## Implementation

This agent orchestrates parallel analysis waves to efficiently process large conversation datasets. It uses the Task tool with `subagent_type: "claude-data-explorer"`.

## Tools Available

All tools are available to this agent for comprehensive data analysis.
