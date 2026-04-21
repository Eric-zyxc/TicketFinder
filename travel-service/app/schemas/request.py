from pydantic import BaseModel
from datetime import date
from decimal import Decimal


class HotelBookingRequest(BaseModel):
    owner_id: int
    hotel_id: int
    agent_id: int
    check_in: date
    check_out: date
    price: Decimal


class FlightBookingRequest(BaseModel):
    owner_id: int
    flight_id: int
    agent_id: int
    cabin_class: str
    adult: int = 0
    children: int = 0
    price: Decimal
