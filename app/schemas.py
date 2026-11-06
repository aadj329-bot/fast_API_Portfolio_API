from datetime import datetime

from pydantic import BaseModel, HttpUrl, ConfigDict, Field


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


class ProfileCreateModel(ProfileBaseModel):
    pass


class ProfileUpdateModel(BaseModel):
    username: str | None = Field(None, min_length=1)
    full_name: str | None = None
    bio: str | None = None
    location: str | None = None
    github_url: HttpUrl | None = None
    primary_language: list[str] | None = None
    secondary_language: list[str] | None = None
    current_focus: str | None = None
    learning_path: str | None = None
    projects_count: int | None = None


class ProfileResponseModel(ProfileBaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


# Skill schemas
class SkillBaseModel(BaseModel):
    id: int
    category: str
    name: str


class SkillCreateModel(SkillBaseModel):
    pass


class SkillUpdateModel(BaseModel):
    category: str | None = Field(None, min_length=1)
    name: str | None = None


class SkillResponseModel(SkillBaseModel):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

# Status schemas
class StatusBaseModel(BaseModel):
    id: int
    current_projects: str
    learning: str
    goals: list[str]


class StatusCreateModel(StatusBaseModel):
    pass


class StatusResponseModel(StatusBaseModel):
    id: int
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class StatusUpdateModel(StatusBaseModel):
    current_projects: str | None
    learning: str | None
    goals: list | None


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
    name: str | None = Field(None, min_length=1)
    description: str | None = None
    language: str | None = None
    url: HttpUrl | None = None
    visibility: str | None = None


class ProjectResponseModel(ProjectBaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


# Task Schemas
class TaskBaseModel(BaseModel):
    title: str
    description: str
    

class TaskCreateModel(TaskBaseModel):
    pass 


class TaskUpdateModel(BaseModel):
    title: str | None = Field(None, min_length=1)
    description: str | None = None
    


class TaskResponseModel(TaskBaseModel):
    title: str
    created_at: datetime
    updated_at: datetime
    