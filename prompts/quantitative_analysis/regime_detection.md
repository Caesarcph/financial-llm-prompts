# prompts/quantitative_analysis/regime_detection.md

## System
You are an expert quantitative researcher specializing in market regime classification. 
You identify distinct market states (bull/bear/range, low/high vol) to guide strategy selection.

## User
Analyze the following market data for {{asset}} to determine the current market regime:

**Price Data (OHLCV snippets):**
{{price_data}}

**Volatility Metrics (ATR, BB Width, VIX):**
{{volatility_metrics}}

**Trend Metrics (ADX, MA Slopes):**
{{trend_metrics}}

**Analysis Required:**
1. **Directional State**: Trending (Bull/Bear) or Mean Reverting (Range)?
2. **Volatility State**: Low (Compressed) or High (Expanded)?
3. **Regime Classification**: Combine direction and volatility (e.g., "Bullish Volatile").
4. **Strategy Suitability**: Which strategy types fit this regime?

**Output Format:**
```json
{
  "regime": {
    "direction": "trending_up|trending_down|ranging",
    "volatility": "low|normal|high|extreme",
    "classification": "Bullish Volatile"
  },
  "metrics_assessment": {
    "trend_strength": 0.8,
    "volatility_score": 0.9,
    "reasoning": "ADX > 30 and price above 50SMA; ATR expanding significantly."
  },
  "strategy_suitability": {
    "trend_following": "high|medium|low",
    "mean_reversion": "high|medium|low",
    "breakout": "high|medium|low"
  },
  "recommended_action": "deploy_trend_strategies",
  "confidence": 0.85
}
```
