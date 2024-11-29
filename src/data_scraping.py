import praw
import pandas as pd

# Reddit API initialization
def init_reddit():
    reddit = praw.Reddit(
        client_id="qxZ-XdAx-8NEroCUW-SU1Q",
        client_secret="x4ibqgGedEUoEHaZaNeAoONz66X5xA", 
        user_agent="stock_sentiment_analysis"
    )
    return reddit

# Scrape data from a specific subreddit
def scrape_reddit(subreddit_name, limit=100):
    reddit = init_reddit()
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    for post in subreddit.hot(limit=limit):
        posts.append({
            'title': post.title,
            'selftext': post.selftext,
            'score': post.score,
            'comments': post.num_comments,
            'created_utc': post.created_utc
        })
    return pd.DataFrame(posts)

# Save the scraped data into a CSV file
def save_scraped_data(subreddit_name, limit=100):
    data = scrape_reddit(subreddit_name, limit)
    data.to_csv(f"data/reddit_posts.csv", index=False)

if __name__ == "__main__":
    save_scraped_data("wallstreetbets", 500)



