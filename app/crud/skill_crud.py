from sqlalchemy.orm import Session

from app.models.skill_model import Skill
from app.schemas import SkillCreateModel, SkillUpdateModel


def create_skill(db: Session, skill: SkillCreateModel) -> Skill:
    """Create a new skill"""
    db_skill = Skill(**skill.model_dump(mode='json'))
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill


def get_skill_by_name(db: Session, skill_name: str) -> Skill | None:
    """Retrieve skill by name"""
    return db.query(Skill).filter(Skill.name == skill_name).first()


def get_skills(db: Session, skip: int = 0, limit: int = 100) -> list[Skill]:
    """Retrieve a list of skills"""
    return db.query(Skill).offset(skip).limit(limit).all()


def update_skill_by_name(db: Session, skill_name: str, skill: SkillUpdateModel) -> Skill | None:
    """Retrieve skill by name"""
    db_skill = get_skill_by_name(db, skill_name)

    if db_skill is None:
        return None

    update_data = skill.model_dump(exclude_unset=True, mode='json')

    for field, value in update_data.items():
        setattr(db_skill, field, value)

    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill


def delete_skill_by_name(db: Session, skill_name: str):
    """Delete skill by name"""
    db_skill = get_skill_by_name(db, skill_name)

    if db_skill is None:
        return False
    
    db.delete(db_skill)
    db.commit()
    return True