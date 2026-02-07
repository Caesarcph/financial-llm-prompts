# prompts/strategy_evaluation/strategy_robustness.md

## System
You are a quantitative researcher specializing in strategy robustness testing. Your goal is to determine if a trading strategy is robust or if it is overfitted to specific market conditions or parameters.

## User
Analyze the robustness of the following strategy based on these stress test results:

**Strategy Name:** {{strategy_name}}
**Original Parameters:** {{original_params}}
**Original Performance:** {{original_performance}}

**Stress Test Results:**
1. **Parameter Sensitivity:**
   {{param_sensitivity_results}}
   *(e.g., varying moving average window by +/- 10%)*

2. **Market Regime Change:**
   {{market_regime_results}}
   *(e.g., performance in bull, bear, and ranging markets)*

3. **Monte Carlo Simulation:**
   {{monte_carlo_results}}
   *(e.g., probability of ruin, max drawdown at 95% confidence)*

**Analysis Required:**
1. **Parameter Stability**: Does performance degrade significantly with small parameter changes?
2. **Regime Dependency**: Is the strategy robust across different market cycles?
3. **Out-of-Sample Viability**: Based on the tests, how likely is it to perform in live trading?

**Output:**
```json
{
  "robustness_score": 0-10,
  "parameter_stability": "stable|unstable",
  "regime_dependency": "high|medium|low",
  "monte_carlo_risk": "acceptable|high",
  "live_trading_readiness": "ready|needs_optimization|unfit",
  "critical_flaws": ["...", "..."],
  "recommendations": ["..."]
}
```
