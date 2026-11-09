import pytest
import uuid


def test_create_project(client):
    """Test create a new project"""
    response = client.post(
        "/projects",
        json={
            "name": "Portfolio API",
            "description": "FastAPI project",
            "language": "Python",
            "url": "https://github.com/example",
            "visibility": "public"
        }
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Portfolio API"
    assert response.json()["description"] == "FastAPI project"
    assert response.json()["visibility"] == "public"


def test_project_duplication(client):
    """Test duplication handling"""
    payload = {
            "name": "FastAPI Portfolio",
            "description": "FastAPI project",
            "language": "Python",
            "url": "https://github.com/example",
            "visibility": "public"        
    }
    # First create succeeds
    first_response = client.post(
        "/projects",
        json=payload
    )

    # Assertion
    assert first_response.status_code == 201

    # Second create should fail
    response = client.post(
        "/projects",
        json=payload
    )

    # Assertion
    assert response.status_code == 409


@pytest.fixture
def created_project(client):
    """Fixture to create a project for testing"""
    response = client.post(
        "/projects",
        json={
            "name": f"project-{uuid.uuid4().hex[:8]}",
            "description": "FastAPI project",
            "language": "Python",
            "url": "https://github.com/example",
            "visibility": "public"
        }
    )
    
    assert response.status_code == 201
    return response.json()


def test_get_project_by_name(client, created_project):
    """Create and test retrieve project"""
    project_test = created_project["name"]

    response = client.get(
        f"/projects/{project_test}"
    )

    # Assertions
    assert response.status_code == 200
    assert response.json()["description"] == "FastAPI project"
    assert response.json()["visibility"] == "public"


def test_get_project_not_found(client):
    """Test get with non-existent project"""
    response = client.get(
        "/projects/989"
    )

    # Assertion
    assert response.status_code == 404


def test_get_projects(client):
    """Test fetching all projects"""
    response = client.get("/projects")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_project(client, created_project):
    """Create project and test update """
    project = created_project["name"]

    response = client.put(
        f"/projects/{project}",
        json={
            "name": "Update Name"
        }
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Update Name"


def test_update_project_not_found(client):
    """Test update with non-existent project name"""
    response = client.put(
        "/projects/999",

        json={
            "name": "Update Name"
        }
    )

    # Assertions
    assert response.status_code == 404
    assert response.json()["message"] == "Project '999' not found"


def test_update_project_duplicate_name(client):
    """Attempt to rename a project to an existing one"""

    # Create first project
    client.post(
        "/projects",
        json={
            "name": "Project One",
            "description": "Place holder one",
            "language": "Python",
            "url": "https://placeholer.com",
            "visibility": "public"
        }
    )

    # Create second project
    client.post(
        "/projects",
        json={
            "name": "Project Two",
            "description": "Second Placeholer",
            "language": "Python",
            "url": "https://holdensecond.com",
            "visibility": "public"
        }
    )

    # Test
    response = client.put(
        "/projects/Project One",
        json ={
            "name": "Project Two"
        }
    )

    # Assertion
    assert response.status_code == 409


def test_update_project_invalid_data(client, created_project):
    """Test updating a project with invalid data"""
    project = created_project["name"]

    response = client.put(
        f"/projects/{project}",
        json={
            "name": ""
        }
    )

    assert response.status_code == 422


def test_delete_project(client, created_project):
    """Test delete project by first creating a project"""
    project = created_project["name"]

    # Delete created project
    response = client.delete(
        f"/projects/{project}"
    )

    # Assertions
    assert response.status_code == 200


def test_delete_project_not_found(client):
    """Test deleting a non-existent project"""
    response = client.delete(
        "/projects/999"
    )

    # Assertion
    assert response.status_code == 404