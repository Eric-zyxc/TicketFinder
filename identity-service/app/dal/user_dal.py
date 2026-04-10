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
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_username(self, username: str):
        return self.db.query(User).filter(User.username == username).first()

    def contains(self, username: str):
        return self.db.query(User).filter(User.username == username).first() is not None

    def set_password_by_username(self, username: str, new_password: str):
        user = self.get_user_by_username(username)
        if not user:
            return None
        user.password = new_password
        self.db.commit()
        self.db.refresh(user)
        return user

    def set_name(self, username: str, name: str):
        user = self.get_user_by_username(username)
        if not user:
            return None
        user.name = name
        self.db.commit()
        self.db.refresh(user)
        return user

    def set_age(self, username: str, age: int):
        user = self.get_user_by_username(username)
        if not user:
            return None
        user.age = age
        self.db.commit()
        self.db.refresh(user)
        return user

    def set_email(self, username: str, email: str):
        user = self.get_user_by_username(username)
        if not user:
            return None
        user.email = email
        self.db.commit()
        self.db.refresh(user)
        return user

    def set_phone(self, username: str, phone: str):
        user = self.get_user_by_username(username)
        if not user:
            return None
        user.phone = phone
        self.db.commit()
        self.db.refresh(user)
        return user

    def set_address(self, username: str, address: str):
        user = self.get_user_by_username(username)
        if not user:
            return None
        user.address = address
        self.db.commit()
        self.db.refresh(user)
        return user
