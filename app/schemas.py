from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional


# Profile schemas
class ProfileBaseModel(BaseModel):
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


class ProfileCreate(ProfileBaseModel):
    pass


class ProfileUpdateModel(BaseModel):
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


class ProfileResponseModel(ProfileBaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Skill schemas
class SkillBaseModel(BaseModel):
    category: str
    name: str


class SkillCreateModel(SkillBaseModel):
    pass


class SkillUpdateModel(BaseModel):
    category: Optional[str] = None
    name: Optional[str] = None


class SkillResponseModel(SkillBaseModel):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
        

# Status schemas
class StatusBaseModel(BaseModel):
    current_projects: str
    learning: str
    goals: list[str]


class StatusCreateModel(StatusBaseModel):
    pass


class StatusResponseModel(StatusBaseModel):
    id: int
    updated_at: datetime

    class Config:
        from_attributes = True

class StatusUpdateModel(StatusBaseModel):
    current_projects: Optional[str]
    learning: Optional[str]
    goals: Optional[str]


# Project schemas
class ProjectBaseModel(BaseModel):
    name: str
    description: str
    language: str
    url: HttpUrl
    visibility: str


class ProjectCreateModel(ProjectBaseModel):
    pass


class ProjectUpdateModel(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    language: Optional[str] = None
    url: Optional[HttpUrl] = None
    visibility: Optional[str] = None


class ProjectResponseModel(ProjectBaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Task Schemas
class TaskBaseModel(BaseModel):
    title: str
    description: str
    

class TaskCreateModel(TaskBaseModel):
    pass 


class TaskUpdateModel(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    


class TaskResponseModel(TaskBaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    