from sqlalchemy.orm import Session
from fastapi import status

from app.models.skill_model import Skill
from app.schemas import SkillUpdateModel, SkillCreateModel



def create_skill(db: Session, skill: SkillCreateModel) -> Skill:
    """Create a new skill."""
    db_skill = Skill(**skill.model_dump(mode='json'))
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill


def get_skill_by_id(db: Session, skill_id: int) -> Skill | None:
    """Retrieve skill by ID."""
    return db.query(Skill).filter(Skill.id == skill_id).first()


def get_skills(db: Session, skip: int = 0, limit: int = 100) -> list[Skill]:
    """Retrieve a list of skills."""
    return db.query(Skill).offset(skip).limit(limit).all()


def update_skill_by_id(db: Session, skill_id: int, skill: SkillUpdateModel) -> Skill | None:
    """Retrieve skill by ID."""
    db_skill = get_skill_by_id(db, skill_id)

    if db_skill is None:
        return None

    update_data = skill.model_dump(exclude_unset=True, mode='json')

    for field, value in update_data.items():
        setattr(db_skill, field, value)

    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill


def delete_skill_by_id(db: Session, skill_id: int):
    """Delete skill by ID."""
    db_skill = get_skill_by_id(db, skill_id)

    if db_skill is None:
        return False
    
    db.delete(db_skill)
    db.commit()
    return True