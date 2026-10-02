from sqlalchemy import Column, DateTime, Integer, JSON, String
from sqlalchemy.sql import func

from core.database import Base


class Profile(Base):
    """Database model for user profile."""
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=False)
    bio = Column(String, nullable=False)
    location = Column(String, nullable=False)
    github_url = Column(String, nullable=False)
    primary_language = Column(JSON, nullable=False)
    secondary_language = Column(JSON, nullable=False)
    current_focus = Column(String, nullable=False)
    learning_path = Column(String, nullable=False)
    projects_count = Column(Integer, nullable=False)
    
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)