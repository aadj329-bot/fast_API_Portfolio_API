from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.database import create_tables, get_db
from app.routes import profile, project, skill, status, task
from app.exceptions import (ResourceNotFoundError, DuplicateResourceError)
from app.error_handlers import (resource_not_found_handler, duplicate_resource_handler)


app = FastAPI()


# Configure CORS
origins = [
    'https://localhost',
    'https:localhost:8080',
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create the tables on startup
@app.on_event("startup")
async def on_startup():
    create_tables()


# Include routers
app.include_router(profile.router)
app.include_router(project.router)
app.include_router(skill.router)
app.include_router(status.router)
app.include_router(task.router)


# Exception handlers
app.add_exception_handler(ResourceNotFoundError, resource_not_found_handler)
app.add_exception_handler(DuplicateResourceError, duplicate_resource_handler)


# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to Aaron's GitHub API"}


# Health endpoint
@app.get("/health")
async def health():
    return {"status": "ok"}