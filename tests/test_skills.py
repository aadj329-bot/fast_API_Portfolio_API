import pytest
import uuid


def test_create_skill(client):
    """Test skill creation"""
    response = client.post(
        "/skills",
        json={
            "id": 1,
            "category": "This and that",
            "name": "Aaron"
        }
    )

    # Assertions
    assert response.status_code == 201
    assert response.json()["id"] == 1
    assert response.json()["category"] == "This and that"
    assert response.json()["name"] == "Aaron"


def test_create_duplicate(client):
    """Test creating a duplicate skill"""
    response = client.post(
        "/skills",
        json={
            "id": 1,
            "category": "This and that",
            "name": "Aaron"
        }
    )

    # Assertion
    assert response.status_code == 409


@pytest.fixture
def created_skill(client):
    """Fixture to create a skill for testing"""
    response = client.post(
        "/skills",
        json={
            "category": "That and this",
            "name": f"skill-{uuid.uuid4().hex[:8]}"
        }
    )

    # Assert creation and return
    assert response.status_code == 201
    return response.json()


def test_get_skill_by_name(client, created_skill):
    """Test retrieving skill by name"""
    skill_name = created_skill["name"]
    
    response = client.get(
        f"/skills/{skill_name}"
    )

    # Assertions
    assert response.status_code == 200
    assert response.json()["name"] == skill_name


def test_get_skill_not_found(client):
    """Test get with non-existent skill"""
    response = client.get("/skills/waldo")

    # Assertion
    assert response.status_code == 404


def test_get_skills(client):
    """Test get all skills"""
    response = client.get("/skills")

    # Assertions
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_skill(client, created_skill):
    """Create a skill and test update"""
    skill_test = created_skill["name"]

    response = client.put(
        f"/skills/{skill_test}",
        json={
            "category": "Whatever",
            "name": "aaron"
        }
    )

    # Assertions
    assert response.status_code == 200
    assert response.json()["category"] == "Whatever"
    assert response.json()["name"] == "aaron"


def test_update_skill_not_found(client):
    """Test update with non-existent skill"""
    response = client.put(
        "/skills/999",
        json={
            "category": "never gonna get it."
        }
    )

    print(response.status_code)
    print(response.json())
    
    # Assertion
    assert response.status_code == 404


def test_update_skill_duplicate_name(client):
    """Attempt to rename a skill to an existing one"""

    # Create first skill
    client.post(
        "/skills",
        json={
            "name": "Pytest",
            "category": "QA Automation"
        }
    )

    # Create second skill
    client.post(
        "/skills",
        json={
            "name": "unit-test",
            "category": "backend engineer"
        }
    )

    # Test
    response = client.put(
        "/skills/Pytest",
        json={
            "name": "unit-test",
            "category": "oh no"
        }
    )

    # Assertion
    assert response.status_code == 409


def test_delete_skill(client, created_skill):
    """Create a skill and test delete"""
    skill_test = created_skill["name"]

    # Delete created skill
    response = client.delete(
        f"/skills/{skill_test}"
    )

    # Assertons
    assert response.status_code == 200


def test_update_invalid_data(client, created_skill):
    """Test update with invalid data"""
    skill_test = created_skill["name"]

    response = client.put(
        f"/skills/{skill_test}",
        json={
            "name": ""
        }
    )

    # Assertion
    assert response.status_code == 422


def test_delete_skill_not_found(client):
    """Test deleting a non-existent skill"""
    response = client.delete(
        "/skills/999"
    )

    # Assertion
    assert response.status_code == 404
