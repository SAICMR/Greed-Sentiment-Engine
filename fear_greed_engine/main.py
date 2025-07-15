import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))
from modules.ingestion import ingest_mock_data
from modules.sentiment import analyze_sentiment
from modules.signal import generate_signal

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <SYMBOL>")
        return
    symbol = sys.argv[1]
    # Ingest mock Twitter data
    twitter_data = ingest_mock_data('twitter')
    # Analyze sentiment for each tweet (mock: just one example)
    example_text = twitter_data.get('example', 'This is a great day for stocks!')
    sentiment = analyze_sentiment(example_text)
    score = sentiment['compound']
    # Placeholder price trend
    price_trend = 'up'
    signal = generate_signal(score, price_trend)
    print({
        'asset': symbol,
        'signal': signal,
        'confidence': abs(score),
        'duration': '1d'
    })

if __name__ == "__main__":
    main() 