from sqlalchemy.orm import Session
from app.models.user import User


class UserDAL:
    def __init__(self, db: Session):
        self.db = db

    def create_user(
        self,
        username: str,
        password: str,
        name: str = None,
        age: int = None,
        email: str = None,
        phone: str = None,
        address: str = None,
    ):
        user = User(
            username=username,
            password=password,
            name=name,
            age=age,
            email=email,
            phone=phone,
            address=address,
            role="active",
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_email(self, email:str):
        return self.db.query(User).filter(User.email == email).first()
    
    def get_user_by_username(self, username: str):
        return self.db.query(User).filter(User.username == username).first()

    def get_user_by_id(self, id: int):
        return self.db.query(User).filter(User.id == id).first()

    def contains(self, username: str):
        return self.db.query(User).filter(User.username == username).first() is not None

    def set_password(self, id: int, new_password: str):
        user = self.get_user_by_id(id)
        if not user:
            return None
        user.password = new_password
        self.db.commit()
        self.db.refresh(user)
        return user

    def promote(self, username: str):
        user = self.get_user_by_username(username=username)
        if not user:
            return None
        user.role = "admin"
        self.db.commit()
        self.db.refresh(user)
        return user

    def set_user_info(
        self, id: int, name: str, age: str, email: str, phone: str, address: str
    ):
        user = self.get_user_by_id(id)
        if not user:
            return None
        user.name = name
        user.age = age
        user.email = email
        user.phone = phone
        user.address = address
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_users(self):
        return self.db.query(User).all()

    def delete_user(self, username: str):
        user = self.get_user_by_username(username=username)
        self.db.delete(user)
        self.db.commit()
        return {"state": "success", "message": "User is deleted", "username": username}
