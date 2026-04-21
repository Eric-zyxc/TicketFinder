from sqlalchemy.orm import Session
from app.models.user import User
from app.models.hotel import Hotel
from app.models.flight import Flight
from app.models.hotel_booking import HotelBooking
from app.models.flight_booking import FlightBooking


class TicketDAL:
    def __init__(self, db: Session):
        self.db = db

    # getters:
    def get_hotel_by_id(self, id: int):
        hotel = self.db.query(Hotel).filter(Hotel.id == id).first()
        if not hotel:
            return {"state": "fail", "message": "Hotel is not found"}
        return {"state": "success", "data": hotel}

    def get_flight_by_id(self, id: int):
        flight = self.db.query(Flight).filter(Flight.id == id).first()
        if not flight:
            return {"state": "fail", "message": "Flight is not found"}
        return {"state": "success", "data": flight}

    def get_hotel_booking_by_id(self, id: int):
        booking = self.db.query(HotelBooking).filter(HotelBooking.id == id).first()
        if not booking:
            return {"state": "fail", "message": "Hotel booking is not found"}
        return {"state": "success", "data": booking}

    def get_flight_booking_by_id(self, id: int):
        booking = self.db.query(FlightBooking).filter(FlightBooking.id == id).first()
        if not booking:
            return {"state": "fail", "message": "Flight booking is not found"}
        return {"state": "success", "data": booking}

    # setters:
    def post_hotel_booking(self, booking: HotelBooking):
        self.db.add(booking)
        self.db.commit()
        self.db.refresh(booking)
        return {"state": "success", "data": booking}

    def post_flight_booking(self, booking: FlightBooking):
        self.db.add(booking)
        self.db.commit()
        self.db.refresh(booking)
        return {"state": "success", "data": booking}
