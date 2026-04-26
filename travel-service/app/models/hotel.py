from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Float, DECIMAL
from app.core.database import Base
from decimal import Decimal


class Hotel(Base):
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(primary_key=True)

    # hotel info
    hotel_id: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    review_score: Mapped[float | None] = mapped_column(Float)
    review_score_word: Mapped[str | None] = mapped_column(String(50))
    review_count: Mapped[int | None] = mapped_column(Integer)
    property_class: Mapped[int | None] = mapped_column(Integer)

    # location info
    latitude: Mapped[float | None] = mapped_column(Float)
    longitude: Mapped[float | None] = mapped_column(Float)

    # 主图
    main_photo: Mapped[str | None] = mapped_column(String(500))
    sub_photo_1: Mapped[str | None] = mapped_column(String(500))
    sub_photo_2: Mapped[str | None] = mapped_column(String(500))
    sub_photo_3: Mapped[str | None] = mapped_column(String(500))
