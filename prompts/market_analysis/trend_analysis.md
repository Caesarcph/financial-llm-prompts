# prompts/market_analysis/trend_analysis.md

## System
You are an expert technical analyst specializing in trend identification 
and price action analysis. Provide clear, actionable insights.

## User
Analyze the following price data for {{symbol}} on the {{timeframe}} timeframe:

**Recent Price Action:**
{{price_data}}

**Technical Indicators:**
{{indicators}}

**Analysis Required:**
1. **Primary Trend**: Identify the dominant trend (bullish/bearish/ranging)
2. **Trend Strength**: Rate 1-10 with justification
3. **Key Levels**: 
   - Support levels (up to 3)
   - Resistance levels (up to 3)
4. **Pattern Recognition**: Any notable chart patterns forming?
5. **Momentum Assessment**: Is momentum confirming or diverging from price?

**Output Format:**
```json
{
  "trend": "bullish|bearish|ranging",
  "trend_strength": 7,
  "trend_reasoning": "...",
  "support_levels": [150.00, 148.50, 145.00],
  "resistance_levels": [155.00, 158.00, 160.00],
  "patterns": ["ascending triangle forming", "..."],
  "momentum": "confirming|diverging",
  "momentum_details": "...",
  "bias": "bullish|bearish|neutral",
  "confidence": 0.75
}
```
