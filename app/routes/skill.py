from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from core.database import get_db
from app.schemas import SkillResponseModel, SkillCreateModel, SkillUpdateModel
from app.services import skill_service

router = APIRouter(prefix="/skills", tags=["skills"])


@router.post("", response_model=SkillResponseModel, status_code=status.HTTP_201_CREATED)
def create_skill(skill: SkillCreateModel, db: Session = Depends(get_db)):
    """Create a new skill."""
    return skill_service.create_skill(db=db, skill=skill)


@router.get("", response_model=list[SkillResponseModel])
def get_skills(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all skills with opional filtering."""
    return skill_service.get_skills(db, skip=skip, limit=limit)


@router.get("/{skill_id}", response_model=SkillResponseModel)
def get_skill_by_id(skill_id: int, db: Session = Depends(get_db)):
    """Get a skill by ID."""
    return skill_service.get_skill_by_id(db, skill_id=skill_id)

@router.put("/{skill_id}", response_model=SkillResponseModel)
def update_skill_by_id(skill_id: int, skill: SkillUpdateModel, db: Session = Depends(get_db)):
    """Update a skill by ID."""
    return skill_service.update_skill(db=db, skill_id=skill_id, skill=skill)
    


@router.delete("/{skill_id}")
def delete_skill_by_id(skill_id: int, db: Session = Depends(get_db)):
    """Delete a skill by ID."""
    success = skill_service.delete_skill(db=db, skill_id=skill_id)
    return {"message": "Skill deleted successfully"}
