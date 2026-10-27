from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.database import get_db
from app.schemas import Profile, ProfileCreate, ProfileUpdate
from app.crud import profile_crud as crud

router = APIRouter(prefix="/profile", tags=["profile"])


@router.post("", response_model=Profile, status_code=status.HTTP_201_CREATED)
def create_profile(profile: ProfileCreate, db: Session = Depends(get_db)):
    """Create a new profile."""
    db_profile = crud.get_profile_by_username(db, profile_username=profile.username)
    if db_profile:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Profile with this username already exists"
        )
    return crud.create_profile(db=db, profile=profile)


@router.get("/{profile_username}", response_model=Profile)
def get_profile_by_username(profile_username: str, db: Session = Depends(get_db)):
    """Get a profile by username."""
    db_profile = crud.get_profile_by_username(db, profile_username=profile_username)
    if not db_profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
    return db_profile


@router.put("/{profile_username}", response_model=Profile)
def update_profile_by_username(profile_username: str, profile: ProfileUpdate, db: Session = Depends(get_db)):
    """Update a profile by username."""
    db_profile = crud.update_profile_by_username(db=db, profile_username=profile_username, profile=profile)
    if not db_profile: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
    return db_profile


@router.delete("/{profile_username}")
def delete_profile_by_username(profile_username: str, db: Session = Depends(get_db)):
    """Delete a profile by username."""
    success = crud.delete_profile_by_username(db=db, profile_username=profile_username)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
    return {"message": "Profile deleted successfully"}