from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.database import get_db
from app.schemas import StatusResponse, StatusCreate
from app.crud import status_crud as crud

router = APIRouter(prefix="/status", tags=["status"])


@router.post("", response_model=StatusResponse, status_code=status.HTTP_201_CREATED)
def create_status(status_data: StatusCreate, db: Session = Depends(get_db)):
    """Create a new status entry."""
    return crud.create_status(db=db, status=status_data)


@router.get("", response_model=StatusResponse)
def get_status(db: Session = Depends(get_db)):
    """Get the current status (most recent entry)."""
    db_status = crud.get_current_status(db)
    if not db_status:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Status not found. Create one first."
        )
    return db_status


@router.get("/{status_id}", response_model=StatusResponse)
def get_status_by_id(status_id: int, db: Session = Depends(get_db)):
    """Get a status by ID."""
    db_status = crud.get_status(db, status_id=status_id)
    if not db_status:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Status not found"
        )
    return db_status


@router.get("/all", response_model=list[StatusResponse])
def get_all_statuses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all status entries with pagination."""
    return crud.get_statuses(db, skip=skip, limit=limit)


@router.put("/{status_id}", response_model=StatusResponse)
def update_status(status_id: int, status_data: StatusCreate, db: Session = Depends(get_db)):
    """Update a status entry by ID."""
    db_status = crud.update_status(db=db, status_id=status_id, status=status_data)
    if not db_status:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Status not found"
        )
    return db_status


@router.delete("/{status_id}")
def delete_status(status_id: int, db: Session = Depends(get_db)):
    """Delete a status entry by ID."""
    success = crud.delete_status(db=db, status_id=status_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Status not found"
        )
    return {"message": "Status deleted successfully"}