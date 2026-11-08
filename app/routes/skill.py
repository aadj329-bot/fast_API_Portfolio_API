from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.schemas import SkillCreateModel, SkillResponseModel, SkillUpdateModel
from app.services import skill_service
from core.database import get_db

router = APIRouter(prefix="/skills", tags=["skills"])


@router.post("", response_model=SkillResponseModel, status_code=status.HTTP_201_CREATED)
def create_skill(skill: SkillCreateModel, db: Session = Depends(get_db)):
    """Create a new skill."""
    return skill_service.create_skill(db=db, skill=skill)


@router.get("", response_model=list[SkillResponseModel])
def get_skills(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all skills with opional filtering."""
    return skill_service.get_skills(db, skip=skip, limit=limit)


@router.get("/{skill_name}", response_model=SkillResponseModel)
def get_skill_by_name(skill_name: str, db: Session = Depends(get_db)):
    """Get a skill by name"""
    return skill_service.get_skill_by_name(db, skill_name=skill_name)

@router.put("/{skill_name}", response_model=SkillResponseModel)
def update_skill_by_name(skill_name: str, skill: SkillUpdateModel, db: Session = Depends(get_db)):
    """Update a skill by name"""
    return skill_service.update_skill(db=db, skill_name=skill_name, skill=skill)
    


@router.delete("/{skill_name}")
def delete_skill_by_name(skill_name: str, db: Session = Depends(get_db)):
    """Delete a skill by name"""
    success = skill_service.delete_skill(db=db, skill_name=skill_name)
    return {"message": "Skill deleted successfully"}
