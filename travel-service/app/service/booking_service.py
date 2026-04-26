from sqlalchemy.orm import Session
from app.models.user import User
from app.dal.booking_DAO import BookingDAO
from datetime import date
from decimal import Decimal
from app.models.hotel_booking import HotelBooking
from app.models.flight_booking import FlightBooking
from app.models.flight import Flight
from app.models.hotel import Hotel
import app.schemas.request as request


class BookingService:
    def __init__(self, db: Session):
        self.booking_dal = BookingDAO(db)

    def book_hotel(self, data: request.HotelBookingRequest):
        saved_hotel = self.booking_dal.get_hotel_by_hotel_id(hotel_id=data.hotel_id)
        if saved_hotel is None:
            new_hotel = Hotel(
                hotel_id=data.hotel_id,
                name=data.name,
                review_score=data.review_score,
                review_score_word=data.review_score_word,
                review_count=data.review_count,
                property_class=data.property_class,
                latitude=data.latitude,
                longitude=data.longitude,
                main_photo=data.main_photo,
                sub_photo_1=data.sub_photo_1,
                sub_photo_2=data.sub_photo_2,
                sub_photo_3=data.sub_photo_3,
            )
            saved_hotel = self.booking_dal.post_hotel(hotel=new_hotel)

        hotel_booking = HotelBooking(
            owner_id=data.owner_id,
            hotel_id=saved_hotel.id,
            agent_id=data.agent_id,
            checkin_date=data.checkin_date,
            checkout_date=data.checkout_date,
            price=data.price,
            currency=data.currency,
        )

        booking = self.booking_dal.post_hotel_booking(hotel_booking)
        return {"state": "success", "result": booking}

    def book_flight(
        self,
        data: request.FlightBookingRequest,
    ):
        existing_flight = self.booking_dal.get_flight_by_token(data.token)

        if existing_flight:
            saved_flight = existing_flight
        else:
            flight = Flight(
                token=data.token,
                airline_name=data.airline_name,
                airline_code=data.airline_code,
                airline_logo=data.airline_logo,
                departure_airport=data.departure_airport,
                departure_city=data.departure_city,
                arrival_airport=data.arrival_airport,
                arrival_city=data.arrival_city,
                departure_time=data.departure_time,
                arrival_time=data.arrival_time,
                duration_seconds=data.duration_seconds,
                stops=data.stops,
            )

            saved_flight = self.booking_dal.post_flight(flight=flight)
            if not saved_flight:
                return {"state": "fail", "result": "fail to add flight"}

        flight_booking = FlightBooking(
            owner_id=data.owner_id,
            flight_id=saved_flight.id,
            agent_id=data.agent_id,
            cabin_class=data.cabin_class,
            adult=data.adult,
            children=data.children,
            price=data.price,
            currency=data.currency,
        )

        booking = self.booking_dal.post_flight_booking(flight_booking=flight_booking)
        return {"state": "success", "result": booking}

    def delete_hotel_booking(self, booking_id: int):
        booking = self.booking_dal.get_hotel_booking_by_id(booking_id)
        if booking is None:
            return {"state": "fail", "result": "hotel booking not found"}
        success = self.booking_dal.delete_hotel_booking(booking)
        if not success:
            return {"state": "fail", "result": "delete failed"}
        return {"state": "success", "result": f"hotel booking {booking_id} deleted"}

    def delete_flight_booking(self, booking_id: int):
        booking = self.booking_dal.get_flight_booking_by_id(booking_id)
        if booking is None:
            return {"state": "fail", "result": "hotel booking not found"}
        success = self.booking_dal.delete_flight_booking(booking)
        if not success:
            return {"state": "fail", "result": "delete failed"}
        return {"state": "success", "result": f"flight booking {booking_id} deleted"}


