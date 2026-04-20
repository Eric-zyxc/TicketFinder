from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.dal.user_dal import UserDAL
from app.service.password_validator import PasswordValidator
from app.models.user import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    def __init__(self, db: Session):
        self.user_dal = UserDAL(db)

    def sign_up(
        self,
        username: str,
        password: str,
        name: str,
        age: int,
        email: str,
        phone: str,
        address: str,
    ):
        password_validator = PasswordValidator(password)
        if not password_validator.check():  # check password
            return {"state": "fail", "message": "Password is not valid"}

        if self.user_dal.contains(username):  # user exsists
            return {"state": "fail", "message": "User exists"}

        if self.user_dal.get_user_by_email(email=email):
            return {"state": "fail", "message": "Email has already in use"}

        hashed_pwd = pwd_context.hash(password)
        new_user = self.user_dal.create_user(
            username=username,
            password=hashed_pwd,
            name=name,
            age=age,
            email=email,
            phone=phone,
            address=address,
        )  # create new user

        return {
            "state": "success",
            "message": "new user created",
            "user_id": new_user.id,
        }

    def get_info(self, username: str):
        exisiting_user = self.user_dal.get_user_by_username(username)
        if exisiting_user:
            return exisiting_user
        return {"state": "fail", "message": "Cannot find user"}

    def reset_password(self, user: User, current_password: str, new_password: str):
        target_user = self.user_dal.get_user_by_id(user.id)
        if not target_user:
            return {"state": "fail", "message": "cannot find user"}

        if not pwd_context.verify(current_password, target_user.password):
            return {"state": "fail", "message": "current password is wrong"}

        if new_password == current_password:
            return {
                "state": "fail",
                "message": "new password cannot be same as old password",
            }

        password_validator = PasswordValidator(new_password)
        if not password_validator.check():
            return {"state": "fail", "message": "Password is not valid"}

        hashed_pwd = pwd_context.hash(new_password)
        self.user_dal.set_password(user.id, hashed_pwd)
        return {
            "state": "success",
            "message": "Password updated",
        }

    def get_my_info(self, user: User):
        user = self.user_dal.get_user_by_username(user.username)
        if user:
            return self.to_dict(user)
        return {"state": "fail", "message": "Cannot find user"}

    def to_dict(self, user: User):
        res = {
            "user_id": user.id,
            "username": user.username,
            "password": user.password,
            "name": user.name,
            "age": user.age,
            "address": user.address,
            "email": user.email,
            "phone": user.phone,
            "role": user.role,
            "state": "active",
        }
        return res

    def login(self, username: str, password: str):
        target_user = self.user_dal.get_user_by_username(username)
        if not target_user:
            return {"state": "fail", "message": "Cannot find user"}

        if pwd_context.verify(password, target_user.password):
            return self.to_dict(target_user)

        return {"state": "fail", "message": "Password is not correct"}

    def logout(self, user: User):
        target_user = self.user_dal.get_user_by_id(user.id)
        if not target_user:
            return {"state": "fail", "message": "Cannot find user"}
        return {"state": "success", "message": "User logged out"}

    def set_my_info(
        self, user: User, name: str, age: int, email: str, phone: str, address: str
    ):
        if len(name) > 30:
            return {
                "state": "fail",
                "message": "name length cannot be greater than 30 characters",
            }
        if age < 0 or age > 100:
            return {"state": "fail", "message": "age is not in the accpeted range"}
        if len(email) > 100:
            return {
                "state": "fail",
                "message": "email length cannot be greater than 100 characters",
            }
        if len(phone) > 30:
            return {
                "state": "fail",
                "message": "phone number length cannot be greater than 30 characters",
            }
        if len(address) > 100:
            return {
                "state": "fail",
                "message": "address length cannot be greater than 30 characters",
            }
        self.user_dal.set_user_info(
            id=user.id, name=name, age=age, email=email, phone=phone, address=address
        )
        return self.user_dal.get_user_by_id(user.id)

    def delete_me(self, current_user):
        if current_user.username == "superadmin":
            return {"state": "fail", "message": "Super admin cannot be deleted"}
        cur_user = self.user_dal.get_user_by_id(current_user.id)
        if not cur_user:
            return {"state": "fail", "message": "Cannot find the user"}
        return self.user_dal.delete_user(cur_user.username)
