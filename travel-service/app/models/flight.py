from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, DateTime, DECIMAL
from app.core.database import Base
from datetime import datetime
from decimal import Decimal


class Flight(Base):
    __tablename__ = "flights"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    flight_number: Mapped[str] = mapped_column(String(30), nullable=False)
    airline: Mapped[str | None] = mapped_column(String(50))
    origin_airport: Mapped[str | None] = mapped_column(String(10))
    destination_airport: Mapped[str | None] = mapped_column(String(10))
    departure_time: Mapped[datetime | None] = mapped_column(DateTime)
    arrival_time: Mapped[datetime | None] = mapped_column(DateTime)
    duration: Mapped[int | None] = mapped_column(Integer)
    price: Mapped[Decimal | None] = mapped_column(DECIMAL(10, 2))