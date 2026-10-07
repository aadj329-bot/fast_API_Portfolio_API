from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session, sessionmaker
from typing import Generator
import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv


# Create the database model base class
Base = declarative_base()


# Database configuration - using environment variables
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

if not SQLALCHEMY_DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is not set")


# Create the engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    future=True,
)


def create_tables():
    """Create all database tables"""
    Base.metadata.create_all(bind=engine)


# Configure the sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, None, None]:
    """Dependency function to get database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()