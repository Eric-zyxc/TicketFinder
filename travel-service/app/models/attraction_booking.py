from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey, DateTime, DECIMAL
from app.core.database import Base
from datetime import datetime
from decimal import Decimal


class AttractionBooking(Base):
    __tablename__ = "attraction_bookings"

    id: Mapped[int] = mapped_column(primary_key=True)

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    attraction_id: Mapped[int] = mapped_column(ForeignKey("attractions.id"), nullable=False)
    agent_id: Mapped[int] = mapped_column(ForeignKey("agents.id"), nullable=False)
    time_slot_id: Mapped[str | None] = mapped_column(String(150))
    offer_id: Mapped[str | None] = mapped_column(String(100))
    offer_item_id: Mapped[str | None] = mapped_column(String(150))
    start_time: Mapped[datetime | None] = mapped_column(DateTime)
    language: Mapped[str | None] = mapped_column(String(20))
    price: Mapped[Decimal | None] = mapped_column(DECIMAL(10, 2))
    currency: Mapped[str] = mapped_column(String(10), nullable=False)
    state: Mapped[str] = mapped_column(String(30), default="booked")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)