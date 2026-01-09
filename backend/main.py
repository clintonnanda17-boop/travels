from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient

app = FastAPI(title="Azuri Travels API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection
client = MongoClient("mongodb://mongodb:27017")
db = client.azuri_travels

@app.get("/")
def home():
    return {"message": "Azuri Travels API", "status": "running"}

@app.get("/health")
def health():
    try:
        client.admin.command('ping')
        return {"status": "healthy", "database": "connected"}
    except:
        return {"status": "unhealthy", "database": "disconnected"}

@app.get("/api/tours")
def get_tours():
    tours = list(db.tours.find({}, {"_id": 0}).limit(10))
    return {"tours": tours, "count": len(tours)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
