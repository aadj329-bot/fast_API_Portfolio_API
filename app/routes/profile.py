from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from core.database import get_db
from app.schemas import ProfileBaseModel, ProfileCreateModel, ProfileUpdateModel, ProfileResponseModel
from app.services import profile_service

router = APIRouter(prefix="/profile", tags=["profile"])


@router.post("", response_model=ProfileResponseModel, status_code=status.HTTP_201_CREATED)
def create_profile(profile: ProfileCreateModel, db: Session = Depends(get_db)):
    """Create a new profile."""
    return profile_service.create_profile(db, profile=profile)



@router.get("/{profile_username}", response_model=ProfileResponseModel)
def get_profile_by_username(profile_username: str, db: Session = Depends(get_db)):
    """Get a profile by username."""
    return profile_service.get_profile_by_username(db, profile_username=profile_username)
  


@router.put("/{profile_username}", response_model=ProfileResponseModel)
def update_profile_by_username(profile_username: str, profile: ProfileUpdateModel, db: Session = Depends(get_db)):
    """Update a profile by username."""
    return profile_service.update_profile(db=db, profile_username=profile_username, profile=profile)
    


@router.delete("/{profile_username}")
def delete_profile_by_username(profile_username: str, db: Session = Depends(get_db)):
    """Delete a profile by username."""
    profile_service.delete_profile(db=db, profile_username=profile_username)
    return{"message": "Task deleted successfully"}