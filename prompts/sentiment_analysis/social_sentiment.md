# prompts/sentiment_analysis/social_sentiment.md

## System
You analyze social media sentiment for trading signals. You understand that 
retail sentiment can be contrarian indicator and filter noise from signal.

## User
Analyze social media sentiment for {{symbol}}:

**Reddit Posts (r/wallstreetbets, r/stocks):**
{{reddit_posts}}

**Twitter/X Financial Accounts:**
{{twitter_posts}}

**Analysis Required:**
1. **Retail Sentiment**: What's the crowd saying?
2. **Sentiment Extremes**: Any signs of extreme bullishness/bearishness?
3. **Contrarian Signal**: Should we fade the crowd?
4. **Key Narratives**: What themes are driving discussion?

**Output:**
```json
{
  "retail_sentiment": "extremely_bullish|bullish|neutral|bearish|extremely_bearish",
  "sentiment_score": 0.8,
  "extreme_detected": true,
  "contrarian_signal": {
    "present": true,
    "direction": "bearish",
    "confidence": 0.7,
    "reasoning": "Extreme bullishness often precedes pullbacks"
  },
  "key_narratives": ["...", "..."],
  "notable_posts": ["..."]
}
```
