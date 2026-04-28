from pydantic import BaseModel
from datetime import date
from decimal import Decimal
from typing import Optional
from datetime import datetime


class HotelBookingRequest(BaseModel):
    # -------- hotel --------
    third_party_id: int
    name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    main_photo: Optional[str] = None
    sub_photo_1: Optional[str] = None
    sub_photo_2: Optional[str] = None
    sub_photo_3: Optional[str] = None
    review_score: Optional[float] = None
    review_score_word: Optional[str] = None
    review_count: Optional[int] = None
    property_class: Optional[int] = None
    # -------- booking --------
    owner_id: int
    agent_id: int
    checkin_date: date
    checkout_date: date
    price: Decimal
    currency: str
    excluded_price: Optional[Decimal] = None


class FlightBookingRequest(BaseModel):
    owner_id: int
    agent_id: int
    cabin_class: str
    adult: int = 0
    children: int = 0
    token: str
    airline_name: str | None = None
    airline_code: str | None = None
    airline_logo: str | None = None
    departure_airport: str | None = None
    departure_city: str | None = None
    arrival_airport: str | None = None
    arrival_city: str | None = None
    departure_time: datetime | None = None
    arrival_time: datetime | None = None
    duration_seconds: int | None = None
    stops: int | None = None
    price: Decimal | None = None
    currency: str | None = None


class HotelSearchRequest(BaseModel):
    dest_id: int
    search_type: str = "CITY"
    arrival_date: date
    departure_date: date
    price_min: Optional[int] = 0
    price_max: Optional[int] = 10000


class SearchFlightsRequest(BaseModel):
    from_id: str
    to_id: str
    departure_date: date
    adults: int
    children: str


class AttractionBookingRequest(BaseModel):
    # -------- attraction info --------
    third_party_id: str
    slug: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    short_description: Optional[str] = None
    operator: Optional[str] = None
    city: Optional[str] = None
    departure_address: Optional[str] = None
    arrival_address: Optional[str] = None
    primary_photo: Optional[str] = None
    free_cancellation: Optional[bool] = None
    sub_photo_1: Optional[str] = None
    sub_photo_2: Optional[str] = None
    sub_photo_3: Optional[str] = None
    languages: Optional[list[str]] = None
    whats_included: Optional[list[str]] = None
    not_included: Optional[list[str]] = None

    # -------- booking info --------
    owner_id: int
    agent_id: int
    time_slot_id: Optional[str] = None
    offer_id: Optional[str] = None
    offer_item_id: Optional[str] = None
    start_time: Optional[datetime] = None
    language: Optional[str] = None
    price: Decimal
    currency: str
