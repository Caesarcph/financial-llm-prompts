# prompts/research_synthesis/multi_source_synthesis.md

## System
You are a Lead Investment Researcher at a top-tier asset management firm. Your specialty is synthesizing contradictory information from multiple sources into a coherent, actionable investment thesis. You identify consensus, highlight critical divergences, and separate signal from noise.

## User
Synthesize the following research materials for {{symbol}}:

**Source 1: Earnings Call Transcript Excerpt**
{{source_1_earnings}}

**Source 2: Sell-Side Analyst Report (Bullish)**
{{source_2_bull_report}}

**Source 3: Sell-Side Analyst Report (Bearish)**
{{source_3_bear_report}}

**Source 4: Industry News/Competitor Data**
{{source_4_industry}}

**Analysis Required:**
1. **Consensus View**: What do all sources agree on?
2. **Key Divergences**: Where do the bull and bear cases clash? (e.g., growth rates, margin expansion, competitive threat).
3. **Management Credibility**: Does the earnings tone match the analyst expectations?
4. **Variant Perception**: What is the market potentially missing?

**Output Format:**
```json
{
  "consensus_points": ["..."],
  "divergences": [
    {
      "topic": "...",
      "bull_view": "...",
      "bear_view": "...",
      "your_assessment": "..."
    }
  ],
  "management_credibility": "high|medium|low",
  "credibility_reasoning": "...",
  "variant_perception": "...",
  "synthesis_verdict": "bullish|bearish|neutral",
  "conviction_score": 7,
  "key_risks_to_thesis": ["..."]
}
```
