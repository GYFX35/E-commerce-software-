import json
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
from api.ai_utils import AIAssistant
from api.marketing_ai import MarketingAI
from api.news_service import NewsService
from api.pos_service import POSService
from passlib.context import CryptContext

app = FastAPI(title="Global Dropshipping AI API")

# Password hashing configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ai_assistant = AIAssistant()
marketing_ai = MarketingAI()
news_service = NewsService()
pos_service = POSService()

class ProductInfo(BaseModel):
    title: str
    price: str
    description: Optional[str] = ""

class MarketingStrategy(BaseModel):
    strategy_name: str
    channels: List[str]
    target_audience: str
    key_message: str

class CustomerQuery(BaseModel):
    query: str

class SellerInsights(BaseModel):
    suggested_price_adjustment: str
    seo_keywords: List[str]
    image_optimization_tips: str

class AnalysisResult(BaseModel):
    recommendation: str
    market_insight: str
    estimated_profit: str

class User(BaseModel):
    username: str
    password: str
    email: Optional[str] = None

class UserLogin(BaseModel):
    username: str
    password: str

class Podcast(BaseModel):
    id: int
    title: str
    description: str
    audio_url: str
    thumbnail: str

class AdRequest(BaseModel):
    product_name: str
    keywords: Optional[List[str]] = []
    target_audience: Optional[str] = "Global"

class PerformanceRequest(BaseModel):
    platform: str

class NewsItem(BaseModel):
    id: int
    title: str
    summary: str
    source: str
    date: str

class POSConnectRequest(BaseModel):
    provider: str
    api_key: str
    merchant_id: Optional[str] = None

class POSSyncResponse(BaseModel):
    status: str
    provider: str
    items_synced: int
    timestamp: str

class POSStatusResponse(BaseModel):
    provider: str
    connected: bool
    status: str
    last_sync: Optional[str] = None

# Data Persistence (Simple JSON files for MVP)
USERS_FILE = "users.json"
PRODUCTS_FILE = "products_data.json"

def load_data(file_path, default=[]):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return default

def save_data(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Global Dropshipping AI API"}

@app.post("/analyze", response_model=AnalysisResult)
async def analyze_product(product: ProductInfo):
    # Use the AI assistant to generate insights
    trends = ai_assistant.analyze_market_trends(product.title)

    recommendation = "High Potential" if trends['growth_rate'] > "10% YoY" else "Moderate Potential"
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

@app.post("/marketing/strategy", response_model=MarketingStrategy)
async def get_marketing_strategy(niche: str):
    """Marketer Role Endpoint"""
    return ai_assistant.generate_marketing_strategy(niche)

@app.post("/customer/support")
async def handle_customer_support(query: CustomerQuery):
    """Clients Assistant Role Endpoint"""
    response = ai_assistant.handle_customer_query(query.query)
    return {"response": response}

@app.post("/seller/optimize", response_model=SellerInsights)
async def get_seller_insights(product: ProductInfo):
    """Products Seller Assistant Role Endpoint"""
    return ai_assistant.optimize_sales_listing(product.model_dump())

# Authentication Endpoints
@app.post("/register")
async def register(user: User):
    users = load_data(USERS_FILE)
    if any(u['username'] == user.username for u in users):
        raise HTTPException(status_code=400, detail="Username already registered")

    # Hash the password before storing
    hashed_password = pwd_context.hash(user.password)
    user_dict = user.model_dump()
    user_dict['password'] = hashed_password

    users.append(user_dict)
    save_data(USERS_FILE, users)
    return {"message": "User registered successfully"}

@app.post("/login")
async def login(user: UserLogin):
    users = load_data(USERS_FILE)
    found_user = next((u for u in users if u['username'] == user.username), None)

    if not found_user or not pwd_context.verify(user.password, found_user['password']):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {"message": "Login successful", "username": user.username}

# Product Submission Endpoints
@app.post("/products")
async def submit_product(product: ProductInfo):
    products = load_data(PRODUCTS_FILE)
    new_product = product.model_dump()
    new_product['id'] = len(products) + 1
    products.append(new_product)
    save_data(PRODUCTS_FILE, products)
    return {"message": "Product submitted successfully", "product": new_product}

@app.get("/products", response_model=List[ProductInfo])
async def get_products():
    return load_data(PRODUCTS_FILE)

# Podcast Endpoints
@app.get("/podcasts", response_model=List[Podcast])
async def get_podcasts():
    # Mock data for podcasts
    return [
        {
            "id": 1,
            "title": "E-commerce Mastery",
            "description": "Learn the secrets of scaling your online business.",
            "audio_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
            "thumbnail": "https://via.placeholder.com/150"
        },
        {
            "id": 2,
            "title": "Global Sourcing 101",
            "description": "How to find reliable suppliers worldwide.",
            "audio_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
            "thumbnail": "https://via.placeholder.com/150"
        }
    ]

# Marketing and AI Data Science Endpoints
@app.post("/marketing/google-ads")
async def generate_google_ads(request: AdRequest):
    return marketing_ai.generate_google_ads(request.product_name, request.keywords)

@app.post("/marketing/facebook-ads")
async def generate_facebook_ads(request: AdRequest):
    return marketing_ai.generate_facebook_ads(request.product_name, request.target_audience)

@app.post("/marketing/performance-prediction")
async def predict_performance(request: PerformanceRequest):
    return marketing_ai.predict_ad_performance(request.platform)

@app.post("/marketing/audience-analysis")
async def analyze_audience(niche: str):
    return marketing_ai.analyze_audience_network(niche)

# News Endpoints
@app.get("/news", response_model=List[NewsItem])
async def get_news():
    return news_service.get_latest_news()

@app.get("/news/{news_id}/summary")
async def get_news_summary(news_id: int):
    return {"summary": news_service.summarize_news(news_id)}

# POS Integration Endpoints
@app.post("/pos/connect")
async def connect_pos(request: POSConnectRequest):
    result = pos_service.connect(request.provider, {"api_key": request.api_key, "merchant_id": request.merchant_id})
    if result["status"] == "error":
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@app.post("/pos/sync/{provider}", response_model=POSSyncResponse)
async def sync_pos_inventory(provider: str):
    result = pos_service.sync_inventory(provider)
    if result["status"] == "error":
        raise HTTPException(status_code=404, detail=result["message"])
    return result

@app.get("/pos/status", response_model=List[POSStatusResponse])
async def get_pos_status():
    return pos_service.get_all_connections()

@app.get("/pos/sales/{provider}")
async def get_pos_sales(provider: str):
    result = pos_service.get_sales_data(provider)
    if "status" in result and result["status"] == "error":
        raise HTTPException(status_code=404, detail=result["message"])
    return result
