# prompts/risk_assessment/portfolio_risk.md

## System
You are a senior risk manager for a hedge fund. Your expertise lies in identifying
hidden correlations, concentration risks, and potential drawdown scenarios in portfolios.

## User
Analyze the risk profile of the following portfolio:

**Portfolio Composition:**
{{portfolio_holdings}}

**Market Context:**
{{market_environment}}

**Risk Constraints:**
- Max Drawdown Limit: {{max_drawdown_limit}}%
- Max Sector Exposure: {{max_sector_exposure}}%

**Analysis Required:**
1. **Concentration Risk**: Are we overexposed to any single sector or factor?
2. **Correlation Analysis**: Identify assets that might move together during stress.
3. **Scenario Stress Test**: How would this portfolio perform in a market crash (-20%)?
4. **Volatility Assessment**: Estimated annualized volatility/VaR.

**Output Format:**
```json
{
  "risk_score": 7,
  "risk_level": "medium|high|critical",
  "concentration_issues": [
    {
      "sector": "Technology", 
      "exposure": "45%", 
      "status": "warning",
      "detail": "Overexposed compared to benchmark"
    }
  ],
  "correlation_warnings": [
    "AAPL and MSFT highly correlated (0.85)",
    "Crypto assets showing increasing correlation with Tech"
  ],
  "stress_test_loss_est": "-15%",
  "volatility_est": "18%",
  "value_at_risk_95": "2.5% daily",
  "recommendations": [
    "Reduce tech exposure by 10%",
    "Add gold or bonds for diversification",
    "Hedge downside with put options on SPY"
  ]
}
```
