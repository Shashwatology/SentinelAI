from sqlalchemy import create_engine, Column, String, Integer, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./sentinel.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class ThreatRecord(Base):
    __tablename__ = "threats"

    ip = Column(String, primary_key=True, index=True)
    risk_score = Column(Integer)
    risk_level = Column(String)
    failed_attempts = Column(Integer)
    successful_logins = Column(Integer)
    unique_users_targeted = Column(Integer)
    anomaly_detected = Column(Boolean)
