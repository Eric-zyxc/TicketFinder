from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, Date, DECIMAL, ForeignKey
from app.core.database import Base
from datetime import datetime, date
from decimal import Decimal


class HotelBooking(Base):
    __tablename__ = "hotel_bookings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id"), nullable=False)
    agent_id: Mapped[int] = mapped_column(ForeignKey("agents.id"), nullable=False)
    booking_time: Mapped[datetime | None] = mapped_column(
        DateTime, default=datetime.now
    )
    check_in: Mapped[date] = mapped_column(Date, nullable=False)
    check_out: Mapped[date] = mapped_column(Date, nullable=False)
    price: Mapped[Decimal | None] = mapped_column(DECIMAL(10, 2))
    state: Mapped[str | None] = mapped_column(String(20), default="booked")
