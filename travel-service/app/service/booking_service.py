from sqlalchemy.orm import Session
from app.models.user import User
from app.dal.booking_DAO import BookingDAO
from datetime import date
from decimal import Decimal
from app.models.hotel_booking import HotelBooking
from app.models.flight_booking import FlightBooking
from app.models.flight import Flight
from app.models.hotel import Hotel
from app.models.attraction import Attraction
from app.models.attraction_booking import AttractionBooking
import app.schemas.request as request


class BookingService:
    def __init__(self, db: Session):
        self.booking_dal = BookingDAO(db)

    def book_hotel(self, data: request.HotelBookingRequest):
        saved_hotel = self.booking_dal.get_hotel_by_third_party_id(
            third_party_id=data.third_party_id
        )
        if saved_hotel is None:
            new_hotel = Hotel(
                third_party_id=data.third_party_id,
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
        saved_flight = self.booking_dal.get_flight_by_token(data.token)
        if saved_flight is None:
            new_flight = Flight(
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
            saved_flight = self.booking_dal.post_flight(flight=new_flight)
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

    def book_attraction(self, data: request.AttractionBookingRequest):
        saved_attraction = self.booking_dal.get_attraction_by_third_party_id(
            third_party_id=data.third_party_id
        )
        if saved_attraction is None:
            new_attraction = Attraction(
                third_party_id=data.third_party_id,
                slug=data.slug,
                name=data.name,
                description=data.description,
                short_description=data.short_description,
                operator=data.operator,
                city=data.city,
                departure_address=data.departure_address,
                arrival_address=data.arrival_address,
                free_cancellation=data.free_cancellation,
                primary_photo=data.primary_photo,
                sub_photo_1=data.sub_photo_1,
                sub_photo_2=data.sub_photo_2,
                sub_photo_3=data.sub_photo_3,
                languages=",".join(data.languages) if data.languages else None,
                whats_included=(
                    "|".join(data.whats_included) if data.whats_included else None
                ),
                not_included="|".join(data.not_included) if data.not_included else None,
            )

            saved_attraction = self.booking_dal.post_attraction(
                attraction=new_attraction
            )
        attraction_booking = AttractionBooking(
            owner_id=data.owner_id,
            attraction_id=saved_attraction.id,
            agent_id=data.agent_id,
            time_slot_id=data.time_slot_id,
            offer_id=data.offer_id,
            offer_item_id=data.offer_item_id,
            start_time=data.start_time,
            language=data.language,
            price=data.price,
            currency=data.currency,
        )
        booking = self.booking_dal.post_attraction_booking(attraction_booking)
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
            return {"state": "fail", "result": "flight booking not found"}
        success = self.booking_dal.delete_flight_booking(booking)
        if not success:
            return {"state": "fail", "result": "delete failed"}
        return {"state": "success", "result": f"flight booking {booking_id} deleted"}

    def delete_attraction_booking(self, booking_id: int):
        booking = self.booking_dal.get_attraction_booking_by_id(booking_id)
        if booking is None:
            return {"state": "fail", "result": "attraction booking not found"}
        success = self.booking_dal.delete_attraction_booking(booking)
        if not success:
            return {"state": "fail", "result": "delete failed"}
        return {"state": "success", "result": f"attraction booking {booking_id} deleted"}

    def get_attraction_bookings_by_user_id(self, user_id: int):
        bookings = self.booking_dal.get_attraction_bookings_by_user_id(user_id=user_id)
        if bookings is None:
            return {"state": "fail", "result": "failed to fetch attraction bookings"}
        return bookings

    def get_hotel_bookings_by_user_id(self, user_id: int):
        bookings = self.booking_dal.get_hotel_bookings_by_user_id(user_id=user_id)
        if bookings is None:
            return {"state": "fail", "result": "failed to fetch hotel bookings"}
        return bookings

    def get_flight_bookings_by_user_id(self, user_id: int):
        bookings = self.booking_dal.get_flight_bookings_by_user_id(user_id=user_id)
        if bookings is None:
            return {"state": "fail", "result": "failed to fetch flight bookings"}
        return bookings
