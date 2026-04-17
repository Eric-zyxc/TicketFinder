from fastapi import FastAPI

travel_service = FastAPI()


@travel_service.get("/")
def root():
    return "System is running"
