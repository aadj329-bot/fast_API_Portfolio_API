from fastapi import FastAPI
from app.database import create_tables, SessionLocal


app = FastAPI(title="Aaron's GitHub API")


# Create the database tables when the app starts
import asyncio


async def initialize_database():
    # Create database tables
    create_tables()
    print("Database intialized successfully")


async def main():
    await initialize_database()
    
    # Create FastAPI app
    app = FastAPI(lifespan=app)

    # Include the routes
    app.include_router(profile.router)
    app.include_router(skills.router)
    app.include_router(projects.router)
    app.include_router(status.router)

    
async def async_main():
    # Initialize the database
    create_tables()

    # Create the FastAPI app
    app = FastAPI(title="Aaron's GitHub API")

    # Add your routes
    app.include_router(profile.router)
    app.include_router(skills.router)
    app.include_router(status.router)
    app.include_router(projects.router)

    # Add routes
    @app.get("/")
    async def root():
        return {"message": "Welcome to Aaron's GitHub API"}

    @app.get("/health")
    async def health():
        return{"status": "ok"}

    return app