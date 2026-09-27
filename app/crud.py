"""CRUD functions for database operations. 

This module contains functions to Create, Read, Update and Delete records from the database. Each function takes a database session and 
the data needed, and returns the created/updated model or None if not found.
"""

from sqlalchemy.orm import Session
from app import models, schemas
  

# PROFILE CRUD OPERATIONS


def create_profile(db: Session, profile: schemas.ProfileCreate) -> models.Profile:
    db_profile = models.Profile(**profile.model_dump())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile


def get_profile(db: Session, username: str) -> models.Profile | None:
    return db.query(models.Profile).filter(models.Profile.username == username).first()


def get_profile_by_id(db: Session, profile_id: int) -> models.Profile | None:
    return db.query(models.Profile).filter(models.Profile.id == profile_id).first()



def update_profile(db: Session, profile_id: int, profile: schemas.ProfileUpdate) -> models.Profile | None:
    db_profile = get_profile_by_id(db, profile_id)
    if not db_profile:
        return None

    update_data = profile.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_profile, field, value)

    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile


def delete_profile(db: Session, profile_id: int) -> bool:
    db_profile = get_profile_by_id(db, profile_id)
    if not db_profile:
        return False

    db.delete(db_profile)
    db.commit()
    return True


# SKILL


def create_skill(db: Session, skill: schemas.SkillCreate) -> models.Skill:
    db_skill = models.Skill(**skill.model_dump())
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill


def get_skill(db: Session, skill_id: int) -> models.Skill | None:
    """Retrieve a skill by ID."""
    return db.query(models.Skill).filter(models.Skill.id == skill_id).first()


def get_skills(db: Session, skip: int = 0, limit: int = 100) -> list[models.Skill]:
    """Retrieve a list of skills."""
    return db.query(models.Skill).offset(skip).limit(limit).all()


def get_skills_by_category(db: Session, category: str) -> list[models.Skill]:
    """Retrieve skills by category."""
    return db.query(models.Skill).filter(models.Skill.category == category).all()


def update_skill(db: Session, skill_id: int, skill: schemas.SkillCreate) -> models.Skill | None:
    """Update an existing skill."""
    db_skill = get_skill(db, skill_id)

    if not db_skill:
        return None

    update_data = skill.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_skill, field, value)

    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill


# STATUS


def create_status(db: Session, status: schemas.StatusCreate) -> models.Status:
    """Create a new status in the database."""
    db_status = models.Status(**status.model_dump())
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status


def get_status(db: Session, status_id: int) -> models.Status | None:
    """Retrieve a status by ID."""
    return db.query(models.Status).filter(models.Status.id == status_id).first()


def get_current_status(db: Session) -> models.Status | None:
    """Retrieve the first status record."""
    return db.query(models.Status).first()


def get_statuses(db: Session, skip: int = 0, limit: int = 100) -> list[models.Status]:
    """Retrieve a list of status records."""
    return db.query(models.Status).offset(skip).limit(limit).all()


def update_status(db: Session, status_id: int, status: schemas.StatusCreate) -> models.Status | None:
    """Update an existing status."""
    db_status = get_status(db, status_id)

    if not db_status:
        return None

    update_data = status.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_status, field, value)

    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status


def delete_status(db: Session, status_id: int) -> bool:
    """Delete a status by ID."""
    db_status = get_status(db, status_id)

    if not db_status:
        return False

    db.delete(db_status)
    db.commit()
    return True


# PROJECT


def create_project(db: Session, project: schemas.ProjectCreate) -> models.Project:
    """Create a new project in the database."""
    db_project = models.Project(**project.model_dump())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def get_project(db: Session, project_id: int) -> models.Project | None:
    """Retrieve a project by ID."""
    return db.query(models.Project).filter(models.Project.id == project_id).first()


def get_project_by_name(db: Session, name: str) -> models.Project | None:
    """Retrieve a project by name."""
    return db.query(models.Project).filter(models.Project.name == name).first()


def get_projects(db: Session, skip: int = 0, limit: int = 100) -> list[models.Project]:
    """Retrieve a list of projects."""
    return db.query(models.Project).offset(skip).limit(limit).all()


def update_project(db: Session, project_id: int, project: schemas.ProjectUpdate) -> models.Project | None:
    """ Update an existing project."""
    db_project = get_project(db, project_id)

    if not db_project:
        return None

    update_data = project.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_project, field, value)

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