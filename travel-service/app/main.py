from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.booking_router import booking_router
from app.api.searching_router import searching_router

travel_service = FastAPI()
travel_service.include_router(booking_router)
travel_service.include_router(searching_router)

travel_service.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@travel_service.get("/")
def root():
    """
    Check for the running status of the system
    """
    
    return "System is running"
