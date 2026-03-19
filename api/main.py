import json
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
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

# Authentication Endpoints
@app.post("/register")
async def register(user: User):
    users = load_data(USERS_FILE)
    if any(u['username'] == user.username for u in users):
        raise HTTPException(status_code=400, detail="Username already registered")

    # Hash the password before storing
    hashed_password = pwd_context.hash(user.password)
    user_dict = user.dict()
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
    new_product = product.dict()
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
