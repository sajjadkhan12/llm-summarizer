from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_summarize_endpoint():
    payload = {
        "text": "This is a long text about machine learning and AI. It covers various topics.",
        "max_length": 50,
        "min_length": 10
    }
    response = client.post("/summarize", json=payload)
    assert response.status_code == 200
    assert "summary" in response.json()
    assert len(response.json()["summary"]) > 0