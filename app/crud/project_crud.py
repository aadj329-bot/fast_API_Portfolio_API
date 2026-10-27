from sqlalchemy.orm import Session

from app.models import project_model as models
from app.schemas import ProjectCreate, ProjectUpdate


# PROJECT CRUD OPERATIONS


def create_project(db: Session, project: ProjectCreate) -> models.Project:
    """Create a new project."""
    db_project = models.Project(**project.model_dump(mode="json"))
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def get_project_by_name(db: Session, project_name: str) -> models.Project | None:
    """Retrieve project by ID."""
    return db.query(models.Project).filter(models.Project.name == project_name).first()


def get_projects(db: Session, skip: int = 0, limit: int = 100) -> list[models.Project]:
    """Retrieve a list of projects"""
    return db.query(models.Project).offset(skip).limit(limit).all()


def update_project(db: Session, project_name: str, project: ProjectUpdate) -> models.Project | None:
    """Update a project by ID."""
    db_project = get_project_by_name(db, project_name)

    if db_project is None:
        return None

    update_data = project.model_dump(exclude_unset=True, mode='json')

    for field, value in update_data.items():
        setattr(db_project, field, value)

    db.commit()
    db.refresh(db_project)
    return db_project


def delete_project(db: Session, project_name: str) -> bool:
    """Delete a project by ID."""
    db_project = get_project_by_name(db, project_name)

    if db_project is None:
        return False

    db.delete(db_project)
    db.commit()
    return True