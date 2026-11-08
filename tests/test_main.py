import pytest


def test_root_endpoint(client):
    """Test root endpoint"""
    response = client.get("/")

    # Assertions
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to Aaron's GitHub API"
    }


def test_health_endpoint(client):
    """Test health endpoint"""
    response = client.get("/health")

    # Assertions
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok"
    }