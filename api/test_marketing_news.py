from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_google_ads():
    response = client.post("/marketing/google-ads", json={
        "product_name": "Test Product",
        "keywords": ["test", "product"]
    })
    assert response.status_code == 200
    data = response.json()
    assert "headline_1" in data
    assert "Test Product" in data["headline_1"]

def test_facebook_ads():
    response = client.post("/marketing/facebook-ads", json={
        "product_name": "Test Product",
        "target_audience": "Gamers"
    })
    assert response.status_code == 200
    data = response.json()
    assert "primary_text" in data
    assert "Gamers" in data["primary_text"]

def test_performance_prediction():
    response = client.post("/marketing/performance-prediction", json={
        "platform": "TikTok"
    })
    assert response.status_code == 200
    data = response.json()
    assert "estimated_ctr" in data
    assert data["platform"] == "TikTok"

def test_audience_analysis():
    response = client.post("/marketing/audience-analysis?niche=Fitness")
    assert response.status_code == 200
    data = response.json()
    assert "audience_size" in data
    assert "networking_tips" in data

def test_get_news():
    response = client.get("/news")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert "title" in data[0]

def test_news_summary():
    response = client.get("/news/1/summary")
    assert response.status_code == 200
    data = response.json()
    assert "summary" in data
    assert "Quick summary of" in data["summary"]
