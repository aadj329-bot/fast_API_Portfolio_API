from sqlalchemy.orm import Session
from app import models, schemas


# PROJECT CRUD OPERATIONS


def create_project(db: Session, project: schemas.ProjectCreate) -> models.Project:
    """Create a new project."""
    db_project = models.Project(**project.model_dump())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def get_project(db: Session, project_id: int) -> models.Project | None:
    """Retrieve project by ID."""
    return db.query(models.Project).filter(models.Project.id == project_id).first()


def get_project_by_name(db: Session, name: str) -> models.Project | None:
    """Retrieve project by name."""
    return db.query(models.Project).filter(models.Project.name == name).first()


def get_projects(db: Session, skip: int = 0, limit: int = 100) -> list[models.Project]:
    """Retrieve a list of projects"""
    return db.query(models.Project).offset(skip).limit(limit).all()


def update_project(db: Session, project_id: int, project: schemas.ProjectUpdate) -> models.Project | None:
    """Update a project by ID."""
    db_project = get_project(db, project_id)

    if not db_project:
        return None

    update_data = project.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(update_data, field, value)

    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def delete_project(db: Session, project_id: int) -> bool:
    """Delete a project by ID."""
    db_project = get_project(db, project_id)

    if not db_project:
        return False

    db.delete(db_project)
    db.commit()
    return True