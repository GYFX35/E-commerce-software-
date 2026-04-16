import random
import datetime
from typing import Dict, Any, List

class POSService:
    def __init__(self):
        self.supported_providers = ["NCR", "Revel", "Lightspeed", "Square", "Toast", "Shopline"]
        self.connections = {}  # Mock storage for active connections

    def connect(self, provider: str, credentials: Dict[str, str]) -> Dict[str, Any]:
        """Simulates connecting to a POS provider's API."""
        if provider not in self.supported_providers:
            return {"status": "error", "message": f"Unsupported provider: {provider}"}

        # Mock successful connection
        self.connections[provider] = {
            "connected": True,
            "last_sync": None,
            "status": "Active"
        }
        return {"status": "success", "message": f"Successfully connected to {provider} POS."}

    def sync_inventory(self, provider: str) -> Dict[str, Any]:
        """Simulates syncing inventory from a POS system to the e-commerce platform."""
        if provider not in self.connections:
            return {"status": "error", "message": f"No active connection for {provider}"}

        # Mock sync logic
        items_synced = random.randint(50, 200)
        self.connections[provider]["last_sync"] = datetime.datetime.now().isoformat()

        return {
            "status": "success",
            "provider": provider,
            "items_synced": items_synced,
            "timestamp": self.connections[provider]["last_sync"]
        }

    def get_sales_data(self, provider: str) -> Dict[str, Any]:
        """Simulates fetching real-time sales data from a POS provider."""
        if provider not in self.connections:
            return {"status": "error", "message": "Connection required"}

        return {
            "provider": provider,
            "daily_revenue": round(random.uniform(500, 5000), 2),
            "transactions_count": random.randint(20, 100),
            "top_selling_item": random.choice(["Coffee", "Burger", "T-Shirt", "Wireless Buds"])
        }

    def get_all_connections(self) -> List[Dict[str, Any]]:
        """Returns the status of all POS integrations."""
        results = []
        for provider in self.supported_providers:
            status = self.connections.get(provider, {"connected": False, "status": "Disconnected", "last_sync": "Never"})
            results.append({
                "provider": provider,
                **status
            })
        return results
