from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_security_scan():
    response = client.post("/security/scan", json={"url": "https://example.com/test"})
    assert response.status_code == 200
    data = response.json()
    assert "risk_level" in data
    assert "findings" in data

def test_verify_supplier():
    response = client.post("/security/verify-supplier", json={"supplier_name": "Test Supplier"})
    assert response.status_code == 200
    data = response.json()
    assert "verified" in data
    assert data["supplier_name"] == "Test Supplier"

def test_security_audit():
    response = client.get("/security/audit")
    assert response.status_code == 200
    data = response.json()
    assert "detected_issues" in data

def test_ai_security_review():
    response = client.post("/security/ai-review?context=database%20security")
    assert response.status_code == 200
    data = response.json()
    assert "recommendations" in data

def test_security_headers():
    response = client.get("/")
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "DENY"
