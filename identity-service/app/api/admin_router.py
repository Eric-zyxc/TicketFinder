from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.core.database import connect_db
import app.schemas.request as request
from app.service.user_service import UserService
from app.service.admin_service import AdminService
from app.models.user import User
from app.service.auth import get_current_user
from app.service.auth import create_access_token

admin_router = APIRouter()


@admin_router.post("/promote")
def promote_user(
    data: request.GeneralUsernameRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(connect_db),
):
    admin_service = AdminService(db)
    return admin_service.promote(current_user, data.username)
