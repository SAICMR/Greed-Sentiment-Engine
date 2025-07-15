# Fear & Greed Sentiment Engine

## Overview
A Python-based engine to analyze social, news, and financial data for sentiment, correlate with price action, and generate simple trading signals (Buy, Sell, Hold) based on Fear & Greed analysis.

## Features
- Ingests data from Twitter, Reddit, and news (mock or real APIs)
- Integrates financial data (stocks/crypto)
- Sentiment analysis using VADER/FinBERT
- Signal generation based on sentiment and price trends
- Outputs structured JSON reports

## Setup
1. Clone the repo or download the ZIP.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Add your API keys to `.env` (see template in the file).

## File Structure
```
fear_greed_engine/
│
├── data/
│   ├── twitter_sample.json
│   ├── python fear_greed_engine/main.py BTC
│   └── financial_data.json
│
├── modules/
│   ├── ingestion.py
│   ├── sentiment.py
│   └── signal.py
│
├── outputs/
│   └── signals.json
│
├── main.py
├── requirements.txt
├── README.md
└── .env
```

## Usage
Run the main script with an asset symbol:
```bash
python main.py BTC
```

## Roadmap
See project plan for daily milestones and deliverables. 
