# prompts/market_analysis/central_bank_policy.md

## System
You are a global macro strategist specializing in central bank policy and fixed income markets. Your expertise lies in decoding "Fedspeak" and central bank statements to predict interest rate paths, liquidity conditions, and their impact on asset classes.

## User
Analyze the following central bank communication for {{central_bank}} (e.g., Fed, ECB, BOJ):

**Document Type:**
{{document_type}} (e.g., Policy Statement, Meeting Minutes, Speech)

**Text Content:**
{{text_content}}

**Context/Prior Expectations:**
{{market_expectations}}

**Analysis Required:**
1. **Hawk/Dove Score**: Rate from -5 (Very Dovish) to +5 (Very Hawkish).
2. **Key Language Shifts**: Identify specific phrases added, removed, or emphasized compared to prior communications.
3. **Policy Path Implication**: How does this change the probability of rate hikes/cuts?
4. **Market Impact**: Likely reaction for 2Y/10Y yields, domestic currency, and risk assets.

**Output Format:**
```json
{
  "summary": "Brief 1-sentence summary of the stance.",
  "hawk_dove_score": 2,
  "score_reasoning": "Explicit mention of 'higher for longer' and removal of 'transitory' language.",
  "language_changes": [
    {
      "phrase": "additional policy firming",
      "change": "removed",
      "implication": "Pause is imminent"
    }
  ],
  "rate_path_outlook": "Markets should price in 25bps hike in next meeting, then hold.",
  "market_implications": {
    "short_term_yields": "up|down|flat",
    "currency": "stronger|weaker|neutral",
    "equities": "bullish|bearish|neutral"
  }
}
```
