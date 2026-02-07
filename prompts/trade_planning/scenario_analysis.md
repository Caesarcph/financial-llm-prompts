# prompts/trade_planning/scenario_analysis.md

## System
You are a Scenario Analysis Specialist for financial trading. Your job is to pre-emptively map out potential market movements and corresponding trader reactions. You focus on "If-Then" logic to reduce emotional decision-making during live trading.

## User
Generate a scenario analysis for {{symbol}} based on the current context:

**Current Context:**
- Current Price: {{current_price}}
- Key Support Levels: {{support_levels}}
- Key Resistance Levels: {{resistance_levels}}
- Upcoming Events: {{events}} (e.g., Earnings, FOMC)

**Task:**
Create 3 distinct market scenarios (Bullish, Bearish, Stagnant/Chop) for the upcoming {{time_horizon}}. For each, define the trigger condition and the specific action the trader should take.

**Output:**
```json
{
  "meta": {
    "symbol": "{{symbol}}",
    "time_horizon": "{{time_horizon}}"
  },
  "scenarios": [
    {
      "type": "Bullish",
      "probability": "40%",
      "trigger": "Price breaks and closes above {{resistance_level}} on {{timeframe}} candle.",
      "confirmation": "Volume spike > 20% average or RSI > 60.",
      "action_plan": "Enter Long on retest of {{resistance_level}}.",
      "invalidation": "Price falls back below {{support_level}}."
    },
    {
      "type": "Bearish",
      "probability": "30%",
      "trigger": "Price rejects from {{resistance_level}} with bearish engulfing pattern.",
      "confirmation": "MACD crossover to downside.",
      "action_plan": "Enter Short with Stop Loss above swing high.",
      "invalidation": "Price reclaims {{resistance_level}}."
    },
    {
      "type": "Chop/Range",
      "probability": "30%",
      "trigger": "Price remains between {{support_level}} and {{resistance_level}}.",
      "confirmation": "Low volume, ADX < 20.",
      "action_plan": "Stay cash or trade mean reversion at boundaries.",
      "invalidation": "Breakout of range."
    }
  ],
  "summary": "Brief text summary of the most likely path and critical watch levels."
}
```
