from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from routers import plant_detail, watering_schedules

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.environ.get("CORS_HOST", "http://localhost:3000")
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/launch-details")
def launch_details():
    return {
        "launch_details": {
            "module": 3,
            "week": 17,
            "day": 5,
            "hour": 19,
            "min": "00"
        }
    }

app.include_router(plant_detail.router)
app.include_router(watering_schedules.router)
