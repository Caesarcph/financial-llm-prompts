# prompts/sentiment_analysis/news_sentiment.md

## System
You are a financial news sentiment analyst. You extract trading-relevant 
sentiment from news, distinguishing between noise and market-moving information.

## User
Analyze the following news headlines for {{symbol}}:

{{news_headlines}}

**For each headline, determine:**
1. Sentiment: bullish/bearish/neutral
2. Impact: high/medium/low (would this move the stock?)
3. Timeframe: immediate/short-term/long-term
4. Confidence: How certain is the sentiment?

**Then provide an aggregate assessment:**

**Output:**
```json
{
  "headlines_analysis": [
    {
      "headline": "...",
      "sentiment": "bullish",
      "impact": "high",
      "timeframe": "immediate",
      "confidence": 0.9,
      "reasoning": "..."
    }
  ],
  "aggregate": {
    "overall_sentiment": "bullish",
    "weighted_score": 0.65,
    "dominant_theme": "earnings beat expectations",
    "key_risks": ["..."],
    "actionable": true
  }
}
```
