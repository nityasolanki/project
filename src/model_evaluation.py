from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load merged data
def load_data(file_path):
    return pd.read_csv(file_path)

# Evaluate the model
def evaluate_model(data, model):
    X = data[['sentiment', 'score', 'comments']]
    y = (data['Close'] > data['Open']).astype(int)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    y_pred = model.predict(X_test)
    
    # Print evaluation metrics
    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))

if __name__ == "__main__":
    data = load_data("data/merged_data.csv")    
    from model_training import train_model
    model = train_model(data)
    evaluate_model(data, model)
