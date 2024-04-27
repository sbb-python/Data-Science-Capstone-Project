import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Sample news article text (replace with actual news articles)
news_articles = [
    "Superior Drilling Products announced strong earnings growth.",
    "The company faces challenges due to declining demand in the oil industry.",
    "Investors are optimistic about SDPI's new product launch.",
]

# Initialize the VADER sentiment analyzer
nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()

# Perform sentiment analysis on each news article
sentiment_scores = []
for article in news_articles:
    sentiment = sid.polarity_scores(article)
    sentiment_scores.append(sentiment)

# Print sentiment scores
for i, score in enumerate(sentiment_scores):
    print(f"News Article {i+1} Sentiment Score: {score}")
