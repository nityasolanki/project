import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize VADER SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Function to handle missing or invalid text
def analyze_sentiment(text):
    if isinstance(text, str):  # Check if the text is a string
        return sia.polarity_scores(text)['compound']  # Return compound sentiment score
    else:
        return 0.0  # Return neutral sentiment if text is invalid or NaN

# Perform sentiment analysis
def perform_sentiment_analysis(input_file, output_file):
    # Read the cleaned data
    data = pd.read_csv(input_file)

    # Ensure the cleaned_text column has no NaN or invalid entries
    data['cleaned_text'] = data['cleaned_text'].fillna("")  # Replace NaN with empty string
    
    # Apply sentiment analysis to the 'cleaned_text' column
    data['sentiment'] = data['cleaned_text'].apply(analyze_sentiment)
    
    # Save the results to a new CSV file
    data.to_csv(output_file, index=False)
    print(f"Sentiment analysis results saved to {output_file}")

if __name__ == "__main__":
    perform_sentiment_analysis("data/cleaned_reddit_posts.csv", "data/reddit_sentiment.csv")
