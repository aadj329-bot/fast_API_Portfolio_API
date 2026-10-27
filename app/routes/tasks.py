from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.database import get_db
from app.schemas import Task, TaskCreate, TaskUpdate
from app.crud import task_crud as crud


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("", response_model=Task, 
status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    """Create a new task."""
    return crud.create_task(db=db, task=task)


@router.get("", response_model=list[Task])
def tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all tasks with opional filtering."""
    return crud.get_tasks(db, skip=skip, limit=limit)


@router.get("/{task_title}", response_model=Task)
def get_task_by_title(task_title: str, db: Session = Depends(get_db)):
    """Get a task by title."""
    db_task = crud.get_task_by_title(db, task_title=task_title)
    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return db_task


@router.put("/{task_title}", response_model=Task)
def update_task(task_title: str, task: TaskUpdate, db: Session = Depends(get_db)):
    """Update a task by title."""
    db_task = crud.update_task(db=db, task_title=task_title, task=task)
    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return db_task


@router.delete("/{task_title}")
def delete_task(task_title: str, db: Session = Depends(get_db)):
    """Delete a task by title."""
    success = crud.delete_task_by_title(db=db, task_title=task_title)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return{"message": "Task deleted successfully"}