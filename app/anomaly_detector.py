from sklearn.ensemble import IsolationForest
import numpy as np

def detect_anomalies(ip_activity):
    feature_matrix = []
    ip_list = []

    for ip, data in ip_activity.items():
        failed = data["failed_attempts"]
        success = data["successful_logins"]
        unique_users = data.get("unique_users_targeted", 0)


        feature_matrix.append([failed, success, unique_users])
        ip_list.append(ip)

    if not feature_matrix:
        return {}

    X = np.array(feature_matrix)

    model = IsolationForest(contamination=0.2, random_state=42)
    model.fit(X)

    predictions = model.predict(X)

    anomaly_report = {}

    for i, ip in enumerate(ip_list):
        anomaly_report[ip] = {
            "features": feature_matrix[i],
            "is_anomaly": True if predictions[i] == -1 else False
        }

    return anomaly_report
