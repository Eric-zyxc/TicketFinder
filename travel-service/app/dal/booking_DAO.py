from sqlalchemy.orm import Session
from app.models.user import User
from app.models.hotel import Hotel
from app.models.flight import Flight
from app.models.hotel_booking import HotelBooking
from app.models.flight_booking import FlightBooking
from app.models.attraction import Attraction
from app.models.attraction_booking import AttractionBooking


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

    def get_attraction_booking_by_id(self, id: int):
        booking = (
            self.db.query(AttractionBooking).filter(AttractionBooking.id == id).first()
        )
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

    def get_hotel_by_third_party_id(self, third_party_id: int):
        hotel = (
            self.db.query(Hotel).filter(Hotel.third_party_id == third_party_id).first()
        )
        return hotel

    def post_hotel(self, hotel: Hotel):
        self.db.add(hotel)
        self.db.commit()
        self.db.refresh(hotel)
        return hotel

    def get_attraction_by_third_party_id(self, third_party_id: str):
        attraction = (
            self.db.query(Attraction)
            .filter(Attraction.third_party_id == third_party_id)
            .first()
        )
        return attraction

    def post_attraction(self, attraction: Attraction):
        self.db.add(attraction)
        self.db.commit()
        self.db.refresh(attraction)
        return attraction

    def post_attraction_booking(self, attraction_booking: AttractionBooking):
        self.db.add(attraction_booking)
        self.db.commit()
        self.db.refresh(attraction_booking)
        return attraction_booking

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

    def delete_attraction_booking(self, booking: AttractionBooking) -> bool:
        try:
            self.db.delete(booking)
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

    def get_attraction_bookings_by_user_id(self, user_id: int):
        return (
            self.db.query(AttractionBooking)
            .filter(AttractionBooking.owner_id == user_id)
            .all()
        )

    def get_hotel_bookings_by_user_id(self, user_id: int):
        return (
            self.db.query(HotelBooking).filter(HotelBooking.owner_id == user_id).all()
        )

    def get_flight_bookings_by_user_id(self, user_id: int):
        return (
            self.db.query(FlightBooking).filter(FlightBooking.owner_id == user_id).all()
        )
