from pydantic import BaseModel
from datetime import date
from decimal import Decimal
from typing import Optional


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


class HotelSearchRequest(BaseModel):
    dest_id: int
    search_type: str = "CITY"
    arrival_date: date
    departure_date: date
    price_min: Optional[int] = None
    price_max: Optional[int] = None
    sort_by: Optional[str] = None
    categories_filter: Optional[str] = None



class HotelDestinationRequest(BaseModel):
    query: str