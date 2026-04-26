from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, DateTime, DECIMAL
from app.core.database import Base
from datetime import datetime
from decimal import Decimal


class Flight(Base):
    __tablename__ = "flights"

    id: Mapped[int] = mapped_column(primary_key=True)

    # booking unique identification
    token: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)

    # airline company
    airline_name: Mapped[str | None] = mapped_column(String(100))
    airline_code: Mapped[str | None] = mapped_column(String(10))
    airline_logo: Mapped[str | None] = mapped_column(String(255))

    # flight info
    departure_airport: Mapped[str | None] = mapped_column(String(10))
    departure_city: Mapped[str | None] = mapped_column(String(100))
    arrival_airport: Mapped[str | None] = mapped_column(String(10))
    arrival_city: Mapped[str | None] = mapped_column(String(100))

    # time info
    departure_time: Mapped[datetime | None] = mapped_column(DateTime)
    arrival_time: Mapped[datetime | None] = mapped_column(DateTime)

    # duration/stop
    duration_seconds: Mapped[int | None] = mapped_column(Integer)
    stops: Mapped[int | None] = mapped_column(Integer)

