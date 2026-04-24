import pytest
from app import app

# Dummy DB cursor
class DummyCursor:
    def execute(self, *args, **kwargs):
        pass

    def fetchall(self):
        return []

    def close(self):
        pass

# Dummy DB connection
class DummyConnection:
    def cursor(self):
        return DummyCursor()

    def commit(self):
        pass

# Dummy MySQL object
class DummyMySQL:
    connection = DummyConnection()

# Inject dummy mysql into app
app.mysql = DummyMySQL()

@pytest.fixture
def client():
    app.config['TESTING'] = True
    yield app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_get_students(client):
    response = client.get('/students')
    assert response.status_code == 200

def test_add_student(client):
    response = client.post('/students', json={
        "name": "Test",
        "email": "test@test.com",
        "age": 20,
        "course": "CSE"
    })
    assert response.status_code == 200