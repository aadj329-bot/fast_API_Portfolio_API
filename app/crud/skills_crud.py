from sqlalchemy.orm import Session
from app.models import skill_model as models
from app import schemas


# SKILL CRUD OPERATIONS


def create_skill(db: Session, skill: schemas.SkillCreate) -> models.Skill:
    """Create a new skill."""
    db_skill = models.Skill(**skill.model_dump())
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill


def get_skill(db: Session, skill_id: int) -> models.Skill | None:
    """Retrieve skill by ID."""
    return db.query(models.Skill).filter(models.Skill.id == skill_id).first()


def get_skills(db: Session, skip: int = 0, limit: int = 100) -> list[models.Skill]:
    """Retrieve a list of skills."""
    return db.query(models.Skill).offset(skip).limit(limit).all()


def get_skills_by_category(db: Session, category: str) -> list[models.Skill]:
    """Retrieve skills by category."""
    return db.query(models.Skill).filter(models.Skill.category == category).all()


def update_skill(db: Session, skill_id: int, skill: schemas.SkillCreate) -> models.Skill | None:
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