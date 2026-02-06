# prompts/market_analysis/mtf_analysis.md

## System
You are a multi-timeframe analysis specialist. You understand how trends 
on higher timeframes influence price action on lower timeframes.

## User
Perform multi-timeframe analysis for {{symbol}}:

**Daily Timeframe:**
{{daily_data}}

**4-Hour Timeframe:**
{{h4_data}}

**1-Hour Timeframe:**
{{h1_data}}

**Analysis Framework:**
1. **Trend Alignment**: Are all timeframes aligned?
2. **Conflict Assessment**: Where do timeframes disagree?
3. **Entry Timeframe**: Which timeframe offers the best entry?
4. **Risk Assessment**: How does MTF context affect risk?

**Output as JSON with structure:**
```json
{
  "daily_trend": "...",
  "h4_trend": "...",
  "h1_trend": "...",
  "alignment": "full|partial|conflicting",
  "dominant_direction": "...",
  "entry_recommendation": {
    "timeframe": "1H",
    "direction": "long|short",
    "reasoning": "..."
  },
  "risk_level": "low|medium|high",
  "confidence": 0.8
}
```
