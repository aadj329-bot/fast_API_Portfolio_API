from sqlalchemy import Column, Integer, DateTime, JSON, String
from sqlalchemy.sql import func

from app.database import Base


class Project(Base):
    """Database model for portfolio projects."""
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=False)
    language = Column(String, nullable=False)
    url = Column(String, nullable=False)
    visibility = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)