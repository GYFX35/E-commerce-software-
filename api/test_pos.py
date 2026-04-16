from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_get_pos_status():
    response = client.get("/pos/status")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    providers = [item["provider"] for item in data]
    assert "Square" in providers
    assert "Toast" in providers
    assert "NCR" in providers

def test_connect_pos_success():
    payload = {
        "provider": "Square",
        "api_key": "test_key",
        "merchant_id": "merchant_123"
    }
    response = client.post("/pos/connect", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_connect_pos_invalid_provider():
    payload = {
        "provider": "InvalidPOS",
        "api_key": "test_key"
    }
    response = client.post("/pos/connect", json=payload)
    assert response.status_code == 400

def test_sync_pos_flow():
    # Connect first
    client.post("/pos/connect", json={"provider": "Toast", "api_key": "key"})

    # Sync
    response = client.post("/pos/sync/Toast")
    assert response.status_code == 200
    data = response.json()
    assert data["provider"] == "Toast"
    assert "items_synced" in data

def test_sync_pos_not_connected():
    response = client.post("/pos/sync/NCR")
    assert response.status_code == 404

def test_get_sales_data():
    # Connect first
    client.post("/pos/connect", json={"provider": "Shopline", "api_key": "key"})

    # Get sales
    response = client.get("/pos/sales/Shopline")
    assert response.status_code == 200
    data = response.json()
    assert "daily_revenue" in data
    assert "top_selling_item" in data
