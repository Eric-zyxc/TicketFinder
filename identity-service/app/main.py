from fastapi import FastAPI
from app.api.user_router import user_router
from app.api.admin_router import admin_router

identity_service = FastAPI()

identity_service.include_router(user_router)
identity_service.include_router(admin_router)


@identity_service.get("/")
def root():
    return {"message": "The system is running"}


@identity_service.get("/admin/sys_info")
def get_sys_info():
    return {
        "application name": "Ticket Finder",
        "python version": "3.10.20",
        "fastapi version": "0.0.24",
        "database": "postgres (PostgreSQL) 18.3",
        "uvicorn": "uvicorn 0.42.0 with CPython 3.10.20 on Darwin",
    }