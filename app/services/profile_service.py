from sqlalchemy.orm import Session

from app.crud import profile_crud
from app.exceptions import (ResourceNotFoundError, DuplicateResourceError)


def create_profile(db: Session, profile):
    existing_profile = profile_crud.get_profile_by_username(db, profile.username)

    if existing_profile:
        raise DuplicateResourceError(f"Profile '{profile.username}' already exists")

    return profile_crud.create_profile(db=db, profile=profile)


def get_profile_by_username(db: Session, profile_username: str):
    profile = profile_crud.get_profile_by_username(db=db, profile_username=profile_username)

    if profile is None:
        raise ResourceNotFoundError(f"Profile '{profile_username}' not found")

    return profile


def update_profile(db: Session, profile_username: str, profile):
    existing_profile = profile_crud.get_profile_by_username(db=db, profile_username=profile_username)

    if existing_profile is None: 
        raise ResourceNotFoundError(f"Profile '{profile_username}' not found")

    return profile_crud.update_profile_by_username(db=db, profile_username=profile_username, profile=profile)


def delete_profile(db: Session, profile_username: str):
    profile = profile_crud.get_profile_by_username(db=db, profile_username=profile_username)

    if profile is None:
        raise ResourceNotFoundError(f"Profile '{profile_username}' not found")

    return profile_crud.delete_profile_by_username(db=db, profile_username=profile_username)