import random
from typing import Dict, Any, List

class SecurityService:
    def __init__(self):
        self.risk_levels = ["Low", "Medium", "High", "Critical"]

    def scan_product(self, product_url: str) -> Dict[str, Any]:
        """Simulates scanning a product page for security issues or scams."""
        # Mock scanning logic
        threats_found = random.randint(0, 3)
        risk_score = random.randint(0, 100)

        if risk_score < 30:
            level = "Low"
        elif risk_score < 60:
            level = "Medium"
        elif risk_score < 85:
            level = "High"
        else:
            level = "Critical"

        return {
            "url": product_url,
            "risk_level": level,
            "risk_score": risk_score,
            "threats_found": threats_found,
            "findings": [
                "SSL certificate valid" if random.random() > 0.1 else "Invalid SSL certificate",
                "Trusted seller domain" if random.random() > 0.2 else "Suspicious seller domain",
                "Secure checkout detected" if random.random() > 0.1 else "Insecure checkout process"
            ][:threats_found + 1]
        }

    def verify_supplier(self, supplier_name: str) -> Dict[str, Any]:
        """Checks the reliability and security background of a supplier."""
        reliability_score = random.randint(40, 99)
        verified = reliability_score > 70

        return {
            "supplier_name": supplier_name,
            "verified": verified,
            "reliability_score": f"{reliability_score}%",
            "security_rating": random.choice(["A", "B", "C", "D"]),
            "last_audit": "2023-10-15"
        }

    def run_store_audit(self) -> Dict[str, Any]:
        """Performs a security audit of the current store configuration."""
        issues = [
            {"issue": "Unrestricted CORS policy", "severity": "Medium", "fix": "Restrict allow_origins in FastAPI"},
            {"issue": "Default admin credentials", "severity": "Critical", "fix": "Change default passwords immediately"},
            {"issue": "Outdated dependencies", "severity": "Low", "fix": "Run pip install --upgrade -r requirements.txt"},
            {"issue": "Missing HTTP Security Headers", "severity": "Medium", "fix": "Add Secure Header middleware"}
        ]

        selected_issues = random.sample(issues, random.randint(1, 4))

        return {
            "audit_date": "2023-11-20",
            "overall_health": "75/100",
            "detected_issues": selected_issues,
            "recommendation": "Address critical and medium issues immediately to ensure data safety."
        }
