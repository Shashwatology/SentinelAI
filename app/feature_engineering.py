import re
from collections import defaultdict
from datetime import datetime

FAILED_LOGIN_PATTERN = re.compile(
    r"Failed password for (invalid user )?(?P<user>\w+) from (?P<ip>\d+\.\d+\.\d+\.\d+)"
)

SUCCESS_LOGIN_PATTERN = re.compile(
    r"Accepted password for (?P<user>\w+) from (?P<ip>\d+\.\d+\.\d+\.\d+)"
)

def extract_auth_features(events):
    ip_activity = defaultdict(lambda: {
        "failed_attempts": 0,
        "successful_logins": 0,
        "users_targeted": set()
    })

    for event in events:
        message = event["message"]

        failed_match = FAILED_LOGIN_PATTERN.search(message)
        success_match = SUCCESS_LOGIN_PATTERN.search(message)

        if failed_match:
            ip = failed_match.group("ip")
            user = failed_match.group("user")

            ip_activity[ip]["failed_attempts"] += 1
            ip_activity[ip]["users_targeted"].add(user)

        elif success_match:
            ip = success_match.group("ip")
            user = success_match.group("user")

            ip_activity[ip]["successful_logins"] += 1
            ip_activity[ip]["users_targeted"].add(user)

    # Convert set → count
    processed_activity = {}

    for ip, data in ip_activity.items():
        processed_activity[ip] = {
            "failed_attempts": data["failed_attempts"],
            "successful_logins": data["successful_logins"],
            "unique_users_targeted": len(data["users_targeted"])
        }

    return processed_activity
