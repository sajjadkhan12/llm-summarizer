from fastapi.testclient import TestClient
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from app.main import app
client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_summarize():
    response = client.post(
        "/summarize",
        json={"text": "This is a test", "max_length": 50, "min_length": 10}
    )
    assert response.status_code == 200
    assert "summary" in response.json()

