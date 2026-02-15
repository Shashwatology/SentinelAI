def generate_defense_actions(risk_report):
    defense_plan = {}

    for ip, data in risk_report.items():
        actions = []

        if data["risk_level"] == "HIGH":
            actions.append(f"Block IP using firewall:")
            actions.append(f"sudo iptables -A INPUT -s {ip} -j DROP")
            actions.append("Enable fail2ban rule for SSH brute force")
            actions.append("Trigger security alert to SOC team")

        elif data["risk_level"] == "MEDIUM":
            actions.append(f"Monitor IP {ip} closely")
            actions.append("Increase logging verbosity for SSH service")

        else:
            actions.append("No immediate action required")

        defense_plan[ip] = actions

    return defense_plan
