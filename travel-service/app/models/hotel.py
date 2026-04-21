from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, DECIMAL, DateTime
from app.core.database import Base
from datetime import datetime
from decimal import Decimal


class Hotel(Base):
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None] = mapped_column(String(30))
    address: Mapped[str | None] = mapped_column(String(100))
    city: Mapped[str | None] = mapped_column(String(30))
    state: Mapped[str | None] = mapped_column(String(30))
    country: Mapped[str | None] = mapped_column(String(30))
    zip_code: Mapped[str | None] = mapped_column(String(30))
    email: Mapped[str | None] = mapped_column(String(30))
    phone: Mapped[str | None] = mapped_column(String(30))
    star: Mapped[int | None] = mapped_column(Integer)
    rating: Mapped[Decimal | None] = mapped_column(DECIMAL(2, 1))
    latitude: Mapped[Decimal | None] = mapped_column(DECIMAL(10, 7))
    longitude: Mapped[Decimal | None] = mapped_column(DECIMAL(10, 7))
    created_at: Mapped[datetime | None] = mapped_column(DateTime)
