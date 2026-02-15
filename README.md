# **🛡 SentinelAI — Adaptive SSH Threat Intelligence Platform**

SentinelAI is an AI-powered security intelligence engine designed to analyze SSH authentication logs, detect suspicious behavior patterns, compute dynamic risk scores, identify anomalies using machine learning, and recommend defensive actions.

It bridges the gap between raw log data and actionable cybersecurity intelligence.

---

## **🚀 Live Deployment**

🔗 Live API: https://sentinelai-dxqo.onrender.com  
📘 API Docs: https://sentinelai-dxqo.onrender.com/docs

---

## **🎯 Problem Statement**

Most servers generate authentication logs continuously.

However:

* Logs are rarely analyzed behaviorally  
* Brute-force patterns go unnoticed  
* Multi-user targeting is ignored  
* Small teams cannot afford heavy SIEM tools

SentinelAI provides:

A lightweight, deployable intelligence layer for authentication threat detection.

---

## **🧠 What SentinelAI Does**

• Parses SSH authentication logs  
• Extracts behavioral security features  
• Detects failed login spikes  
• Identifies multi-account targeting  
• Calculates dynamic risk scores  
• Performs anomaly detection (Isolation Forest)  
• Recommends defensive actions  
• Stores persistent threat intelligence  
• Provides executive dashboard metrics

---

## **🏗 System Architecture**

               `┌────────────────────┐`  
                `│   SSH Auth Logs    │`  
                `└─────────┬──────────┘`  
                          `│`  
                          `▼`  
                `┌────────────────────┐`  
                `│   Log Parser       │`  
                `└─────────┬──────────┘`  
                          `│`  
                          `▼`  
                `┌────────────────────┐`  
                `│ Feature Extraction │`  
                `└─────────┬──────────┘`  
                          `│`  
                          `▼`  
                `┌────────────────────┐`  
                `│ Risk Engine        │`  
                `└─────────┬──────────┘`  
                          `│`  
                          `▼`  
                `┌────────────────────┐`  
                `│ Anomaly Detector   │`  
                `└─────────┬──────────┘`  
                          `│`  
                          `▼`  
                `┌────────────────────┐`  
                `│ Defense Engine     │`  
                `└─────────┬──────────┘`  
                          `│`  
                          `▼`  
                `┌────────────────────┐`  
                `│ Threat Database    │`  
                `└─────────┬──────────┘`  
                          `│`  
                          `▼`  
                `┌────────────────────┐`  
                `│ API + Dashboard    │`  
                `└────────────────────┘`

---

## **📂 Project Structure**

`sentinelAI/`  
`│`  
`├── app/`  
`│   ├── api.py`  
`│   ├── log_parser.py`  
`│   ├── feature_engineering.py`  
`│   ├── risk_engine.py`  
`│   ├── anomaly_detector.py`  
`│   ├── defense_engine.py`  
`│   ├── database.py`  
`│`  
`├── frontend/`  
`│   ├── index.html`  
`│   ├── style.css`  
`│   ├── script.js`  
`│`  
`├── Dockerfile`  
`├── requirements.txt`  
`├── sample_auth.log`  
`└── README.md`

---

## **🔬 Feature Engineering**

From each authentication event, SentinelAI extracts:

* Failed login attempts per IP  
* Successful logins per IP  
* Number of unique users targeted  
* Behavioral frequency patterns

These features are aggregated into a structured threat profile per IP address.

---

## **🧮 Risk Scoring Formula**

SentinelAI computes a dynamic risk score using weighted behavioral signals:

Risk Score \=  
(2 × Failed Attempts)

* (3 × Unique Users Targeted)  
  − (1 × Successful Logins)

Risk Level Classification:

* HIGH → Risk Score ≥ 10  
* MEDIUM → 5 ≤ Risk Score \< 10  
* LOW → Risk Score \< 5

This scoring system prioritizes brute-force intensity and multi-user targeting behavior.

---

## **🤖 Anomaly Detection (Machine Learning)**

SentinelAI uses:

Isolation Forest (Scikit-learn)

Model Input Features:

* Failed attempts  
* Successful logins  
* Unique users targeted

The model identifies statistically abnormal behavior patterns compared to typical authentication activity.

An anomaly flag is added if the IP deviates significantly from baseline behavior.

---

## **🛡 Defense Engine**

Based on risk score and anomaly detection:

SentinelAI recommends:

• Temporary IP blocking  
• Rate limiting  
• Account lockout  
• Monitoring escalation

This bridges AI intelligence with actionable security response.

---

## **💾 Database Layer**

SQLite is used for:

* Persistent threat storage  
* Historical risk analysis  
* Executive summary metrics  
* Dashboard aggregation

Each IP threat record includes:

* Risk score  
* Risk level  
* Attempt counts  
* Anomaly flag

---

## **🌍 Production Deployment**

SentinelAI is:

* Dockerized  
* Cloud deployed (Render)  
* API-documented (Swagger)  
* Environment-configurable  
* Modular and extensible

---

## **📊 Executive Dashboard**

The dashboard provides:

* Total IP threats  
* High/Medium/Low distribution  
* Anomaly count  
* Threat detail table  
* Auto-refresh monitoring

---

## **🔐 Major Use Cases**

• Small startups lacking SIEM infrastructure  
• DevOps teams monitoring SSH exposure  
• Cloud servers vulnerable to brute-force  
• Early-stage security automation pipelines  
• Lightweight threat scoring microservices

---

## **💰 Monetization Potential**

SentinelAI can evolve into:

* Security SaaS for startups  
* DevSecOps plugin  
* API-based threat scoring service  
* Managed log intelligence layer  
* Multi-tenant threat analytics platform

---

## **🔮 Future Roadmap**

• Real-time log streaming ingestion  
• Firewall auto-block integration  
• GeoIP threat enrichment  
• Multi-tenant SaaS architecture  
• Historical risk trend modeling  
• Alert notification system  
• Enterprise dashboard UI

---

## **🧠 Why SentinelAI Matters**

Security tools are often heavy and expensive.

SentinelAI demonstrates how AI \+ behavioral modeling can:

Transform raw logs into intelligence.

It is a step toward accessible, deployable, intelligent security systems.

---

# **⭐ Built By**

Shashwat Upadhyay  
AI & Cybersecurity Engineer

