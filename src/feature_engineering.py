import pandas as pd

# Function to merge sentiment and stock data
def merge_data(sentiment_file, stock_file, output_file):
    # Load sentiment data (Reddit data with sentiment)
    sentiment_data = pd.read_csv(sentiment_file)
    print(f"Sentiment Data Columns: {sentiment_data.columns}")  # Debug: Check column names
    
    # Load stock data (AAPL stock data)
    stock_data = pd.read_csv(stock_file)
    print(f"Stock Data Columns: {stock_data.columns}")  # Debug: Check column names

    # Check if 'Date' column exists in stock data
    if 'Date' not in stock_data.columns:
        print("Error: 'Date' column not found in stock data.")
        return

    # Check if sentiment data has a 'date' or 'created_utc' column for matching
    if 'date' not in sentiment_data.columns and 'created_utc' not in sentiment_data.columns:
        print("Error: 'date' or 'created_utc' column not found in sentiment data.")
        return

    # Convert 'Date' column to datetime with utc=True to avoid time zone issues in stock data
    stock_data['Date'] = pd.to_datetime(stock_data['Date'], utc=True)
    
    # Extract the date part (only date, without time) in stock data
    stock_data['date'] = stock_data['Date'].dt.date

    # Check the first few rows of sentiment data to see date format
    print("First few rows of sentiment data:", sentiment_data.head())

    # If 'created_utc' exists, convert it to datetime
    if 'created_utc' in sentiment_data.columns:
        sentiment_data['date'] = pd.to_datetime(sentiment_data['created_utc'], unit='s').dt.date

    # Check if 'date' column is now present in both dataframes
    print(f"Sentiment Data Columns After Preprocessing: {sentiment_data.columns}")
    print(f"Stock Data Columns After Preprocessing: {stock_data.columns}")
    
    # Merge the stock data with sentiment data (assuming the 'date' column exists in both)
    merged_data = pd.merge(sentiment_data, stock_data, left_on='date', right_on='date', how='inner')

    # Save the merged data to a new CSV file
    merged_data.to_csv(output_file, index=False)
    print(f"Merged data saved to {output_file}")

# Example usage
if __name__ == "__main__":
    merge_data("data/reddit_sentiment.csv", "data/AAPL_stock_data.csv", "data/merged_data.csv")

