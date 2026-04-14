from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_marketing_strategy():
    response = client.post("/marketing/strategy?niche=Fitness")
    assert response.status_code == 200
    data = response.json()
    assert "strategy_name" in data
    assert "Fitness" in data["strategy_name"]
    assert "channels" in data

def test_customer_support():
    query_data = {"query": "Where is my order?"}
    response = client.post("/customer/support", json=query_data)
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert "Where is my order?" in data["response"]

def test_seller_optimize():
    product_data = {
        "title": "Yoga Mat",
        "price": "$29.99",
        "description": "High quality yoga mat"
    }
    response = client.post("/seller/optimize", json=product_data)
    assert response.status_code == 200
    data = response.json()
    assert "suggested_price_adjustment" in data
    assert "seo_keywords" in data
    assert "image_optimization_tips" in data
