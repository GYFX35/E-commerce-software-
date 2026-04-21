from pydantic import BaseModel
from typing import List, Optional

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    image_url: Optional[str] = None

class Catalog(BaseModel):
    id: int
    name: str
    description: str
    product_ids: List[int]

class Campaign(BaseModel):
    id: int
    name: str
    catalog_id: int
    platform: str
    budget: float
    status: str  # e.g., Draft, Active, Completed

class TikTokAdRequest(BaseModel):
    product_name: str
    niche: str
    video_duration: int = 15
