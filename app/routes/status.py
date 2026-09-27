from fastapi import APIRouter
from pydantic import BaseModel


class Status(BaseModel):
    current_projects: str
    learning: str
    goals: list[str]
    last_updated: str


router = APIRouter(prefix="/status")


@router.get("", response_model=Status)
def get_status():
    return Status(
        current_projects="Building personal FastAPI portfolio API",
        learning="Advanced Python, backend development, GitHub workflows",
        goals=[
            "Transition into QA Automation / Backend Python",
            "Build portfolio projects",
            "Deploy FastAPI apps",
            "Grow GitHub activity",
        ],
        last_updated="2026-09-15",
    )
