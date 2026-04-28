from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import connect_db
import app.schemas.request as request
from app.service.booking_service import BookingService

booking_router = APIRouter(prefix="/book", tags=["Booking Service"])


@booking_router.post("/hotel")
def book_hotel(data: request.HotelBookingRequest, db: Session = Depends(connect_db)):
    """
    Desciption:\n
        This endpoint will take a request forms for hotel booking, and store the information to the database.\n
    """
    booking_service = BookingService(db=db)
    return booking_service.book_hotel(data=data)


@booking_router.post("/flight")
def book_flight(
    data: request.FlightBookingRequest,
    db: Session = Depends(connect_db),
):
    """
    Desciption:\n
         This endpoint will take a request forms for hotel booking, and store the information to the database.\n
    """

    booking_service = BookingService(db=db)
    return booking_service.book_flight(data=data)


@booking_router.post("/attraction")
def book_attraction(
    data: request.AttractionBookingRequest, db: Session = Depends(connect_db)
):
    """ """
    booking_service = BookingService(db=db)
    return booking_service.book_attraction(data=data)


@booking_router.delete("/delete/hotel_booking")
def delete_hotel_booking(booking_id: int, db: Session = Depends(connect_db)):
    booking_service = BookingService(db=db)
    return booking_service.delete_hotel_booking(booking_id=booking_id)


@booking_router.delete("/delete/flight_booking")
def delete_hotel_booking(booking_id: int, db: Session = Depends(connect_db)):
    booking_service = BookingService(db=db)
    return booking_service.delete_flight_booking(booking_id=booking_id)


@booking_router.delete("/delete/attraction_booking")
def delete_attraction_booking(booking_id: int, db: Session = Depends(connect_db)):
    booking_service = BookingService(db=db)
    return booking_service.delete_attraction_booking(booking_id=booking_id)


@booking_router.get("/get/attraction_booking")
def get_attraction_bookings_by_user_id(user_id: int, db: Session = Depends(connect_db)):
    booking_service = BookingService(db=db)
    return booking_service.get_attraction_bookings_by_user_id(user_id)


@booking_router.get("/get/hotel_booking")
def get_hotel_bookings_by_user_id(user_id: int, db: Session = Depends(connect_db)):
    booking_service = BookingService(db=db)
    return booking_service.get_hotel_bookings_by_user_id(user_id)


@booking_router.get("/get/flight_booking")
def get_flight_bookings_by_user_id(user_id: int, db: Session = Depends(connect_db)):
    booking_service = BookingService(db=db)
    return booking_service.get_flight_bookings_by_user_id(user_id)
