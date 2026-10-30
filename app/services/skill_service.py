from sqlalchemy.orm import Session

from app.crud import skill_crud
from app.exceptions import (ResourceNotFoundError, DuplicateResourceError)


def create_skill(db: Session, skill):
    """Create new skill"""
    existing_skill = skill_crud.get_skill_by_id(db, skill.id)

    if existing_skill:
        raise DuplicateResourceError(f"Skill '{skill.id}' already exists")

    return skill_crud.create_skill(db=db, skill=skill)


def get_skills(db: Session, skip: int, limit:int):
    """Retrieve all skills"""
    return skill_crud.get_skills(db=db, skip=skip, limit=limit)


def get_skill_by_id(db: Session, skill_id: int):
    skill = skill_crud.get_skill_by_id(db=db, skill_id=skill_id)

    if skill is None:
        raise ResourceNotFoundError(f"Skill '{skill_id}' not found")

    return skill


def update_skill(db: Session, skill_id: int, skill):
    """Update skill by id"""
    existing_skill = skill_crud.get_skill_by_id(db=db, skill_id=skill_id)

    if existing_skill is None:
        raise ResourceNotFoundError(f"Skill '{skill_id}' not found")

    return skill_crud.update_skill_by_id(db=db, skill_id=skill_id, skill=skill)


def delete_skill(db: Session, skill_id: int):
    skill = skill_crud.get_skill_by_id(db=db, skill_id=skill_id)

    if skill is None:
        raise ResourceNotFoundError(f"SKill '{skill_id}' not found")

    return skill_crud.delete_skill_by_id(db=db, skill_id=skill_id)