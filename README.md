# Stock Movement Analysis Based on Social Media Sentiment

This project uses sentiment analysis of Reddit posts from subreddits like **wallstreetbets** to predict stock price movements. The system scrapes Reddit posts, analyzes sentiment, and merges the data with stock prices to predict future movements.

## Prerequisites

You need to install the following libraries:

- praw
- nltk
- pandas
- yfinance
- scikit-learn
- matplotlib

You can install them using pip:

pip install praw nltk pandas yfinance scikit-learn matplotlib

## Setup Instructions

1. Clone this repository:
https://github.com/nityasolanki/Stock-Sentiment-Analysis.git

2. Set up your Reddit API credentials by following these steps:
- Go to https://www.reddit.com/prefs/apps and create a new application to get your `client_id`, `client_secret`, and `user_agent`.
- Store your credentials in the `data_scraping.py` file.

3. Run the **data scraping** script:
python src/data_scraping.py

4. Preprocess the data:
python src/sentiment_analysis.py

5. Merge data and perform model training:
python src/feature_engineering.py python src/model_training.py

6. Run the Jupyter notebook `notebooks/data_scraping_and_analysis.ipynb` to view the analysis and predictions.


