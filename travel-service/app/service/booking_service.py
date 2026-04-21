from sqlalchemy.orm import Session
from app.models.user import User
from app.dal.ticket_dal import TicketDAL
from datetime import date
from decimal import Decimal
from app.models.hotel_booking import HotelBooking
from app.models.flight_booking import FlightBooking


class BookingService:
    def __init__(self, db: Session):
        self.booking_dal = TicketDAL(db)

    def book_hotel(
        self,
        owner_id: int,
        hotel_id: int,
        agent_id: int,
        check_in: date,
        check_out: date,
        price: Decimal,
    ):
        hotel_booking = HotelBooking(
            owner_id=owner_id,
            hotel_id=hotel_id,
            agent_id=agent_id,
            check_in=check_in,
            check_out=check_out,
            price=price,
        )

        return self.booking_dal.post_hotel_booking(hotel_booking)

    def book_flight(
        self,
        owner_id: int,
        hotel_id: int,
        agent_id: int,
        cabin_class: str,
        adult: int,
        children: int,
        price: Decimal,
    ):

        flight_booking = FlightBooking(
            owner_id=owner_id,
            hotel_id=hotel_id,
            agent_id=agent_id,
            cabin_class=cabin_class,
            adult=adult,
            children=children,
            price=price,
        )
        
        return self.booking_dal.post_flight_booking(flight_booking)
