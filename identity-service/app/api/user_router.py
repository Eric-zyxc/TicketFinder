from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.core.database import connect_db
import app.schemas.request as request
from app.service.user_service import UserService
from app.models.user import User
from app.service.auth import get_current_user
from app.service.auth import create_access_token

user_router = APIRouter(tags=["For regular users"])


@user_router.post("/sign_up")
def add_user(data: request.SignUpRequest, db: Session = Depends(connect_db)):
    """
    Use:\n
        sign up api, use to create a new account\n
    Args:\n
        sign up request (form)\n
    Returns: \n
        fail: state=fail, message\n
        success: user info (json)\n
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


@user_router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(connect_db),
):
    """
    User:\n
        Login user into the system, verify authencation\n
    Args:\n
        login request (form)\n
    Return:\n
        token (JWT)\n
    """

    user_service = UserService(db)

    result = user_service.login(form_data.username, form_data.password)

    if result["state"] == "fail":
        return result

    access_token = create_access_token({"sub": form_data.username})

    return {
        "state": "success",
        "username": result["username"],
        "name": result["name"],
        "age": result["age"],
        "email": result["email"],
        "phone": result["phone"],
        "address": result["address"],
        "access_token": access_token,
        "token_type": "bearer",
        "id": result["id"],
    }


@user_router.post("/reset_password")
def reset_password(
    data: request.ResetPwdRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(connect_db),
):
    """
    Use:\n
        reset/change password\n
    Args:\n
        current user auth, new password\n
    Reture:\n
        fail: state=fail, message
        success: state=success, message
    """

    user_service = UserService(db)
    return user_service.reset_password(
        user=current_user,
        current_password=data.current_password,
        new_password=data.new_password,
    )


@user_router.post("/set_my_info")
def set_my_info(
    data: request.ChangeUserInfoRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(connect_db),
):
    """
    Use:\n
        update current user's information\n
    Args:\n
        user info request (form)\n
    Returns:\n
        fail: state=fail, message
        success: updated user information (json)
    """

    user_service = UserService(db)
    return user_service.set_my_info(
        current_user,
        name=data.name,
        age=data.age,
        email=data.email,
        phone=data.phone,
        address=data.address,
    )


@user_router.get("/me")
def get_my_info(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(connect_db),
):
    """
    Use:\n
        get the information of the current user.\n
    Args:\n
        None\n
    Returns:\n
        success: current user information (json)
    """

    user_service = UserService(db)
    return user_service.get_my_info(current_user)


@user_router.post("/logout")
def logout(
    current_user: User = Depends(get_current_user), db: Session = Depends(connect_db)
):
    user_service = UserService(db)
    return user_service.logout(current_user)


@user_router.delete("/delete_me")
def delete_me(
    current_user: User = Depends(get_current_user), db: Session = Depends(connect_db)
):
    user_service = UserService(db)
    return user_service.delete_me(current_user=current_user)
