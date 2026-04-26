from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey, Date, DateTime, DECIMAL
from app.core.database import Base
from datetime import date, datetime
from decimal import Decimal


class HotelBooking(Base):
    __tablename__ = "hotel_bookings"

    id: Mapped[int] = mapped_column(primary_key=True)

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id"), nullable=False)
    agent_id: Mapped[int] = mapped_column(ForeignKey("agents.id"), nullable=False)

    checkin_date: Mapped[date] = mapped_column(Date, nullable=False)
    checkout_date: Mapped[date] = mapped_column(Date, nullable=False)

    price: Mapped[Decimal | None] = mapped_column(DECIMAL(10, 2))
    currency: Mapped[str] = mapped_column(String(10), nullable=False)

    state: Mapped[str] = mapped_column(String(30), default="booked")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())