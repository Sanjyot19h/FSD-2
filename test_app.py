import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_create_student(client):
    response = client.post("/students", json={"name": "Sanjyot"})
    assert response.status_code == 201
    assert response.json["name"] == "Sanjyot"

def test_get_students(client):
    response = client.get("/students")
    assert response.status_code == 200