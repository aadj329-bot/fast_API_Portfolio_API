from sqlalchemy.orm import Session

from app.crud import project_crud
from app.exceptions import DuplicateResourceError, ResourceNotFoundError


def create_project(db: Session, project):
    """Create new project"""
    existing_project = project_crud.get_project_by_name(db=db, project_name=project.name)

    # Project name duplicate error
    if existing_project:
        raise DuplicateResourceError(f"Project '{project.name}' already exist")

    return project_crud.create_project(db=db, project=project)


def get_projects(db: Session, skip: int, limit: int):
    """Retrieve all projects"""
    return project_crud.get_projects(db=db, skip=skip, limit=limit)


def get_project_by_name(db: Session, project_name: str):
    """Retrieve project by name"""
    project = project_crud.get_project_by_name(db=db, project_name=project_name)

    # Project name not found error
    if project is None:
        raise ResourceNotFoundError(f"Project '{project_name}' not found")

    return project 


def update_project(db: Session, project_name: str, project):
    """Update project by name"""
    existing_project = project_crud.get_project_by_name(db=db, project_name=project_name)

    # Project name not found error
    if existing_project is None:
        raise ResourceNotFoundError(f"Project '{project_name}' not found")

    # Project name duplicate attempt error
    if project.name:
        duplicate_name = project_crud.get_project_by_name(db=db, project_name=project.name)

        if (duplicate_name and duplicate_name.id != existing_project.id):
            raise DuplicateResourceError(f"Project '{project.name}' already exists")

    return project_crud.update_project_by_name(db=db, project_name=project_name, project=project)


def delete_project(db: Session, project_name: str):
    """Delete project by name"""
    project = project_crud.get_project_by_name(db=db, project_name=project_name)

    # Project name not found error
    if project is None:
        raise ResourceNotFoundError(f"Project '{project_name}' not found")

    return project_crud.delete_project_by_name(db=db, project_name=project_name)
