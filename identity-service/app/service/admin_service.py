from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.dal.user_DAO import UserDAO
from app.models.user import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AdminService:
    def __init__(self, db: Session):
        self.user_dal = UserDAO(db)

    def promote(self, current_user: User, username: str):
        cur_user = self.user_dal.get_user_by_id(current_user.id)
        if not self.permission_validation(cur_user, ["super_admin"]):
            return {"state": "fail", "message": "you are not super admin"}

        if not self.user_dal.contains(username=username):
            return {"state": "fail", "message": "cannot find user"}

        return self.user_dal.promote(username=username)

    def get_users(self, current_user: User):
        cur_user = self.user_dal.get_user_by_id(current_user.id)
        if not current_user:
            return {"state": "fail", "message": "User is not exisit"}
        if self.permission_validation(cur_user, ["super_admin", "admin"]):
            return self.user_dal.get_users()
        return {"state": "fail", "message": "Permission denied"}

    def get_user_by_username(self, current_user, target_username):
        cur_user = self.user_dal.get_user_by_id(current_user.id)
        if not current_user:
            return {"state": "fail", "message": "User is not exisit"}
        if not self.permission_validation(cur_user, ["super_admin", "admin"]):
            return {"state": "fail", "message": "Permission denied"}
        found_user = self.user_dal.get_user_by_username(target_username)
        if not found_user:
            return {"state": "fail", "message": "User is not exisit"}
        return found_user

    def permission_validation(self, current_user: User, required_role: list[str]):
        cur_user = self.user_dal.get_user_by_id(current_user.id)
        if not cur_user:
            return False
        for str in required_role:
            if str == cur_user.role:
                return True
        return False

    def delete_user(self, current_user: User, target_username: str):
        if target_username == "superadmin":
            return {"state": "fail", "message": "Super admin cannot be deleted"}
        cur_user = self.user_dal.get_user_by_id(current_user.id)
        if not cur_user:
            return {"state": "fail", "message": "User is not exisit"}
        if not self.permission_validation(
            current_user=cur_user, required_role=["admin", "super_admin"]
        ):
            return {"state": "fail", "message": "Permission denied"}

        return self.user_dal.delete_user(target_username)
    
    
