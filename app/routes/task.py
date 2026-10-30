from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from core.database import get_db
from app.schemas import TaskResponseModel, TaskCreateModel, TaskUpdateModel
from app.services import task_service


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("", response_model=TaskResponseModel, 
status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreateModel, db: Session = Depends(get_db)):
    """Create a new task."""
    return task_service.create_task(db=db, task=task)


@router.get("", response_model=list[TaskResponseModel])
def tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)): 
    """Get all tasks with opional filtering."""
    return task_service.get_tasks(db=db, skip=skip, limit=limit)


@router.get("/{task_title}", response_model=TaskResponseModel)
def get_task_by_title(task_title: str, db: Session = Depends(get_db)):
    """Get a task by title."""
    return task_service.get_task_by_title(db, task_title=task_title)
    
    
@router.put("/{task_title}", response_model=TaskResponseModel)
def update_task_by_title(task_title: str, task: TaskUpdateModel, db: Session = Depends(get_db)):
    """Update a task by title."""
    return task_service.update_task(db=db, task_title=task_title, task=task)
    

@router.delete("/{task_title}")
def delete_task(task_title: str, db: Session = Depends(get_db)):
    """Delete a task by title."""
    task_service.delete_task(db=db, task_title=task_title)
    return{"message": "Task deleted successfully"}