import pytest


def test_create_status(client):
    """Test create status"""
    response = client.post(
        "/status",
        json={
            "current_projects": "FastAPI Portfolio",
            "learning": "The path of the one",
            "goals": ["To be the one", "To understand"]
        }
    )

    # Assertions
    assert response.status_code == 201
    assert response.json()["current_projects"] == "FastAPI Portfolio"
    assert response.json()["learning"] == "The path of the one"
    assert response.json()["goals"] == ["To be the one", "To understand"]


@pytest.fixture
def created_status(client):
    """Fixture to create status for testing"""
    response = client.post(
        "/status",
        json={
            "current_projects": "Portfolio API",
            "learning": "Become the one",
            "goals": ["To be", "Or not to be"]
        }
    )

    # Assert creation and return
    assert response.status_code == 201
    return response.json()


def test_get_status_by_id(client, created_status):
    """Test retrieval status by id"""
    status_id = created_status["id"]

    response = client.get(
        f"/status/{status_id}"
    )

    # Assertions
    assert response.status_code == 200
    assert response.json()["id"] == status_id


def test_get_statuses(client):
    """Test get all statuses"""
    response = client.get("/status/all")

    # Assertions
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_status_not_found(client):
    """Test get status with non-existent status"""
    response = client.get("/status/999")

    # Assertion
    assert response.status_code == 404


def test_update_status(client, created_status):
    """Create and test update status"""
    status_tester = created_status["id"]

    response = client.put(
        f"/status/{status_tester}",
        json={
            "current_projects": "Updated Portfolio",
            "learning": "FastAPI Testing",
            "goals": ["100% Coverage (Kool-aid man) Oh YEAH"]
        }
    )

    # Assertion
    assert response.status_code == 200


def test_update_status_not_found(client):
    """Test update with non-existent status"""
    response = client.put(
        "/status/999",
        json={
            "current_projects": "Ghost Project"
        }
    )

    # Assertion
    assert response.status_code == 404


def test_delete_status(client, created_status):
    """Create and test delete status"""
    status_test = created_status["id"]

    response = client.delete(
        f"/status/{status_test}"
    )

    # Assertion
    assert response.status_code == 200


def test_delete_status_not_found(client):
    """Test delete with a non-existent status"""
    response = client.delete(
        "/status/999"
    )

    # Assertion
    assert response.status_code == 404