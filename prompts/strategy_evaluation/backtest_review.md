# prompts/strategy_evaluation/backtest_review.md

## System
You are a quantitative analyst reviewing trading strategy backtests. 
You identify strengths, weaknesses, and potential improvements.

## User
Review the following backtest results:

**Strategy:** {{strategy_name}}
**Period:** {{start_date}} to {{end_date}}
**Market:** {{market}}

**Performance Metrics:**
{{metrics}}

**Trade List (sample):**
{{trade_list}}

**Equity Curve:**
{{equity_curve_description}}

**Analysis Required:**
1. **Performance Assessment**: Is this a viable strategy?
2. **Risk Analysis**: What are the key risks?
3. **Edge Identification**: Where does the strategy perform best/worst?
4. **Improvement Suggestions**: How could it be enhanced?
5. **Overfitting Check**: Signs of curve fitting?

**Output:**
```json
{
  "overall_assessment": "promising|mediocre|poor",
  "viability_score": 7,
  "strengths": ["...", "..."],
  "weaknesses": ["...", "..."],
  "risk_concerns": ["...", "..."],
  "best_conditions": "trending markets with...",
  "worst_conditions": "ranging markets when...",
  "overfitting_risk": "low|medium|high",
  "overfitting_indicators": ["..."],
  "improvements": [
    {"suggestion": "...", "expected_impact": "...", "difficulty": "easy|medium|hard"}
  ],
  "recommendation": "proceed with caution|optimize further|abandon"
}
```
