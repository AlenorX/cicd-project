from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read():
    response = client.get("/random/status")
    assert response.status_code == 200