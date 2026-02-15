def calculate_risk(ip_activity):
    risk_report = {}

    for ip, data in ip_activity.items():
        failed = data["failed_attempts"]
        success = data["successful_logins"]
        unique_users = data.get("unique_users_targeted", 0)

        risk_score = (failed * 2) + (unique_users * 3) - (success * 2)

        if risk_score >= 10:
            level = "HIGH"
        elif risk_score >= 5:
            level = "MEDIUM"
        else:
            level = "LOW"

        risk_report[ip] = {
            "risk_score": risk_score,
            "risk_level": level,
            "failed_attempts": failed,
            "successful_logins": success,
            "unique_users_targeted": unique_users
        }

    return risk_report
