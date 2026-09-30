from sqlalchemy import Column, DateTime, Integer, JSON, String
from sqlalchemy.sql import func

from app.database import Base


class Status(Base):
    """Database model for status."""
    __tablename__ = "statuses"

    id = Column(Integer, primary_key=True, index=True)
    current_projects = Column(String, nullable=False)
    learning = Column(String, nullable=False)
    goals = Column(JSON, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
