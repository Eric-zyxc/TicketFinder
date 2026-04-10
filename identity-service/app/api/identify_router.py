from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import connect_db
import app.schemas.request as request
from app.service.user_service import UserService

router = APIRouter()


@router.post("/sign_up")
def add_user(data: request.SignUpRequest, db: Session = Depends(connect_db)):
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
def reset_password(data: request.ResetPwdRequest, db: Session = Depends(connect_db)):
    user_service = UserService(db)
    return user_service.reset_password(data.username, data.new_password)


@router.get("/user_info")
def get_user(username: str, db: Session = Depends(connect_db)):
    user_service = UserService(db)
    return user_service.get_user_info(username)


@router.post("/login")
def login(data: request.LoginRequest, db: Session = Depends(connect_db)):
    user_service = UserService(db)
    return user_service.login(data.username, data.password)
