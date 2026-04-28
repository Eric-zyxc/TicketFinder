from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import connect_db
import app.schemas.request as request
from app.service.admin_service import AdminService
from app.models.user import User
from app.service.auth import get_current_user
import platform
import sys
from datetime import datetime
import fastapi
import sqlalchemy
import uvicorn
from fastapi import Depends
from sqlalchemy import text

admin_router = APIRouter(prefix="/admin", tags=["system admin"])


@admin_router.post("/promote")
def promote_user(
    data: request.GeneralUsernameRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(connect_db),
):
    admin_service = AdminService(db)
    return admin_service.promote(current_user, data.username)


@admin_router.get("/get_users")
def get_users(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(connect_db),
):
    admin_service = AdminService(db)
    return admin_service.get_users(current_user=current_user)


@admin_router.get("/get_user/{target_username}")
def get_user_by_username(
    target_username: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(connect_db),
):
    admin_service = AdminService(db=db)
    return admin_service.get_user_by_username(
        current_user=current_user, target_username=target_username
    )


@admin_router.delete("/delete_user/{target_username}")
def delete_user(
    target_username: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(connect_db),
):
    admin_service = AdminService(db=db)
    return admin_service.delete_user(
        current_user=current_user, target_username=target_username
    )


@admin_router.get("/get_user_count")
def get_user_count(
    current_user: User = Depends(get_current_user), db: Session = Depends(connect_db)
):
    admin_service = AdminService(db=db)
    return admin_service.get_user_count(current_user=current_user)


@admin_router.get("/sys_info")
def get_sys_info(db: Session = Depends(connect_db)):
    """
    System information and DB health check
    """
    try:
        db.execute(text("SELECT 1"))
        db_status = "ok"
    except Exception as e:
        db_status = f"fail: {str(e)}"

    return {
        "application": {
            "name": "Ticket Finder",
            "environment": "dev",
        },
        "system": {
            "os": platform.system(),
            "os_version": platform.release(),
            "architecture": platform.machine(),
        },
        "runtime": {
            "python_version": sys.version,
            "time_utc": datetime.utcnow().isoformat(),
        },
        "dependencies": {
            "fastapi": fastapi.__version__,
            "sqlalchemy": sqlalchemy.__version__,
            "uvicorn": uvicorn.__version__,
        },
        "database": {
            "type": "PostgreSQL",
            "status": db_status,
        },
    }
