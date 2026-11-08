from sqlalchemy.orm import Session

from app.crud import skill_crud
from app.exceptions import DuplicateResourceError, ResourceNotFoundError


def create_skill(db: Session, skill):
    """Create new skill"""
    existing_skill = skill_crud.get_skill_by_name(db=db, skill_name=skill.name)

    if existing_skill:
        raise DuplicateResourceError(f"Skill '{skill.name}' already exists")

    return skill_crud.create_skill(db=db, skill=skill)


def get_skills(db: Session, skip: int, limit:int):
    """Retrieve all skills"""
    return skill_crud.get_skills(db=db, skip=skip, limit=limit)


def get_skill_by_name(db: Session, skill_name: str):
    """Retrieve skill by name"""
    skill = skill_crud.get_skill_by_name(db=db, skill_name=skill_name)

    if skill is None:
        raise ResourceNotFoundError(f"Skill '{skill_name}' not found")

    return skill


def update_skill(db: Session, skill_name: str, skill):
    """Update skill by name"""
    existing_skill = skill_crud.get_skill_by_name(db=db, skill_name=skill_name)

    if existing_skill is None:
        raise ResourceNotFoundError(f"Skill '{skill_name}' not found")

    return skill_crud.update_skill_by_name(db=db, skill_name=skill_name, skill=skill)


def delete_skill(db: Session, skill_name: str):
    """Delete a skill by name"""
    skill = skill_crud.get_skill_by_name(db=db, skill_name=skill_name)

    if skill is None:
        raise ResourceNotFoundError(f"SKill '{skill_name}' not found")

    return skill_crud.delete_skill_by_name(db=db, skill_name=skill_name)