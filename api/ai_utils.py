import os
import json
import re
from typing import Dict, Any, List, Optional
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

class AIAssistant:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        if self.api_key:
            try:
                self.llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=self.api_key)
            except Exception as e:
                print(f"Error initializing ChatGoogleGenerativeAI: {e}")
                self.llm = None
        else:
            self.llm = None
            print("Warning: GOOGLE_API_KEY not found. AIAssistant will run in mock mode.")

    def _parse_json_response(self, response: str, default_factory) -> Dict[str, Any]:
        """Helper to parse JSON from AI response."""
        try:
            json_match = re.search(r'\{.*\}', response, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except Exception:
            pass
        return default_factory()

    def generate_product_description(self, product_title: str) -> str:
        """Generates a high-converting e-commerce product description using LangChain."""
        if not self.llm:
            return f"Discover the excellence of {product_title}. Perfect for your daily needs, designed for global markets."

        prompt = ChatPromptTemplate.from_template(
            "Write a professional, high-converting e-commerce product description for: {product_title}. "
            "Highlight its benefits and appeal to a global audience. Return only the description text."
        )
        chain = prompt | self.llm | StrOutputParser()

        try:
            return chain.invoke({"product_title": product_title})
        except Exception as e:
            return f"Discover the excellence of {product_title}. Perfect for your daily needs, designed for global markets. (AI error: {str(e)})"

    def analyze_market_trends(self, niche: str) -> Dict[str, Any]:
        """Analyzes global trends for a specific niche using LangChain."""
        def default_trends():
            return {
                "trending_regions": ["US", "UK", "DE"],
                "growth_rate": "15% YoY",
                "competition_level": "Medium"
            }

        if not self.llm:
            return default_trends()

        prompt = ChatPromptTemplate.from_template(
            "Analyze global market trends for the niche: {niche}. "
            "Provide trending regions, estimated growth rate, and competition level. "
            "Format the output as a JSON with keys: trending_regions (list of strings), growth_rate (string), competition_level (string)."
        )
        chain = prompt | self.llm | StrOutputParser()

        try:
            response = chain.invoke({"niche": niche})
            return self._parse_json_response(response, default_trends)
        except Exception:
            return default_trends()

    def generate_marketing_strategy(self, niche: str) -> Dict[str, Any]:
        """Marketer Role: Generates a comprehensive marketing strategy."""
        def default_strategy():
            return {
                "target_audience": "Tech-savvy individuals",
                "channels": ["Instagram", "TikTok", "Facebook Ads"],
                "key_message": f"Revolutionize your life with our {niche} solutions."
            }

        if not self.llm:
            return default_strategy()

        prompt = ChatPromptTemplate.from_template(
            "Act as a professional marketer. Generate a marketing strategy for a dropshipping business in the {niche} niche. "
            "Include target_audience (string), suggested marketing channels (list of strings), and a compelling key_message (string). "
            "Format as JSON with those keys."
        )
        chain = prompt | self.llm | StrOutputParser()

        try:
            response = chain.invoke({"niche": niche})
            return self._parse_json_response(response, default_strategy)
        except Exception:
            return default_strategy()

    def handle_customer_query(self, query: str) -> str:
        """Clients Assistant Role: Responds to customer inquiries."""
        if not self.llm:
            return f"Thank you for your query regarding '{query}'. Our support team will get back to you within 24 hours."

        prompt = ChatPromptTemplate.from_template(
            "Act as a helpful customer support assistant for a global dropshipping store. "
            "Respond to the following customer inquiry: {query}"
        )
        chain = prompt | self.llm | StrOutputParser()

        try:
            return chain.invoke({"query": query})
        except Exception as e:
            return f"Thank you for your query. We are experiencing high volume but will respond soon."

    def optimize_sales_listing(self, product_details: Dict[str, Any]) -> Dict[str, Any]:
        """Products Seller Assistant Role: Provides insights to optimize product listings."""
        def default_optimization():
            return {
                "suggested_price_adjustment": "+5%",
                "seo_keywords": ["high quality", "affordable", "fast shipping"],
                "image_optimization_tips": "Ensure high-resolution images with white backgrounds."
            }

        if not self.llm:
            return default_optimization()

        prompt = ChatPromptTemplate.from_template(
            "Act as a product listing expert. Optimize the following product details for better sales: {product_details}. "
            "Provide suggested_price_adjustment (string), a list of seo_keywords (list of strings), and image_optimization_tips (string). "
            "Format as JSON with those keys."
        )
        chain = prompt | self.llm | StrOutputParser()

        try:
            response = chain.invoke({"product_details": str(product_details)})
            return self._parse_json_response(response, default_optimization)
        except Exception:
            return default_optimization()
