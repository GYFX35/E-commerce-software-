from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_get_shipments():
    response = client.get("/logistics/shipments")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "coords" in data[0]

def test_analyze_image():
    payload = {"image_data": "data:image/jpeg;base64,mockdata"}
    response = client.post("/media/analyze-image", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "detected_objects" in data
    assert "barcode_value" in data
