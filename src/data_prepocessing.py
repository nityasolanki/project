import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import pandas as pd
import os


# Download the required resources
nltk.download('punkt')        # Tokenizer data
nltk.download('punkt_tab')
nltk.download('stopwords')    # Stopwords for text cleaning

# Create data folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')



# Function to preprocess text: clean and remove unwanted characters
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)  # Remove links
    text = re.sub(r'\@\w+|\#','', text)  # Remove @mentions and hashtags
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    tokens = word_tokenize(text)  # Tokenize the text
    filtered_words = [word for word in tokens if word not in stopwords.words('english')]  # Remove stopwords
    return " ".join(filtered_words)

# Load the scraped Reddit data
def preprocess_data(input_file, output_file):
    data = pd.read_csv(input_file)
    data['cleaned_text'] = data['title'].apply(preprocess_text)  # Apply preprocessing
    data.to_csv(output_file, index=False)  # Save cleaned data

if __name__ == "__main__":
    preprocess_data("data/reddit_posts.csv", "data/cleaned_reddit_posts.csv")

