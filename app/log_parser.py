import re
from datetime import datetime

LOG_PATTERN = re.compile(
    r'(?P<timestamp>\d{4}-\d{2}-\d{2}T[^\s]+)\s+'
    r'(?P<host>\S+)\s+'
    r'(?P<service>[^\[]+)\[(?P<pid>\d+)\]:\s+'
    r'(?P<message>.*)'
)

def parse_log_line(line: str):
    match = LOG_PATTERN.match(line)
    if not match:
        return None
    
    data = match.groupdict()
    
    return {
        "timestamp": data["timestamp"],
        "host": data["host"],
        "service": data["service"],
        "pid": int(data["pid"]),
        "message": data["message"]
    }


def parse_log_file(filepath: str):
    events = []
    with open(filepath, "r") as f:
        for line in f:
            parsed = parse_log_line(line.strip())
            if parsed:
                events.append(parsed)
    return events

from app.feature_engineering import extract_auth_features
from app.risk_engine import calculate_risk
from app.defense_engine import generate_defense_actions


if __name__ == "__main__":
    logs = parse_log_file("/var/log/auth.log")
    print(f"Parsed {len(logs)} log entries.")

    features = extract_auth_features(logs)

    risk_report = calculate_risk(features)
    defense_plan = generate_defense_actions(risk_report)

    for ip, data in risk_report.items():
        print(f"\nIP: {ip}")
        print(f"  Risk Score: {data['risk_score']}")
        print(f"  Risk Level: {data['risk_level']}")
        print(f"  Failed Attempts: {data['failed_attempts']}")
        print(f"  Successful Logins: {data['successful_logins']}")
        print(f"  Unique Users Targeted: {data['unique_users_targeted']}")

        print("  Recommended Actions:")
        for action in defense_plan[ip]:
            print(f"    - {action}")
