from datetime import datetime

from pydantic import BaseModel, HttpUrl, ConfigDict, Field


# Profile schemas

class ProfileCreateModel(BaseModel):
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


class ProfileResponseModel(BaseModel):
    id: int
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
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


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


# Skill schemas

class SkillCreateModel(BaseModel):
    category: str
    name: str


class SkillResponseModel(BaseModel):
    id: int
    category: str
    name: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class SkillUpdateModel(BaseModel):
    category: str | None = None
    name: str | None = Field(default=None, min_length=1)


# Status schemas

class StatusCreateModel(BaseModel):
    current_projects: str
    learning: str
    goals: list[str]


class StatusResponseModel(BaseModel):
    id: int
    current_projects: str
    learning: str
    goals: list[str]
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class StatusUpdateModel(BaseModel):
    current_projects: str | None = None
    learning: str | None = None
    goals: list[str] | None = None


# Project schemas

class ProjectCreateModel(BaseModel):
    name: str
    description: str
    language: str
    url: HttpUrl
    visibility: str


class ProjectResponseModel(BaseModel):
    id: int
    name: str
    description: str
    language: str
    url: HttpUrl
    visibility: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ProjectUpdateModel(BaseModel):
    name: str | None = Field(None, min_length=1)
    description: str | None = None
    language: str | None = None
    url: HttpUrl | None = None
    visibility: str | None = None


# Task Schemas

class TaskCreateModel(BaseModel):
    title: str
    description: str
    

class TaskResponseModel(BaseModel):
    title: str
    title: str
    description: str
    created_at: datetime
    updated_at: datetime


class TaskUpdateModel(BaseModel):
    title: str | None = Field(None, min_length=1)
    description: str | None = None