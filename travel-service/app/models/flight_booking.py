from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, DECIMAL, ForeignKey
from app.core.database import Base
from datetime import datetime
from decimal import Decimal


class FlightBooking(Base):
    __tablename__ = "flight_bookings"

    id: Mapped[int] = mapped_column(primary_key=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    agent_id: Mapped[int] = mapped_column(ForeignKey("agents.id"), nullable=False)
    flight_id: Mapped[int] = mapped_column(ForeignKey("flights.id"), nullable=False)
    cabin_class: Mapped[str | None] = mapped_column(String(20))
    adult: Mapped[int] = mapped_column(Integer, nullable=False)
    children: Mapped[str | None] = mapped_column(String(50))
    price: Mapped[Decimal | None] = mapped_column(DECIMAL(10, 2))
    currency: Mapped[str] = mapped_column(String(10), nullable=False)
    state: Mapped[str] = mapped_column(String(30), default="booked")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
