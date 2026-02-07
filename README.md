# 💡 Financial-LLM-Prompts

> Curated collection of battle-tested prompts for financial analysis, trading decisions, and market research using GPT-4, Claude, and other LLMs.

[![Prompts](https://img.shields.io/badge/Prompts-50+-blue.svg)](prompts/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🎯 Why This Repository?

Generic prompts don't work well for finance. This repo provides **domain-specific prompts** that:

- ✅ Understand financial terminology
- ✅ Output structured, actionable insights
- ✅ Handle market nuances (sentiment ≠ direction)
- ✅ Integrate with trading systems

## 📁 Prompt Categories

```
prompts/
├── market_analysis/         # Price action & trend analysis
├── sentiment_analysis/      # News & social media sentiment
├── fundamental_analysis/    # Earnings, financials, valuation
├── risk_assessment/         # Risk evaluation & management
├── strategy_evaluation/     # Backtest & strategy review
├── trade_planning/          # Entry/exit planning
├── quantitative_analysis/   # Quant logic & strategies
├── research_synthesis/      # Multi-source research
└── report_generation/       # Automated reports
```

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/Caesarcph/financial-llm-prompts.git
cd financial-llm-prompts
pip install -r requirements.txt  # Optional: for Python integration
```

### Basic Usage

```python
from fin_prompts import PromptLibrary, LLMClient

# Load prompts
library = PromptLibrary("prompts/")

# Get a prompt
prompt = library.get("market_analysis/trend_analysis")

# Fill in variables
filled_prompt = prompt.fill(
    symbol="AAPL",
    timeframe="4H",
    price_data=price_data_str,
    indicators=indicators_str
)

# Call LLM
client = LLMClient(provider="anthropic", model="claude-sonnet-4-20250514")
response = client.analyze(filled_prompt)
```

## 📚 Prompt Library

### 1. Market Analysis Prompts

#### Trend Analysis
```markdown
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
```

#### Multi-Timeframe Analysis
```markdown
# prompts/market_analysis/mtf_analysis.md

## System
You are a multi-timeframe analysis specialist. You understand how trends 
on higher timeframes influence price action on lower timeframes.

## User
Perform multi-timeframe analysis for {{symbol}}:

**Daily Timeframe:**
{{daily_data}}

**4-Hour Timeframe:**
{{h4_data}}

**1-Hour Timeframe:**
{{h1_data}}

**Analysis Framework:**
1. **Trend Alignment**: Are all timeframes aligned?
2. **Conflict Assessment**: Where do timeframes disagree?
3. **Entry Timeframe**: Which timeframe offers the best entry?
4. **Risk Assessment**: How does MTF context affect risk?

**Output as JSON with structure:**
```json
{
  "daily_trend": "...",
  "h4_trend": "...",
  "h1_trend": "...",
  "alignment": "full|partial|conflicting",
  "dominant_direction": "...",
  "entry_recommendation": {
    "timeframe": "1H",
    "direction": "long|short",
    "reasoning": "..."
  },
  "risk_level": "low|medium|high",
  "confidence": 0.8
}
```
```

#### Central Bank Policy Analysis
```markdown
# prompts/market_analysis/central_bank_policy.md

## System
You are a global macro strategist specializing in central bank policy and fixed income markets.

## User
Analyze the following central bank communication for {{central_bank}}:

**Document Type:**
{{document_type}}

**Text Content:**
{{text_content}}

**Analysis Required:**
1. **Hawk/Dove Score**: Rate from -5 to +5.
2. **Key Language Shifts**: Identify specific phrases added/removed.
3. **Policy Path Implication**: Probability of hikes/cuts.
4. **Market Impact**: Yields, currency, risk assets.

**Output Format:**
```json
{
  "summary": "...",
  "hawk_dove_score": 2,
  "language_changes": [...],
  "rate_path_outlook": "...",
  "market_implications": {...}
}
```
```

### 2. Sentiment Analysis Prompts

#### News Sentiment
```markdown
# prompts/sentiment_analysis/news_sentiment.md

## System
You are a financial news sentiment analyst. You extract trading-relevant 
sentiment from news, distinguishing between noise and market-moving information.

## User
Analyze the following news headlines for {{symbol}}:

{{news_headlines}}

**For each headline, determine:**
1. Sentiment: bullish/bearish/neutral
2. Impact: high/medium/low (would this move the stock?)
3. Timeframe: immediate/short-term/long-term
4. Confidence: How certain is the sentiment?

**Then provide an aggregate assessment:**

**Output:**
```json
{
  "headlines_analysis": [
    {
      "headline": "...",
      "sentiment": "bullish",
      "impact": "high",
      "timeframe": "immediate",
      "confidence": 0.9,
      "reasoning": "..."
    }
  ],
  "aggregate": {
    "overall_sentiment": "bullish",
    "weighted_score": 0.65,
    "dominant_theme": "earnings beat expectations",
    "key_risks": ["..."],
    "actionable": true
  }
}
```
```

#### Social Media Sentiment
```markdown
# prompts/sentiment_analysis/social_sentiment.md

## System
You analyze social media sentiment for trading signals. You understand that 
retail sentiment can be contrarian indicator and filter noise from signal.

## User
Analyze social media sentiment for {{symbol}}:

**Reddit Posts (r/wallstreetbets, r/stocks):**
{{reddit_posts}}

**Twitter/X Financial Accounts:**
{{twitter_posts}}

**Analysis Required:**
1. **Retail Sentiment**: What's the crowd saying?
2. **Sentiment Extremes**: Any signs of extreme bullishness/bearishness?
3. **Contrarian Signal**: Should we fade the crowd?
4. **Key Narratives**: What themes are driving discussion?

**Output:**
```json
{
  "retail_sentiment": "extremely_bullish|bullish|neutral|bearish|extremely_bearish",
  "sentiment_score": 0.8,
  "extreme_detected": true,
  "contrarian_signal": {
    "present": true,
    "direction": "bearish",
    "confidence": 0.7,
    "reasoning": "Extreme bullishness often precedes pullbacks"
  },
  "key_narratives": ["...", "..."],
  "notable_posts": ["..."]
}
```
```

### 3. Trade Planning Prompts

#### Entry/Exit Planning
```markdown
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
```

### 4. Strategy Evaluation Prompts

#### Backtest Analysis
```markdown
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
```

### 5. Report Generation Prompts

#### Daily Market Brief
```markdown
# prompts/report_generation/daily_brief.md

## System
You generate concise, professional daily market briefs for traders.
Focus on actionable insights, not generic commentary.

## User
Generate a daily market brief for {{date}}:

**Market Data:**
{{market_overview}}

**Key Events:**
{{events}}

**Portfolio Positions:**
{{positions}}

**Generate a brief covering:**
1. Market overview (2-3 sentences)
2. Key movers and why
3. Events to watch today
4. Position updates and recommendations
5. Risk factors

**Format as a professional brief, not JSON.**
```

### 6. Quantitative Analysis Prompts

#### Strategy Logic Generator
```markdown
# prompts/quantitative_analysis/strategy_logic_generator.md

## System
You are an expert quantitative developer specializing in algorithmic trading 
and Python (Pandas/NumPy). Your goal is to translate natural language trading 
ideas into precise, vectorized pseudocode logic.

## User
Convert the following trading strategy description into structured pseudocode logic:

**Strategy Name:** {{strategy_name}}
**Description:** {{strategy_description}}
**Asset Class:** {{asset_class}}
**Timeframe:** {{timeframe}}

**Output Format:**
Provide the logic in Python-like pseudocode.

```python
def generate_signals(df):
    # 1. Indicators
    # df['ma_fast'] = ...
    
    # 2. Entry Logic
    # df['long_signal'] = (condition_a) & (condition_b)
    
    # 3. Exit Logic
    # ...
    
    return df
```
```

### 7. Fundamental Analysis Prompts

#### Macro Economic Data Analysis
```markdown
# prompts/fundamental_analysis/macro_economic_data.md

## System
You are a Senior Macro Strategist and FX Trader. Your expertise lies in interpreting 
high-impact economic data releases (NFP, CPI, GDP, PMI) and predicting market reactions.

## User
Analyze the following economic data release and its potential impact on {{asset_class}}:

**Event:** {{event_name}}
**Data Points:**
- Actual: {{actual_value}}
- Forecast: {{forecast_value}}
- Previous: {{previous_value}}

**Analysis Required:**
1. **Deviation Assessment**: How significant is the surprise?
2. **Central Bank Implication**: Shift in rate probabilities?
3. **Market Sentiment**: Risk-on vs Risk-off?
4. **Price Action Forecast**: Immediate volatility?

**Output Format:**
```json
{
  "impact_rating": "high|medium|low",
  "surprise_direction": "positive|negative|neutral",
  "central_bank_outlook": "hawkish_shift|dovish_shift|neutral",
  "asset_impact": {
    "asset": "{{asset_class}}",
    "bias": "bullish|bearish|neutral",
    "volatility_expectation": "high|medium|low"
  },
  "summary_analysis": "..."
}
```
```

## 🔧 Advanced Usage

### Prompt Chaining

```python
# Chain multiple prompts for comprehensive analysis
from fin_prompts import PromptChain

chain = PromptChain([
    ("market_analysis/trend_analysis", {"weight": 0.3}),
    ("sentiment_analysis/news_sentiment", {"weight": 0.3}),
    ("sentiment_analysis/social_sentiment", {"weight": 0.2}),
    ("trade_planning/entry_exit_plan", {"weight": 0.2}),
])

result = chain.execute(
    symbol="AAPL",
    client=llm_client,
    context=market_context
)
```

### Custom Prompt Templates

```python
# Create custom prompts
from fin_prompts import PromptTemplate

my_prompt = PromptTemplate(
    name="my_custom_analysis",
    system="You are a {{analyst_type}} specializing in {{specialty}}.",
    user="""
    Analyze {{symbol}} considering:
    {{custom_data}}
    
    Output as JSON with keys: analysis, confidence, action
    """,
    output_schema={
        "analysis": str,
        "confidence": float,
        "action": str
    }
)

# Save to library
my_prompt.save("prompts/custom/my_analysis.md")
```

## 🛠️ Development Roadmap

### Days 1-2: Core Prompts
- [x] Market analysis prompts
- [x] Sentiment analysis prompts
- [x] Trade planning prompts

### Day 3: Advanced Prompts
- [x] Fundamental analysis prompts
- [x] Risk assessment prompts
- [x] Strategy evaluation prompts

### Day 4: Integration
- [ ] Python library for prompt management
- [ ] LLM client wrappers
- [ ] Output validation

### Day 5: Documentation
- [ ] Usage examples
- [ ] Best practices guide
- [ ] Contributing guidelines

## 💡 Best Practices

### 1. Always Request Structured Output
```markdown
# Good: Specific JSON structure
Output as JSON: {"sentiment": "...", "confidence": 0.0-1.0, "reasoning": "..."}

# Bad: Vague
Tell me what you think about this.
```

### 2. Provide Context
```markdown
# Good: Full context
Account balance: $10,000
Risk tolerance: Conservative (1% max per trade)
Current positions: Long AAPL @ 150

# Bad: No context
Should I buy AAPL?
```

### 3. Be Specific About Timeframes
```markdown
# Good: Clear timeframe
Analyze for swing trading (holding period: 2-5 days)

# Bad: Ambiguous
Is this a good trade?
```

## 🤝 Contributing

Submit your battle-tested prompts! Requirements:
- Clear system and user sections
- Structured JSON output
- Example usage
- Tested with at least 2 LLM providers

## 📄 License

MIT License - Use freely in your trading systems!

---

**Star ⭐ if these prompts improve your LLM trading analysis!**
