from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import connect_db
import app.schemas.request as request
from app.service.booking_service import BookingService

booking_router = APIRouter(prefix="/booking", tags=["Booking Service"])


@booking_router.post("/book_hotel")
def book_hotel(data: request.HotelBookingRequest, db: Session = Depends(connect_db)):
    booking_service = BookingService(db=db)
    return booking_service.book_hotel(
        data.owner_id,
        data.hotel_id,
        data.agent_id,
        data.check_in,
        data.check_out,
        data.price,
    )


@booking_router.post("/booking_flight")
def book_flight(data: request.FlightBookingRequest, db: Session = Depends(connect_db)):
    booking_service = BookingService(db=db)
    return booking_service.book_flight(data)
