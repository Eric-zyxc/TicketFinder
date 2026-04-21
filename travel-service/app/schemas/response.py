from pydantic import BaseModel, ConfigDict
from datetime import datetime
from decimal import Decimal


class HotelResponse(BaseModel):
    id: int
    name: str | None = None
    address: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None
    zip_code: str | None = None
    email: str | None = None
    phone: str | None = None
    star: int | None = None
    rating: Decimal | None = None
    latitude: Decimal | None = None
    longitude: Decimal | None = None
    created_at: datetime | None = None
    model_config = ConfigDict(from_attributes=True)


class FlightResponse(BaseModel):
    id: int
    flight_number: str
    airline: str | None = None
    origin_airport: str | None = None
    destination_airport: str | None = None
    departure_time: datetime | None = None
    arrival_time: datetime | None = None
    duration: int | None = None
    price: Decimal | None = None
    model_config = ConfigDict(from_attributes=True)


class AgentResponse(BaseModel):
    id: int
    name: str | None = None
    email: str | None = None
    phone: str | None = None
    status: str
    model_config = ConfigDict(from_attributes=True)


class FlightBookingResponse(BaseModel):
    id: int
    owner_id: int
    flight_id: int
    agent_id: int
    booking_time: datetime
    cabin_class: str | None = None
    price: Decimal | None = None
    adult: int
    children: int
    state: str
    model_config = ConfigDict(from_attributes=True)
