# prompts/trade_planning/entry_exit_plan.md

## System
You are a trade planning specialist. You create precise, executable trade 
plans with clear entries, exits, and risk parameters.

## User
Create a trade plan for {{symbol}} based on the following analysis:

**Technical Analysis:**
{{technical_analysis}}

**Sentiment Analysis:**
{{sentiment_analysis}}

**Account Context:**
- Account Balance: ${{account_balance}}
- Max Risk Per Trade: {{risk_percent}}%
- Preferred Timeframe: {{timeframe}}

**Generate a complete trade plan:**

**Output:**
```json
{
  "trade_plan": {
    "direction": "long|short",
    "confidence": 0.75,
    "reasoning": "..."
  },
  "entry": {
    "type": "market|limit|stop",
    "price": 150.00,
    "conditions": ["RSI < 30", "Price touches support"]
  },
  "stop_loss": {
    "price": 147.00,
    "pips": 30,
    "reasoning": "Below recent swing low"
  },
  "take_profit": [
    {"level": 1, "price": 155.00, "size": "50%"},
    {"level": 2, "price": 160.00, "size": "50%"}
  ],
  "position_size": {
    "lots": 0.05,
    "risk_amount": 150.00,
    "risk_percent": 1.0
  },
  "risk_reward": 2.5,
  "invalidation": "Close below 145.00 invalidates bullish thesis"
}
```
