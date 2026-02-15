import joblib
import pandas as pd
from sklearn.ensemble import IsolationForest
from app.feature_engineering import extract_auth_features
from app.log_parser import parse_log_file

LOG_PATH = "sample_auth.log"
MODEL_PATH = "sentinel_model.pkl"

def train_model():
    logs = parse_log_file(LOG_PATH)
    features = extract_auth_features(logs)

    df = pd.DataFrame.from_dict(features, orient="index")

    model = IsolationForest(contamination=0.2, random_state=42)
    model.fit(df)

    joblib.dump(model, MODEL_PATH)
    print("Model trained and saved.")

if __name__ == "__main__":
    train_model()
