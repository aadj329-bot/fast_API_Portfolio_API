from sqlalchemy.orm import Session
from fastapi import status

from app.models import profile_model as models
from core.database import get_db
from app.schemas import ProfileCreateModel, ProfileUpdateModel 


# PROFILE CRUD OPERATIONS


def create_profile(db: Session, profile: ProfileCreateModel) -> models.Profile:
    """Create a new profile."""
    db_profile = models.Profile(**profile.model_dump(mode="json"))
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile


def get_profile_by_username(db: Session, profile_username: str) -> models.Profile | None:
    """Retrieve profile by username."""
    return db.query(models.Profile).filter(models.Profile.username == profile_username).first()



def update_profile_by_username(db: Session, profile_username: str, profile: ProfileUpdateModel) -> models.Profile | None:
    """Update profile by username."""
    db_profile = get_profile_by_username(db, profile_username)
    
    if db_profile is None:
        return False
    
    update_data = profile.model_dump(exclude_unset=True, mode='json')
    for field, value in update_data.items():
        setattr(db_profile, field, value)

    db.commit()
    db.refresh(db_profile)
    return db_profile


def delete_profile_by_username(db: Session, profile_username: str) -> bool:
    """Delete profile by username."""
    db_profile = get_profile_by_username(db, profile_username)
    
    if db_profile is None:
        return False
    
    db.delete(db_profile)
    db.commit()
    return True