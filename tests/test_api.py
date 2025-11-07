from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_get_rejections_returns_data():
    resp = client.get("/rejections")
    assert resp.status_code == 200
    assert "data" in resp.json()
