"""
Module for sentiment analysis using VADER or other models.
"""
try:
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    VADER_AVAILABLE = True
except ImportError:
    VADER_AVAILABLE = False
    print("Warning: vaderSentiment not installed. Using fallback sentiment analysis.")

def analyze_sentiment(text):
    """Return sentiment score for the given text using VADER or fallback method."""
    if VADER_AVAILABLE:
        analyzer = SentimentIntensityAnalyzer()
        return analyzer.polarity_scores(text)
    else:
        # Fallback simple sentiment analysis
        positive_words = ['good', 'great', 'excellent', 'amazing', 'bullish', 'up', 'rise', 'gain']
        negative_words = ['bad', 'terrible', 'awful', 'bearish', 'down', 'fall', 'drop', 'crash']
        
        text_lower = text.lower()
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        
        if positive_count > negative_count:
            compound = 0.5
        elif negative_count > positive_count:
            compound = -0.5
        else:
            compound = 0.0
            
        return {
            'neg': 0.0 if compound >= 0 else abs(compound),
            'neu': 1.0 - abs(compound),
            'pos': 0.0 if compound <= 0 else compound,
            'compound': compound
        } 