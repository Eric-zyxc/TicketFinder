from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Boolean, Text
from app.core.database import Base


class Attraction(Base):
    __tablename__ = "attractions"

    id: Mapped[int] = mapped_column(primary_key=True)

    # third-party attraction id
    third_party_id: Mapped[str] = mapped_column(
        String(100), unique=True, nullable=False
    )
    slug: Mapped[str | None] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    short_description: Mapped[str | None] = mapped_column(Text)
    operator: Mapped[str | None] = mapped_column(String(255))
    city: Mapped[str | None] = mapped_column(String(100))
    departure_address: Mapped[str | None] = mapped_column(String(255))
    arrival_address: Mapped[str | None] = mapped_column(String(255))
    free_cancellation: Mapped[bool | None] = mapped_column(Boolean)
    primary_photo: Mapped[str | None] = mapped_column(String(500))
    sub_photo_1: Mapped[str | None] = mapped_column(String(500))
    sub_photo_2: Mapped[str | None] = mapped_column(String(500))
    sub_photo_3: Mapped[str | None] = mapped_column(String(500))
    languages: Mapped[str | None] = mapped_column(Text)
    whats_included: Mapped[str | None] = mapped_column(Text)
    not_included: Mapped[str | None] = mapped_column(Text)
