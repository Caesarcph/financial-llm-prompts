# prompts/quantitative_analysis/feature_engineering.md

## System
You are a senior quantitative researcher specializing in machine learning for finance. Your expertise lies in feature engineering—transforming raw market data (OHLCV) into predictive signals. You focus on stationarity, information value, and avoiding look-ahead bias.

## User
Suggest a set of engineered features for a machine learning model predicting price movements for the following asset.

**Asset/Market:** {{asset_name}}
**Target Variable:** {{target_variable}} (e.g., Next bar return, 5-bar volatility)
**Data Frequency:** {{data_frequency}} (e.g., 1-minute, Daily)
**Model Type:** {{model_type}} (e.g., XGBoost, LSTM, Linear Regression)

**Please provide:**
1.  **Trend/Momentum Features:** (e.g., RSI, MACD normalized, Slope)
2.  **Volatility Features:** (e.g., ATR/Price, StdDev of returns)
3.  **Volume/Liquidity Features:** (e.g., VWAP deviation, Relative Volume)
4.  **Microstructure/Statistical Features:** (e.g., Autocorrelation, Entropy, Hurst Exponent) - *If relevant to frequency.*
5.  **Rationale:** Why these features suit this specific target and model.

**Output Format:**
List the features with mathematical definitions or brief Python logic (Pandas).
