import pytest
import uuid


def test_create_task(client):
    """Test task creation"""
    response = client.post(
        "/tasks",
        json={
            "id": 0,
            "title": "testing purposes",
            "description": "Making the bacon!"
        }
    )

    assert response.status_code == 201 
    assert response.json()["title"] == "testing purposes"
    assert response.json()["description"] == "Making the bacon!"


@pytest.fixture
def created_task(client):
    response = client.post(
        "/tasks",
        json={
            "title": f"task-{uuid.uuid4().hex[:8]}",
            "description": "Making the bacon!"
        }
    )

    assert response.status_code == 201
    return response.json()


def test_get_tasks(client):
    """Test get all tasks"""
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_task(client, created_task):
    """Test update task by first creating a task to update"""
    task_title = created_task["title"]

    # Update created task
    response = client.put(
        f"/tasks/{task_title}",
        json={
            "title": "Updated Title",
            "description": "Bacon is crispy"
        }
    )

    # Assertions
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"
    assert response.json()["description"] == "Bacon is crispy"


def test_delete_task(client, created_task):
    """Test delete task by first creating a task to delete"""
    task_title = created_task["title"]

    # Delete created task
    response = client.delete(
        f"/tasks/{task_title}"
    )

    # Assertions
    assert response.status_code == 200


def test_update_task_not_found(client):
    """Test update with non-existent task title"""
    response = client.put(
        "/tasks/999",
        json={
            "title": "testing purposes",
            "description": "Making the bacon!"
        }
    )

    assert response.status_code == 404


def test_update_task_invalid_data(client, created_task):
    """Test update task with invalid data"""
    task_title = created_task["title"]

    # Update created task with invalid data
    response = client.put(
        f"/tasks/{task_title}",
        json={
            "title": "",
            "description": "Bacon is crispy"
        }
    )

    assert response.status_code == 422

