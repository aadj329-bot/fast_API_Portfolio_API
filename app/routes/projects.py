from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.database import get_db
from app.schemas import Project, ProjectCreate
from app.crud import project_crud as crud


router = APIRouter(prefix="/projects")


@router.get("", response_model=list[Project])
def projects(db: Session = Depends(get_db)):
    """Get all projects."""
    return crud.get_projects(db)


@router.post("", response_model=Project, status_code=status.HTTP_201_CREATED)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    """Create a new project."""
    return crud.create_project(db=db, project=project)


@router.get("/{project_name}", response_model=Project)
def get_project_by_name(project_name: str, db: Session = Depends(get_db)):
    """Get a project by name."""
    db_project = crud.get_project_by_name(db, project_name=project_name)
    if db_project is None: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    return db_project


@router.put("/{project_name}", response_model=Project)
def update_project(project_name: str, project: ProjectCreate, db: Session = Depends(get_db)):
    """Update a project by ID."""
    db_project = crud.update_project(db=db, project_name=project_name, project=project)
    if db_project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    return db_project


@router.delete("/{project_name}")
def delete_project(project_name: int, db: Session = Depends(get_db)):
    """Delete a project by ID."""
    success = crud.delete_project(db=db, project_name=project_name)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    return {"message": "Project deleted successfully"}