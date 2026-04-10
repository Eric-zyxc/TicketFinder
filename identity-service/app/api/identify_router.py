from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.core.database import connect_db
import app.schemas.request as request
from app.service.user_service import UserService
from app.models.user import User
from app.service.auth import get_current_user
from app.service.auth import create_access_token

router = APIRouter()


@router.post("/sign_up")
def add_user(data: request.SignUpRequest, db: Session = Depends(connect_db)):
    """
    Usage:\n
        sign up api, use to create a new account\n
    Args:\n
        sign up request from\n
    Returns: \n
        fail: state, message\n
        success: user info\n
    """

    user_service = UserService(db)
    return user_service.sign_up(
        data.username,
        data.password,
        data.name,
        data.age,
        data.email,
        data.phone,
        data.address,
    )


@router.post("/reset_password")
def reset_password(
    data: request.ResetPwdRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(connect_db),
):
    user_service = UserService(db)
    return user_service.reset_password(current_user, data.new_password)


@router.get("/my_info")
def get_user(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(connect_db),
):
    user_service = UserService(db)
    return user_service.get_my_info(current_user)


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(connect_db),
):
    user_service = UserService(db)

    result = user_service.login(form_data.username, form_data.password)

    if result["state"] == "fail":
        return result

    access_token = create_access_token({"sub": form_data.username})

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
