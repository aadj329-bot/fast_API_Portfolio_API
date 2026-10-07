from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.database import get_db
from app.schemas import Profile, ProfileCreate, ProfileUpdate
from app.crud import profile_crud as crud

router = APIRouter(prefix="/profile", tags=["profile"])


@router.post("", response_model=Profile, status_code=status.HTTP_201_CREATED)
def create_profile(profile: ProfileCreate, db: Session = Depends(get_db)):
    """Create a new profile."""
    db_profile = crud.get_profile(db, username=profile.username)
    if db_profile:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Profile with this username already exists"
        )
    return crud.create_profile(db=db, profile=profile)


@router.get("", response_model=Profile)
def get_profile(db: Session = Depends(get_db)):
    """Get the first profile (current user profile)."""
    db_profile = crud.get_profile(db)
    if not db_profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found. Create one first."
        )
    return db_profile


@router.get("/{profile_id}", response_model=Profile)
def get_profile_by_id(profile_id: int, db: Session = Depends(get_db)):
    """Get a profile by ID."""
    db_profile = crud.get_profile_by_id(db, profile_id=profile_id)
    if not db_profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
    return db_profile


@router.put("/{profile_id}", response_model=Profile)
def update_profile(profile_id: int, profile: ProfileUpdate, db: Session = Depends(get_db)):
    """Update a profile by ID."""
    db_profile = crud.update_profile(db=db, profile_id=profile_id, profile=profile)
    if not db_profile: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
    return db_profile


@router.delete("/{profile_id}")
def delete_profile(profile_id: int, db: Session = Depends(get_db)):
    """Delete a profile by ID."""
    success = crud.delete_profile(db=db, profile_id=profile_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
    return {"message": "Profile deleted successfully"}