import pandas as pd

# Assuming you have loaded the scraped data
scraped_data = pd.read_csv("data/wallstreetbets_posts.csv")

# Apply the preprocess_text function to the 'title' column (or any other relevant text column)
scraped_data['cleaned_text'] = scraped_data['title'].apply(preprocess_text)

# Save the cleaned data
scraped_data.to_csv("data/cleaned_reddit_posts.csv", index=False)
