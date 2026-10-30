from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()
    assert data["message"] == "E-Commerce API is running"
    assert data["project"] == "production-devops-ecommerce"