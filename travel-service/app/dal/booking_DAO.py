from sqlalchemy.orm import Session
from app.models.user import User
from app.models.hotel import Hotel
from app.models.flight import Flight
from app.models.hotel_booking import HotelBooking
from app.models.flight_booking import FlightBooking


class BookingDAO:
    def __init__(self, db: Session):
        self.db = db

    # getters:
    def get_hotel_by_id(self, id: int):
        hotel = self.db.query(Hotel).filter(Hotel.id == id).first()
        return hotel

    def get_flight_by_id(self, id: int):
        flight = self.db.query(Flight).filter(Flight.id == id).first()
        return flight

    def get_hotel_booking_by_id(self, id: int):
        booking = self.db.query(HotelBooking).filter(HotelBooking.id == id).first()
        return booking

    def get_flight_booking_by_id(self, id: int):
        booking = self.db.query(FlightBooking).filter(FlightBooking.id == id).first()
        return booking

    # setters:
    def post_hotel_booking(self, booking: HotelBooking):
        self.db.add(booking)
        self.db.commit()
        self.db.refresh(booking)
        return booking

    def post_flight_booking(self, flight_booking: FlightBooking):
        self.db.add(flight_booking)
        self.db.commit()
        self.db.refresh(flight_booking)
        return flight_booking

    def post_flight(self, flight: Flight):
        self.db.add(flight)
        self.db.commit()
        self.db.refresh(flight)
        return flight

    def get_flight_by_token(self, token: str):
        flight = self.db.query(Flight).filter(Flight.token == token).first()
        return flight

    def get_hotel_by_hotel_id(self, hotel_id: int):
        hotel = self.db.query(Hotel).filter(Hotel.hotel_id == hotel_id).first()
        return hotel

    def post_hotel(self, hotel: Hotel):
        self.db.add(hotel)
        self.db.commit()
        self.db.refresh(hotel)
        return hotel

    def delete_hotel_booking(self, booking: HotelBooking) -> bool:
        try:
            self.db.delete(booking)
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

    def delete_flight_booking(self, booking: FlightBooking) -> bool:
        try:
            self.db.delete(booking)
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False
