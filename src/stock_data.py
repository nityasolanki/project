import yfinance as yf
import pandas as pd

# Function to get stock data
def get_stock_data(ticker, period="1y"):
    stock = yf.Ticker(ticker)
    stock_data = stock.history(period=period)
    stock_data.to_csv(f"data/{ticker}_stock_data.csv")

if __name__ == "__main__":
    get_stock_data("AAPL", "1y")
