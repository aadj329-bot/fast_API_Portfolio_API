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


def test_delete_project(client, created_project):
    """Test delete project by first creating a project"""
    project = created_project["name"]

    # Delete created project
    response = client.delete(
        f"/projects/{project}"
    )

    # Assertions
    assert response.status_code == 200


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


def test_delete_project_not_found(client):
    """Test deleting a non-existent project"""
    response = client.delete(
        "/projects/999"
    )

    # Assertions
    assert response.status_code == 404