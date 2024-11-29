import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load merged data
def load_data(file_path):
    return pd.read_csv(file_path)

# Train a Random Forest model
def train_model(data):
    X = data[['sentiment', 'score', 'comments']]  # Features
    y = (data['Close'] > data['Open']).astype(int)  # Label: 1 if price increased, else 0

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    clf = RandomForestClassifier(random_state=42)
    clf.fit(X_train, y_train)

    # Evaluate the model
    accuracy = clf.score(X_test, y_test)
    print(f"Model Accuracy: {accuracy:.2f}")
    return clf

if __name__ == "__main__":
    data = load_data("data/merged_data.csv")
    model = train_model(data)
