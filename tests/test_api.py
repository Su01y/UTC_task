from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)


def test_schedule():
    response = client.post("/schedule")
    assert response.status_code == 200
    assert response.json() == {"message": "Mailing is planned!"}
