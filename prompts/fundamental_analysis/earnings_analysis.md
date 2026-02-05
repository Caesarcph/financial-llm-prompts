# prompts/fundamental_analysis/earnings_analysis.md

## System
You are a seasoned fundamental equity analyst. Your goal is to dissect earnings reports to determine the true health of a company, looking beyond the headline numbers to identify earnings quality, guidance shifts, and management tone.

## User
Analyze the recent earnings report for {{symbol}} based on the provided data:

**Headline Numbers:**
{{headline_metrics}} (EPS, Revenue vs Consensus)

**Guidance:**
{{guidance_text}}

**Key Segments/Highlights:**
{{segments_data}}

**Management Commentary/Transcript Snippets:**
{{transcript_snippets}}

**Analysis Required:**
1. **Quality of Beat/Miss**: Was it driven by organic growth or one-offs (tax cuts, buybacks)?
2. **Guidance Evolution**: Is management raising, maintaining, or cutting outlook? Why?
3. **Margin Analysis**: Are margins expanding or contracting? (Pricing power vs cost inflation)
4. **Sentiment Check**: Is management confident or defensive?

**Output Format:**
```json
{
  "headline_assessment": "strong_beat|soft_beat|mixed|miss",
  "earnings_quality_score": 7,
  "quality_reasoning": "Beat driven by 15% volume growth, not just price hikes...",
  "guidance_change": "raised|unchanged|lowered",
  "key_drivers": ["Cloud growth +20%", "China headwinds"],
  "margin_trend": "expanding|contracting",
  "management_tone": "confident|cautious|evasive",
  "red_flags": ["Inventory build-up", "AR growing faster than sales"],
  "investment_thesis_impact": "positive|neutral|negative"
}
```
