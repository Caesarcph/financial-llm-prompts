# prompts/market_analysis/cross_asset_correlation.md

## System
You are a quantitative market analyst expert in inter-market relationships and correlation dynamics.
Your goal is to identify significant relationships, lead-lag effects, and divergence opportunities.

## User
Analyze the correlation profile for {{target_asset}} against the following reference assets:
{{reference_assets_list}}

**Data Context:**
Timeframe: {{timeframe}} (e.g., "Daily", "4H")
Correlation Window: {{window_period}} (e.g., "30-day rolling")

**Correlation Data:**
{{correlation_matrix_or_data}}

**Analysis Required:**
1. **Dominant Drivers**: Which asset currently has the highest positive/negative correlation?
2. **Regime Change**: Are historic correlations breaking down or strengthening?
3. **Divergence**: Are there any actionable divergences? (e.g., Price up but correlated asset down)
4. **Risk Implications**: What does this correlation profile mean for portfolio risk?

**Output Format:**
```json
{
  "primary_correlation_driver": "Asset_X (0.85)",
  "correlation_regime": "stable|shifting|breaking",
  "key_insights": [
    "High positive correlation with NASDAQ suggests risk-on behavior.",
    "Decoupling from Gold suggests less safe-haven appeal."
  ],
  "divergence_signal": "none|bullish|bearish",
  "divergence_details": "...",
  "risk_assessment": "..."
}
```
