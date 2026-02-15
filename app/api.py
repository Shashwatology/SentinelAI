from fastapi import FastAPI, HTTPException
from pathlib import Path
import os
import logging
from datetime import datetime
from typing import List

from app.log_parser import parse_log_file
from app.feature_engineering import extract_auth_features
from app.risk_engine import calculate_risk
from app.defense_engine import generate_defense_actions
from app.anomaly_detector import detect_anomalies

from app.database import Base, engine, SessionLocal, ThreatRecord


# -------------------------------------------------
# Logging Configuration
# -------------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("sentinelai")


# -------------------------------------------------
# App Initialization
# -------------------------------------------------
app = FastAPI(
    title="SentinelAI API",
    version="1.1.0",
    description="AI-powered SSH Threat Intelligence Engine"
)


# -------------------------------------------------
# Database Initialization
# -------------------------------------------------
Base.metadata.create_all(bind=engine)


# -------------------------------------------------
# Configuration
# -------------------------------------------------
LOG_PATH = os.getenv("LOG_PATH", "sample_auth.log")


# -------------------------------------------------
# Root
# -------------------------------------------------
@app.get("/")
def root():
    return {
        "status": "running",
        "service": "SentinelAI",
        "version": "1.1.0",
        "timestamp": datetime.utcnow()
    }


# -------------------------------------------------
# Health Check
# -------------------------------------------------
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow()
    }


# -------------------------------------------------
# Analyze Logs
# -------------------------------------------------
@app.get("/analyze")
def analyze_logs():

    if not Path(LOG_PATH).exists():
        logger.error(f"Log file not found: {LOG_PATH}")
        raise HTTPException(
            status_code=500,
            detail=f"Log file not found at {LOG_PATH}"
        )

    logs = parse_log_file(LOG_PATH)

    if not logs:
        raise HTTPException(
            status_code=400,
            detail="No valid log entries found"
        )

    features = extract_auth_features(logs)
    risk_report = calculate_risk(features)
    anomaly_report = detect_anomalies(features)
    defense_plan = generate_defense_actions(risk_report)

    db = SessionLocal()
    response = []

    try:
        for ip in risk_report:

            record_data = {
                "ip": ip,
                "risk_score": risk_report[ip]["risk_score"],
                "risk_level": risk_report[ip]["risk_level"],
                "failed_attempts": risk_report[ip]["failed_attempts"],
                "successful_logins": risk_report[ip]["successful_logins"],
                "unique_users_targeted": risk_report[ip]["unique_users_targeted"],
                "anomaly_detected": anomaly_report.get(ip, {}).get("is_anomaly", False),
            }

            # Save or update record
            threat = db.query(ThreatRecord).filter(ThreatRecord.ip == ip).first()

            if threat:
                for key, value in record_data.items():
                    setattr(threat, key, value)
            else:
                threat = ThreatRecord(**record_data)
                db.add(threat)

            response.append({
                **record_data,
                "defense_actions": defense_plan.get(ip, [])
            })

        db.commit()

    except Exception as e:
        db.rollback()
        logger.error(f"Analysis failed: {e}")
        raise HTTPException(status_code=500, detail="Internal analysis error")

    finally:
        db.close()

    logger.info(f"Analyzed {len(response)} IPs successfully")

    return {
        "total_ips_analyzed": len(response),
        "analysis": response
    }


# -------------------------------------------------
# Get All Threats
# -------------------------------------------------
@app.get("/threats")
def get_all_threats():

    db = SessionLocal()
    try:
        threats = db.query(ThreatRecord).all()

        return [
            {
                "ip": t.ip,
                "risk_score": t.risk_score,
                "risk_level": t.risk_level,
                "failed_attempts": t.failed_attempts,
                "successful_logins": t.successful_logins,
                "unique_users_targeted": t.unique_users_targeted,
                "anomaly_detected": t.anomaly_detected
            }
            for t in threats
        ]

    finally:
        db.close()


# -------------------------------------------------
# Get Single Threat
# -------------------------------------------------
@app.get("/threats/{ip}")
def get_threat(ip: str):

    db = SessionLocal()
    try:
        threat = db.query(ThreatRecord).filter(ThreatRecord.ip == ip).first()

        if not threat:
            raise HTTPException(status_code=404, detail="IP not found")

        return {
            "ip": threat.ip,
            "risk_score": threat.risk_score,
            "risk_level": threat.risk_level,
            "failed_attempts": threat.failed_attempts,
            "successful_logins": threat.successful_logins,
            "unique_users_targeted": threat.unique_users_targeted,
            "anomaly_detected": threat.anomaly_detected
        }

    finally:
        db.close()


# -------------------------------------------------
# Executive Dashboard Summary
# -------------------------------------------------
@app.get("/dashboard-summary")
def dashboard_summary():

    db = SessionLocal()
    try:
        threats = db.query(ThreatRecord).all()

        return {
            "total_ips": len(threats),
            "high_risk": sum(1 for t in threats if t.risk_level == "HIGH"),
            "medium_risk": sum(1 for t in threats if t.risk_level == "MEDIUM"),
            "low_risk": sum(1 for t in threats if t.risk_level == "LOW"),
            "anomalies_detected": sum(1 for t in threats if t.anomaly_detected)
        }

    finally:
        db.close()
