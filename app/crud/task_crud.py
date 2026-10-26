from sqlalchemy.orm import Session

from app.models import task_model as task
from app.schemas import TaskCreate, TaskUpdate


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    """Get all task with optional filtering."""
    return db.query(task).offset(skip).limit(limit).all()


def get_task(db: Session, task_id: int):
    """Get a task by ID."""
    return db.query(task).filter(task.id == task_id).first()


def create_task(db: Session, task: TaskCreate):
    """Create a new task."""
    db_task = task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(db: Session, task_id: int, task: TaskUpdate):
    """Update a task by ID."""
    db_task = get_task(db, task_id: int)
    
    if db_task is None:
        return None

    update_data = task.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int):
    """Delete a task by ID."""
    db_task = get_task(db, task_id)

    if db_task is None:
        return False
    
    db.delete(db_task)
    db.commit()
    return True