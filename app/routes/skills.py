from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import Skill, SkillCreate
from app import crud

router = APIRouter(prefix="/skills", tags=["skills"])


@router.post("", response_model=Skill, status_code=status.HTTP_201_CREATED)
def create_skill(skill: SkillCreate, db: Session = Depends(get_db)):
    """Create a new skill."""
    return crud.create_skill(db=db, skill=skill)


@router.get("", response_model=list[Skill])
def get_skills(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all skills with opional filtering."""
    return crud.get_skills(db, skip=skip, limit=limit)


@router.get("/category/{category}", response_model=list[Skill])
def get_skills_by_category(category: str, db: Session = Depends(get_db)):
    """Get skills filtered by category (e.g., 'language', 'framework', 'tool',
    'concept')."""
    skills = crud.get_skills_by_category(db, category=category)
    if not skills:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No skills found in category '{category}'"
        )
    return skills


@router.get("/{skill_id}", response_model=Skill)
def get_skill(skill_id: int, db: Session = Depends(get_db)):
    """Get a skill by ID."""
    db_skill = crud.get_skill(db, skill_id=skill_id)
    if not db_skill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Skill not found"
        )
    return db_skill


@router.put("/{skill_id}", response_model=Skill)
def update_skill(skill_id: int, skill: SkillCreate, db: Session = Depends(get_db)):
    """Update a skill by ID."""
    db_skill = crud.update_skill(db=db, skill_id=skill_id, skill=skill)
    if not db_skill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Skill not found"
        )
    return db_skill


@router.delete("/{skill_id}")
def delete_skill(skill_id: int, db: Session = Depends(get_db)):
    """Delete a skill by ID."""
    success = crud.delete_skill(db=db, skill_id=skill_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Skill not found"
        )
    return {"message": "Skill deleted successfully"}
