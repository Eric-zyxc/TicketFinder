from fastapi import FastAPI
from app.api.user_router import user_router
from app.api.admin_router import admin_router
from fastapi.middleware.cors import CORSMiddleware

identity_service = FastAPI()


identity_service.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


identity_service.include_router(user_router)
identity_service.include_router(admin_router)


@identity_service.get("/")
def root():
    return {"message": "The system is running"}


@identity_service.get("/sys_info")
def get_sys_info():
    return {
        "application name": "Ticket Finder",
        "version" : "prototype v-0.1",
        "certificate":"N/A",
        
    }
