from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Global Dropshipping AI API"}

def test_analyze_product():
    product_data = {
        "title": "Ergonomic Office Chair",
        "price": "$150.00",
        "url": "https://example.com/chair"
    }
    response = client.post("/analyze", json=product_data)
    assert response.status_code == 200
    data = response.json()
    assert "recommendation" in data
    assert "market_insight" in data
    assert "estimated_profit" in data
    assert "Ergonomic Office Chair" in data["market_insight"]

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
