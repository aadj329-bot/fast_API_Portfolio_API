from sqlalchemy.orm import Session

from app.models.task_model import Task
from app.schemas import TaskCreateModel, TaskUpdateModel


def create_task(db: Session, task: TaskCreateModel) -> Task:
    """Create a new task."""
    db_task = Task(**task.model_dump(mode='json'))
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_tasks(db: Session, skip: int = 0, limit: int = 100) -> list[Task]:
    """Get all task."""
    return db.query(Task).offset(skip).limit(limit).all()


def get_task_by_title(db: Session, task_title: str):
    """Get a task by title."""
    return db.query(Task).filter(Task.title == task_title).first()


def update_task_by_title(db: Session, task_title: str, task_update: TaskUpdateModel) -> Task | None:
    """Update a task by title."""
    db_session = get_task_by_title(db, task_title)
    
    if db_session is None:
        return None

    update_data = task_update.model_dump(exclude_unset=True, mode='json')
    
    for key, value in update_data.items():
        setattr(db_session, key, value)
     
    db.commit()
    db.refresh(db_session)
    return db_session


def delete_task_by_title(db: Session, task_title: str) -> bool:
    """Delete a task by title."""
    db_task = get_task_by_title(db, task_title)

    if db_task is None:
        return False
    
    db.delete(db_task)
    db.commit()
    return True