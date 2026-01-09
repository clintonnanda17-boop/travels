from .models import Tour
import json

sample_tours = [
    {
        "title": "Classic Kenya Safari",
        "slug": "classic-kenya-safari",
        "description": "Experience the best of Kenya's wildlife",
        "duration_days": 8,
        "price_usd": 2299.00,
        "image_url": "https://images.unsplash.com/photo-1516426122078-c23e76319801",
        "category": "Safari",
        "highlights": ["Masai Mara", "Lake Nakuru", "Amboseli"],
        "included": ["Accommodation", "Meals", "Game Drives"],
        "itinerary": [
            {
                "day": "Day 1: Nairobi",
                "description": "Arrival and orientation",
                "accommodation": "Nairobi Hotel",
                "meals": "Dinner"
            }
        ]
    }
]

def get_tours():
    return [Tour(**tour) for tour in sample_tours]
