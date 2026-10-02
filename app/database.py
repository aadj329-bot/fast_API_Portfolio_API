from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Create SQLite database file
DATABASE_URL = "sqlite:///./portfolio.db"


# Create the engine (connection to the database)
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  
)

# Create a session factory (used to interact with the database)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base class for all ORM models 
Base = declarative_base()


def create_tables():
    """Create all database tables"""
    Base.metadata.create_all(bind=engine)


def get_db():
    """
    Dependency injection function for FastAPI.
    This gives each request its own database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create all tables
def create_tables():
    Base.metadata.create_all(bind=engine)