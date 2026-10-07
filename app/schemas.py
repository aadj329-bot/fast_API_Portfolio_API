from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional


# Profile schemas
class ProfileBase(BaseModel):
    username: str
    full_name: str
    bio: str
    location: str
    github_url: HttpUrl
    primary_language: list[str]
    secondary_language: list[str]
    current_focus: str
    learning_path: str
    projects_count: int


class ProfileCreate(ProfileBase):
    pass


class ProfileUpdate(BaseModel):
    username: Optional[str] = None
    full_name: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    github_url: Optional[HttpUrl] = None
    primary_language: Optional[list[str]] = None
    secondary_language: Optional[list[str]] = None
    current_focus: Optional[str] = None
    learning_path: Optional[str] = None
    projects_count: Optional[int] = None


class Profile(ProfileBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Skill schemas
class SkillBase(BaseModel):
    category: str
    name: str


class SkillCreate(SkillBase):
    pass


class SkillUpdate(BaseModel):
    category: Optional[str] = None
    name: Optional[str] = None


class Skill(SkillBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
        

# Status schemas
class StatusBase(BaseModel):
    current_projects: str
    learning: str
    goals: list[str]


class StatusCreate(StatusBase):
    pass


class StatusResponse(StatusBase):
    id: int
    last_updated: datetime

    class Config:
        from_attributes = True


# Project schemas
class ProjectBase(BaseModel):
    name: str
    description: str
    language: str
    url: HttpUrl
    visibility: str


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    language: Optional[str] = None
    url: Optional[HttpUrl] = None
    visibility: Optional[str] = None


class Project(ProjectBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True