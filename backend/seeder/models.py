import os
from pydantic import BaseModel
from typing import List

class ItineraryItem(BaseModel):
    day: str
    description: str
    accommodation: str
    meals: str

class Tour(BaseModel):
    title: str
    slug: str
    description: str
    duration_days: int
    price_usd: float
    image_url: str
    category: str
    highlights: List[str]
    included: List[str]
    itinerary: List[ItineraryItem]
