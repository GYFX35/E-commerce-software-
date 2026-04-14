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
        "description": "Comfortable chair"
    }
    response = client.post("/analyze", json=product_data)
    assert response.status_code == 200
    data = response.json()
    assert "recommendation" in data
    assert "market_insight" in data
    assert "estimated_profit" in data
    # Mock mode should return these regions
    assert "US" in data["market_insight"] or "Global" in data["market_insight"]

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_marketing_strategy():
    response = client.post("/marketing/strategy", json={"niche": "fitness"})
    assert response.status_code == 200
    data = response.json()
    assert "target_audience" in data
    assert "channels" in data
    assert "key_message" in data

def test_customer_support():
    response = client.post("/customer/support", json={"query": "Where is my order?"})
    assert response.status_code == 200
    data = response.json()
    assert "response" in data

def test_product_optimization():
    product_data = {
        "title": "Yoga Mat",
        "price": "$29.99",
        "description": "Non-slip yoga mat"
    }
    response = client.post("/products/optimize", json=product_data)
    assert response.status_code == 200
    data = response.json()
    assert "suggested_price_adjustment" in data
    assert "seo_keywords" in data
    assert "image_optimization_tips" in data
