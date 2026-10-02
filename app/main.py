from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import create_tables, get_db
from routes import profile, projects, skills, status


app = FastAPI()


# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create the tables on startup
@app.on_event("startup")
async def on_startup():
    create_tables()


# Include routers
app.include_router(profile.router)
app.include_router(projects.router)
app.include_router(skills.router)
app.include_router(status.router)

# 