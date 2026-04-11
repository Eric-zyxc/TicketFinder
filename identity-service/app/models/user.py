from sqlalchemy import Column, Integer, String
from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(30), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    name = Column(String(30), nullable=True)
    age = Column(Integer, nullable=True)
    address = Column(String(100), nullable=True)
    note = Column(String(500), nullable=True)
    phone = Column(String(30), nullable=True)
    email = Column(String(100), nullable=True)
    role = Column(String(30), nullable=False)
