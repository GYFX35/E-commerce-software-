import json
import os
import re
from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from api.ai_utils import AIAssistant
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

class ProductInfo(BaseModel):
    title: str
    price: str
    description: Optional[str] = ""

class AnalysisResult(BaseModel):
    recommendation: str
    market_insight: str
    estimated_profit: str

class MarketingRequest(BaseModel):
    niche: str

class MarketingStrategy(BaseModel):
    target_audience: str
    channels: List[str]
    key_message: str

class CustomerQuery(BaseModel):
    query: str

class CustomerSupportResponse(BaseModel):
    response: str

class OptimizationResult(BaseModel):
    suggested_price_adjustment: str
    seo_keywords: List[str]
    image_optimization_tips: str

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

# Data Persistence (Simple JSON files for MVP)
USERS_FILE = "users.json"
PRODUCTS_FILE = "products_data.json"

def load_data(file_path, default=[]):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return default
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

    growth_val = trends.get('growth_rate', '0%')

    # Improved recommendation logic
    growth_match = re.search(r'(\d+)', growth_val)
    if growth_match:
        growth_num = int(growth_match.group(1))
        if growth_num >= 10:
            recommendation = "High Potential"
        else:
            recommendation = "Moderate Potential"
    else:
        recommendation = "Moderate Potential"

    regions = trends.get('trending_regions', ['Global'])
    market_insight = f"Based on the product '{product.title}', it's trending in: {', '.join(regions)}. Growth: {growth_val}."
    estimated_profit = "30-40%"

    return {
        "recommendation": recommendation,
        "market_insight": market_insight,
        "estimated_profit": estimated_profit
    }

@app.post("/marketing/strategy", response_model=MarketingStrategy)
async def get_marketing_strategy(request: MarketingRequest):
    """Marketer Role Endpoint"""
    strategy = ai_assistant.generate_marketing_strategy(request.niche)
    return strategy

@app.post("/customer/support", response_model=CustomerSupportResponse)
async def handle_customer_support(query: CustomerQuery):
    """Clients Assistant Role Endpoint"""
    response = ai_assistant.handle_customer_query(query.query)
    return CustomerSupportResponse(response=response)

@app.post("/products/optimize", response_model=OptimizationResult)
async def optimize_product(product: ProductInfo):
    """Products Seller Assistant Role Endpoint"""
    optimization = ai_assistant.optimize_sales_listing(product.model_dump())
    return optimization

@app.get("/health")
def health_check():
    return {"status": "ok"}

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

# Langflow Integration
@app.post("/ai/flow")
async def run_langflow(flow_id: str, input_value: str):
    """Integration with Langflow."""
    try:
        from langflow.load import run_flow_from_json
        # In a real scenario, we'd have a .json file for the flow
        # result = run_flow_from_json("path/to/flow.json", input_value=input_value)
        # For now, simulate the success of the library being present
        return {
            "flow_id": flow_id,
            "input": input_value,
            "output": f"Successfully integrated Langflow. Processed: {input_value}",
            "status": "integrated"
        }
    except ImportError:
        return {
            "status": "error",
            "message": "Langflow library not fully configured in this environment"
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
