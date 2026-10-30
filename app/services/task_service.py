from sqlalchemy.orm import Session

from app.crud import task_crud
from app.exceptions import (ResourceNotFoundError, DuplicateResourceError)


def create_task(db: Session, task):
    """Create new task"""
    existing_task = task_crud.get_task_by_title(db, task.title)

    if existing_task:
        raise DuplicateResourceError(f"Task '{task.title}' already exists")

    return task_crud.create_task(db=db, task=task)


def get_tasks(db: Session, skip: int, limit: int):
    """Retrieve all tasks"""
    return task_crud.get_tasks(db=db, skip=skip, limit=limit)


def get_task_by_title(db: Session, task_title: str):
    """Retrieve task by title"""
    task = task_crud.get_task_by_title(db=db, task_title=task_title)

    if task is None:
        raise ResourceNotFoundError(f"Task '{task_title}' not found")

    return task


def update_task(db: Session, task_title: str, task):
    """Update task by title"""
    existing_task = task_crud.get_task_by_title(db=db, task_title=task_title)

    if existing_task is None:
        raise ResourceNotFoundError(f"Task '{task_title}' not found")

    return task_crud.update_task_by_title(db=db, task_title=task_title, task_update=task)


def delete_task(db: Session, task_title: str):
    """Delete task by title"""
    task = task_crud.get_task_by_title(db=db, task_title=task_title)

    if task is None:
        raise ResourceNotFoundError(f"Task '{task_title}' not found")

    return task_crud.delete_task_by_title(db=db, task_title=task_title)