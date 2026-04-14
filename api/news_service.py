from typing import List, Dict
from datetime import datetime

class NewsService:
    def __init__(self):
        self.mock_news = [
            {
                "id": 1,
                "title": "E-commerce Trends 2024: The Rise of AI in Dropshipping",
                "summary": "Artificial Intelligence is revolutionizing how dropshippers find products and manage customer service.",
                "source": "TechCommerce",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            {
                "id": 2,
                "title": "Global Shipping Updates: Port Congestions Easing",
                "summary": "Major international ports report faster turnaround times, benefiting global e-commerce businesses.",
                "source": "LogisticsDaily",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            {
                "id": 3,
                "title": "Google Ads Algorithm Update: What You Need to Know",
                "summary": "Google announces new features for Smart Shopping campaigns to improve conversion rates.",
                "source": "AdWorld",
                "date": datetime.now().strftime("%Y-%m-%d")
            }
        ]

    def get_latest_news(self) -> List[Dict]:
        """Returns the latest e-commerce news."""
        return self.mock_news

    def summarize_news(self, news_id: int) -> str:
        """Returns a summarized version of a specific news item."""
        news_item = next((item for item in self.mock_news if item["id"] == news_id), None)
        if news_item:
            return f"Quick summary of '{news_item['title']}': {news_item['summary']} Experts suggest following these developments closely."
        return "News item not found."
