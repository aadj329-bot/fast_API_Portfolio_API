from sqlalchemy.orm import Session

from app.crud import profile_crud
from app.exceptions import DuplicateResourceError, ResourceNotFoundError


def create_profile(db: Session, profile):
    """Create a new profile"""
    existing_profile = profile_crud.get_profile_by_username(db, profile.username)

    # Duplicate username error
    if existing_profile:
        raise DuplicateResourceError(f"Profile '{profile.username}' already exists")

    return profile_crud.create_profile(db=db, profile=profile)


def get_profile_by_username(db: Session, profile_username: str):
    """Retrieve profile by username"""
    profile = profile_crud.get_profile_by_username(db=db, profile_username=profile_username)

    # Profile not found error
    if profile is None:
        raise ResourceNotFoundError(f"Profile '{profile_username}' not found")

    return profile


def update_profile(db: Session, profile_username: str, profile):
    """Update profile by username"""
    existing_profile = profile_crud.get_profile_by_username(db=db, profile_username=profile_username)

    # Username not found error
    if existing_profile is None: 
        raise ResourceNotFoundError(f"Profile '{profile_username}' not found")

    # Duplicate username attempt error
    if profile.username:
        duplicate_username = profile_crud.get_profile_by_username(db=db, profile_username=profile.username)

        if (duplicate_username and duplicate_username.id != existing_profile.id):
            raise DuplicateResourceError(f"Profile '{profile.username}' already exists")


    return profile_crud.update_profile_by_username(db=db, profile_username=profile_username, profile=profile)


def delete_profile(db: Session, profile_username: str):
    """Delete profile by username"""
    profile = profile_crud.get_profile_by_username(db=db, profile_username=profile_username)

    # Username not found error
    if profile is None:
        raise ResourceNotFoundError(f"Profile '{profile_username}' not found")

    return profile_crud.delete_profile_by_username(db=db, profile_username=profile_username)