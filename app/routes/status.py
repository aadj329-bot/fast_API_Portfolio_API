from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from core.database import get_db
from app.schemas import StatusResponseModel, StatusCreateModel, StatusUpdateModel
from app.services import status_service

router = APIRouter(prefix="/status", tags=["status"])


@router.post("", response_model=StatusResponseModel, status_code=status.HTTP_201_CREATED)
def create_status(status_data: StatusCreateModel, db: Session = Depends(get_db)):
    """Create a new status entry."""
    return status_service.create_status(db=db, status=status_data)
 

@router.get("/{status_id}", response_model=StatusResponseModel)
def get_status_by_id(status_id: int, db: Session = Depends(get_db)):
    """Get a status by ID."""
    return status_service.get_status_by_id(db, status_id=status_id)
    


@router.get("/all", response_model=list[StatusResponseModel])
def get_all_statuses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all status entries with pagination."""
    return status_service.get_all_statuses(db, skip=skip, limit=limit)


@router.put("/{status_id}", response_model=StatusResponseModel)
def update_status_by_id(status_id: int, status_data: StatusUpdateModel, db: Session = Depends(get_db)):
    """Update a status entry by ID."""
    return status_service.update_status(db=db, status_id=status_id, status=status_data)
    


@router.delete("/{status_id}")
def delete_status_by_id(status_id: int, db: Session = Depends(get_db)):
    """Delete a status entry by ID."""
    status_service.delete_status(db=db, status_id=status_id)
    return {"message": "Status deleted successfully"}