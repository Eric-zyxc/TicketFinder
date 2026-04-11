from fastapi import FastAPI
from app.api.user_router import user_router
from app.api.admin_router import admin_router

identity_service = FastAPI()

identity_service.include_router(user_router)
identity_service.include_router(admin_router)


@identity_service.get("/")
def root():
    return {"message": "The system is running"}


@identity_service.get("/version")
def get_version():
    return {"version": "v0.01", "stage": "prototype"}


@identity_service.get("/sys_info")
def get_sys_info():
    return {
        "application name": "Ticket Finder",
        "python version": "3.10.20",
        "fastapi version": "0.0.24",
        "database": "mysql Ver 9.6.0",
    }
