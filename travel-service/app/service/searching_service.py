from sqlalchemy.orm import Session
from app.dal.ticket_dal import TicketDAL
from app.client.rapidapi_client import RapidApiClient
import app.schemas.request as request
from fastapi import Depends
from app.core.database import connect_db
from app.client.rapidapi_client import get_rapidapi_client


class SearchingService:
    def __init__(self, db: Session, client: RapidApiClient):
        self.dal = TicketDAL(db=db)
        self.client = client

    def search_destination(self, query: str):
        if not query or query.strip() == "":
            return {"state": "fail", "message": "query cannot be empty"}
        result = self.client.search_destination(query=query)
        if result.get("status") is True:
            return {"state": "success", "result": result}
        return {
            "state": "fail",
            "message": result.get("message", "Search hotel failed"),
            "result": result,
        }

    def search_hotel(self, data: request.HotelSearchRequest):
        result = self.client.search_hotel(
            dest_id=data.dest_id,
            arrival_date=data.arrival_date,
            departure_date=data.departure_date,
            price_min=data.price_min,
            price_max=data.price_max,
            sort_by=data.sort_by,
            categories_filter=data.categories_filter,
        )
        if result.get("status") is False:
            return {"state": "success", "result": result}

        clean_hotels = []

        for hotel in result["data"]["hotels"]:
            prop = hotel.get("property", {})
            price_breakdown = prop.get("priceBreakdown", {})
            gross_price = price_breakdown.get("grossPrice", {})
            excluded_price = price_breakdown.get("excludedPrice", {})
            photos = prop.get("photoUrls", [])
            checkin = prop.get("checkin", {})
            checkout = prop.get("checkout", {})

            clean_hotels.append(
                {
                    "hotel_id": hotel.get("hotel_id"),
                    "name": prop.get("name"),
                    "review_score": prop.get("reviewScore"),
                    "review_score_word": prop.get("reviewScoreWord"),
                    "review_count": prop.get("reviewCount"),
                    "property_class": prop.get("propertyClass"),
                    "latitude": prop.get("latitude"),
                    "longitude": prop.get("longitude"),
                    "checkin_date": prop.get("checkinDate"),
                    "checkout_date": prop.get("checkoutDate"),
                    "checkin_from_time": checkin.get("fromTime"),
                    "checkin_until_time": checkin.get("untilTime"),
                    "checkout_from_time": checkout.get("fromTime"),
                    "checkout_until_time": checkout.get("untilTime"),
                    "gross_price": gross_price.get("value"),
                    "gross_price_currency": gross_price.get("currency"),
                    "excluded_price": excluded_price.get("value"),
                    "excluded_price_currency": excluded_price.get("currency"),
                    "main_photo": photos[0] if photos else None,
                    "photo_urls": photos,
                }
            )

        return {
            "state": "success",
            "timestamp": result.get("timestamp"),
            "meta": result["data"].get("meta", []),
            "hotels": clean_hotels,
        }


# *************** instance ******************
def get_searching_service(
    db: Session = Depends(connect_db),
    client=Depends(get_rapidapi_client),
) -> SearchingService:
    return SearchingService(db=db, client=client)
