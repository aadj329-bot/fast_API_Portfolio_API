# FastAPI Portfolio API

This project is a portfolio API built with FastAPI and SQLAlchemy to showcase my profile, technical skills, projects, and ongoing learning journey. 
Beyond serving portfolio data through RESTful endpoints, it demonstrates backend development fundamentals including database design, CRUD operations, 
schema migrations, automated testing, and clean application architecture.

## Features

- RESTful API built with FastAPI
- Stores and serves portfolio data using SQLAlchemy ORM
- Manages portfolio resources including profiles, skill, projects, statuses and tasks
- Supports CRUD operations for portfolio
- Uses Pydantic models for request and response validation
- Includes health-check endpoint for service monitoring
- Automated test suite built with pytest
- Continuous Integration (CI) with GitHub Actions
- Database schemas management with Alembic migrations

## Tech Stack

### Category                   ### Technologies

Backend                    FastAPI, Python 3, SQLAlchemy
Database                   SQLite, Alembic
Validation                 Pydantic
Testing                    Pytest
Version Control            Git, GitHub
API Design                 RESTful Endpoints, CRUD Operations, Dependency Injection

## Architecture

Client Request
   ↓
Routes
   ↓
Services
   ↓
CRUD
   ↓
SQLAlchemy
   ↓
Database

## Project Structure

app/
  main.py          App setup, routers, CORS, exception handlers
  routes/          CRUD HTTP endpoints for portfolio resources
  services/        Resource checks and business logic
  crud/            SQLAlchemy create/read/update/delete operations
  models/          SQLAlchemy tables: profiles, projects, skills, statuses, tasks
  schemas.py       Pydantic create, response, and update models
  error_handlers.py
                   Maps custom errors to HTTP responses
core/
  database.py      DATABASE_URL configuration and session dependency
alembic/
  env.py           Migration configuration
  versions/        Initial database schema migration
tests/
  conftest.py      In-memory SQLite test setup and DB dependency override
  test_*.py        API and resource tests
.github/workflows/
  test.yml         CI runs pytest with a 95% coverage threshold
run.py             Uvicorn startup entry point

## Setup

### 1. Clone the repository:

```bash
git clone https://github.com/aadj329-bot/fast_API_Portfolio_API.git
cd fast_API_Portfolio_API
```

## 2. Create a virtual environment:

### Windows PowerShell

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install the project dependencies:

```bash
pip install -r requirements.txt
```

## 4. Run the API

Start the application with:

```bash
python run.py
```

### Once Running, the API will be available at:

Resource	URL
- API	http://127.0.0.1:8000
- Swagger UI	http://127.0.0.1:8000/docs
- ReDoc	http://127.0.0.1:8000/redoc

## API Resources

### Resource    Supported Operations
Profile         Create, Read, Update, Delete
Skills          Create, Read, Update, Delete
Projects        Create, Read, Update, Delete
Statuses        Create, Read, Update, Delete
Tasks           Create, Read, Update, Delete

## Running Tests

Run the test suite with:

```bash
python -m pytest --cov=app --cov-report=term-missing
```

The tests will verify several aspects:

- successful response from the API endpoints
- expected response data
- invalid routes returning 404
- unsupported methods returning 405
- response fields having the expected types
- project data being returned correctly
- The test suite includes endpoint, validation, and database operation tests and maintains a 95% coverage requirement through the CI pipeline

## Continuous Integration

This project uses GitHub Actions for continuous integration.

The workflow runs automatically when:

- Code is pushed to the repository
- A pull request is opened or updated

The workflow:

    1. Check out the repository
    2. Install Python
    3. Install dependencies from `requirements.txt`
    4. Runs the pytest test suite

The workflow file is located at:

.github/workflows/test.yml

## What I Am Learning

This project gives me hands-on experience with:

- Designing RESTful APIs with FastAPI
- Structuring Python applications using layered architecture
- Managing database schemas with Alembic migrations
- Building and testing CRUD operations
- Validating data with Pydantic
- Writing automated tests with Pytest
- Using Git and GitHub in a development workflow
- Automating quality checks with GitHub Actions
- Refactoring code while maintaining test coverage

## Future Improvements

Future improvements will include:

    - Adding more portfolio projects
    - Expand exception handling and application logging 
    - Adding authentication and authorization
    - Adding project filtering and search functionality
    - Deploying the API
    - Building a frontend interface

## About the Author

Hello, my name is Aaron Johnson. I am an aspiring backend developer transitioning into software engineering through hands-on project work and continuous learning.

This repository serves as both a portfolio piece and a learning project. This allows me to apply concepts such as API design, database modeling, automated testing, migrations and continuous integration within a real-world codebase.

GitHub: https://github.com/aadj329-bot
