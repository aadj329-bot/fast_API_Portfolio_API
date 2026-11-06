import pytest
import uuid


def test_create_profile(client):
    """Test create a new profile"""
    response = client.post(
        "/profile", 
        json={
            "username": "tester",
            "full_name": "testing testerton",
            "bio": "Like you wouldn't believe",
            "location": "123 What St. Birmingham, New York",
            "github_url": "https://github.com/example",
            "primary_language": ["Python"],
            "secondary_language": ["JavaScript"],
            "current_focus": "Getting a better job",
            "learning_path": "Learning by doing",
            "projects_count": 3    
        }
    )

    # Assertions
    assert response.status_code == 201
    assert response.json()["username"] == "tester"
    assert response.json()["full_name"] == "testing testerton"
    assert response.json()["bio"] == "Like you wouldn't believe"
    assert response.json()["location"] == "123 What St. Birmingham, New York"
    assert response.json()["github_url"] == "https://github.com/example"
    assert response.json()["primary_language"] == ["Python"]
    assert response.json()["secondary_language"] == ["JavaScript"]
    assert response.json()["current_focus"] == "Getting a better job"
    assert response.json()["learning_path"] == "Learning by doing"
    assert response.json()["projects_count"] == 3



@pytest.fixture
def created_profile(client):
    """Fixture to create a project for testing"""
    response = client.post(
        "/profile",
        json={
            "username": f"user_{uuid.uuid4().hex[:8]}",
            "full_name": "testing testerton",
            "bio": "Like you wouldn't believe",
            "location": "123 What St. Birmingham, New York",
            "github_url": "https://github.com/example",
            "primary_language": ["Python"],
            "secondary_language": ["JavaScript"],
            "current_focus": "Getting a better job",
            "learning_path": "Learning by doing",
            "projects_count": 3 

        }
    )

    assert response.status_code == 201, response.json()
    return response.json()


def test_update_profile(client, created_profile):
    """Create a profile and test update"""
    profile_test = created_profile["username"]

    response = client.put(
        f"/profile/{profile_test}",
        json={
            "full_name": "Bestie testing testerton"
        }
    )

    print(response.json())

    # Assertions
    assert response.status_code == 200
    assert response.json()["username"] == profile_test
    assert response.json()["full_name"] == "Bestie testing testerton"


def test_delete_profile(client, created_profile):
    """Create a profile and test delete"""
    profile_test = created_profile["username"]

    response = client.delete(
        f"/profile/{profile_test}"
    )

    # Assertions
    assert response.status_code == 200


def test_update_profile_not_found(client):
    """Test update with non-existent profile"""
    response = client.put(
        "/profile/999",
        json={
            "username": "Haddy"
        }
    )

    print(response.json())

    assert response.status_code == 404


def test_update_profile_invalid_data(client, created_profile):
    """Test update profile with invalid data"""
    profile_test = created_profile["username"]

    response = client.put(
        f"/profile/{profile_test}",
        json={
            "username": ""
        }
    )

    assert response.status_code == 422

