from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from api.ai_utils import AIAssistant

app = FastAPI(title="Global Dropshipping AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

ai_assistant = AIAssistant()

class ProductInfo(BaseModel):
    title: str
    price: str
    url: str

class AnalysisResult(BaseModel):
    recommendation: str
    market_insight: str
    estimated_profit: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Global Dropshipping AI API"}

@app.post("/analyze", response_model=AnalysisResult)
async def analyze_product(product: ProductInfo):
    # Use the AI assistant to generate insights
    trends = ai_assistant.analyze_market_trends(product.title)

    # Extract numeric value for robust comparison
    growth_value = 0.0
    try:
        growth_value = float(trends['growth_rate'].split('%')[0])
    except (ValueError, KeyError, IndexError):
        pass

    recommendation = "High Potential" if growth_value > 10.0 else "Moderate Potential"
    market_insight = f"Based on the product '{product.title}', it's trending in {len(trends['trending_regions'])} global regions: {', '.join(trends['trending_regions'])}. Growth: {trends['growth_rate']}."
    estimated_profit = "35%"

    return {
        "recommendation": recommendation,
        "market_insight": market_insight,
        "estimated_profit": estimated_profit
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}
