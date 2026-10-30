from sqlalchemy.orm import Session

from app.crud import status_crud
from app.exceptions import (ResourceNotFoundError, DuplicateResourceError)


def create_status(db: Session, status):
    """Create new status"""
    existing_status = status_crud.get_status_by_id(db, status.id)

    if existing_status:
        raise DuplicateResourceError(f"Status '{status.id}' already exists")

    return status_crud.create_status(db=db, status=status)


def get_all_statuses(db: Session, skip: int, limit: int):
    """Retrieve all statuses"""
    return status_crud.get_all_statuses(db=db, skip=skip, limit=limit)


def get_status_by_id(db: Session, status_id: int):
    """Retrieve status by id"""
    status = status_crud.get_status_by_id(db=db, status_id=status_id)

    if status is None:
        raise ResourceNotFoundError(f"Status '{status_id}' not found")

    return status


def update_status(db: Session, status_id: int, status):
    """Update status by id"""
    existing_status = status_crud.get_status_by_id(db=db, status_id=status_id)

    if existing_status is None:
        raise ResourceNotFoundError(f"Status '{status_id}' not found")

    return status_crud.update_status_by_id(db=db, status_id=status_id, status=status)


def delete_status(db: Session, status_id: int):
    """Delete status by id"""
    status = status_crud.get_status_by_id(db=db, status_id=status_id)

    if status is None:
        raise ResourceNotFoundError(f"Status '{status_id}' not found")

    return status_crud.delete_status_by_id(db=db, status_id=status_id)