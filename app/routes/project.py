from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from core.database import get_db
from app.schemas import ProjectResponseModel, ProjectCreateModel, ProjectUpdateModel
from app.services import project_service


router = APIRouter(prefix="/projects")


@router.post("", response_model=ProjectResponseModel, status_code=status.HTTP_201_CREATED)
def create_project(project: ProjectCreateModel, db: Session = Depends(get_db)):
    """Create a new project."""
    return project_service.create_project(db=db, project=project)


@router.get("/{project_name}", response_model=ProjectResponseModel)
def get_project_by_name(project_name: str, db: Session = Depends(get_db)):
    """Get a project by name."""
    return project_service.get_project_by_name(db=db, project_name=project_name) 


@router.get("", response_model=list[ProjectResponseModel])
def projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all projects."""
    return project_service.get_projects(db=db, skip=skip, limit=limit)


@router.put("/{project_name}", response_model=ProjectResponseModel)
def update_project_by_name(project_name: str, project: ProjectUpdateModel, db: Session = Depends(get_db)):
    """Update a project by name."""
    return project_service.update_project(db=db, project_name=project_name, project=project)


@router.delete("/{project_name}")
def delete_project_by_name(project_name: str, db: Session = Depends(get_db)):
    """Delete a project by name."""
    project_service.delete_project(db=db, project_name=project_name)
    return{"message": "Project deleted successfully"}
        