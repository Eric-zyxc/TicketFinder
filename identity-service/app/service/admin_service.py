from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.dal.user_dal import UserDAL
from app.service.password_validator import PasswordValidator
from app.models.user import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AdminService:
    def __init__(self, db: Session):
        self.user_dal = UserDAL(db)

    def promote(self, current_user: User, username: str):
        cur_user = self.user_dal.get_user_by_id(current_user.id)
        if cur_user.role == "super_admin":
            return {"state": "fail", "message": "you are not super admin"}

        if not self.user_dal.contains(username=username):
            return {"state": "fail", "message": "cannot find user"}

        return self.user_dal.promote(username=username)
