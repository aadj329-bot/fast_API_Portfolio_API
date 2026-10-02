from sqlalchemy.orm import Session
from app.models import profile_model as models
from core.database import get_db
from app import schemas


# PROFILE CRUD OPERATIONS


def create_profile(db: Session, profile: schemas.ProfileCreate) -> models.Profile:
    """Create a new profile."""
    db_profile = models.Profile(**profile.model_dump())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile


def get_profile(db: Session, username: str) -> models.Profile | None:
    """Retrieve profile by username."""
    return db.query(models.Profile).filter(models.Profile.username == username).first()


def get_profile_by_id(db: Session, profile_id: int) -> models.Profile | None:
    """Retrieve profile by ID."""
    return db.query(models.Profile).filter(models.Profile.id == profile_id).first()


def update_profile(db: Session, profile_id: int, profile: schemas.ProfileUpdate) -> models.Profile | None:
    """Update profile by ID."""
    db_profile = get_profile_by_id(db, profile_id)
    if not db_profile:
        return None

    update_data = profile.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_profile, field, value)

    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile


def delete_profile(db: Session, profile_id: int) -> bool:
    db_profile = get_profile_by_id(db, profile_id)
    if not db_profile:
        return False

    db.delete(db_profile)
    db.commit()
    return True