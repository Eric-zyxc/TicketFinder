from sqlalchemy.orm import Session
from app.dal.booking_DAO import BookingDAO
from app.client.rapidapi_client import RapidApiClient
import app.schemas.request as request
from fastapi import Depends
from app.core.database import connect_db
from app.client.rapidapi_client import get_rapidapi_client
from datetime import date
from app.core.config import settings


class SearchingService:
    def __init__(self, db: Session, client: RapidApiClient):
        self.dal = BookingDAO(db=db)
        self.client = client

    def search_destination(self, query: str):
        result = self.client.search_destination(query=query)
        if result.get("status") is True:
            return {"state": "success", "result": result}
        return {
            "state": "fail",
            "result": result,
        }

    def search_hotel(self, data: request.HotelSearchRequest):
        result = self.client.search_hotel(
            dest_id=data.dest_id,
            arrival_date=data.arrival_date,
            departure_date=data.departure_date,
            price_min=data.price_min,
            price_max=data.price_max,
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
                    "excluded_price": excluded_price.get("value"),
                    "main_photo": photos[0] if photos else None,
                    "photo_urls": photos,
                }
            )

        cheapest_hotels = get_cheapest_hotels(
            clean_hotels, limit=settings.MAX_CHEAPEST_HOTELS
        )  # get cheapest 50 results

        return {
            "state": "success",
            "result": cheapest_hotels,
        }

    def search_attraction_location(self, location: str):
        result = self.client.search_attraction_location(location=location)
        if result.get("status") is False:
            return {"state": "fail", "result": result}
        return {"state": "success", "result": result}

    def search_attraction_detail(self, attraction_id: str, date: date):
        result = self.client.search_attraction_by_id(
            attraction_id=attraction_id, date=date
        )
        if result.get("status") is False:
            return {"state": "fail", "result": result}

        cleaned_result = []
        products = result.get("data", {}).get("products", [])
        for product in products:
            price_info = product.get("representativePrice") or {}
            photo_info = product.get("primaryPhoto") or {}
            cancellation_policy = product.get("cancellationPolicy") or {}
            ufi_details = product.get("ufiDetails") or {}
            review_stats = product.get("reviewsStats") or {}
            combined_stats = review_stats.get("combinedNumericStats") or {}
            cleaned_result.append(
                {
                    "id": product.get("id"),
                    "name": product.get("name"),
                    "slug": product.get("slug"),
                    "short_description": product.get("shortDescription"),
                    "price": price_info.get("chargeAmount"),
                    "currency": price_info.get("currency"),
                    "photo": photo_info.get("small"),
                    "city": ufi_details.get("bCityName"),
                    "ufi": ufi_details.get("ufi"),
                    "free_cancellation": cancellation_policy.get("hasFreeCancellation"),
                    "review_average": combined_stats.get("average"),
                    "review_total": combined_stats.get("total"),
                }
            )

        return {"state": "success", "result": cleaned_result}

    def search_flight_location(self, location: str):
        result = self.client.search_flight_location(location=location)
        if result.get("status") is False:
            return {"state": "fail", "result": result}

        data = result.get("data")
        return {"state": "success", "result": data}

    def search_flights(self, request_form: request.SearchFlightsRequest):
        result = self.client.search_flights(
            from_id=request_form.from_id,
            to_id=request_form.to_id,
            departure_date=request_form.departure_date,
            adults=request_form.adults,
            children=request_form.children,
        )
        if result.get("status") is False:
            return {"state": "fail", "result": result}

        cleaned_data = []

        offers = result.get("data", {}).get("flightOffers", [])

        for offer in offers:
            token = offer.get("token")
            segment = (offer.get("segments") or [{}])[0]
            departure_airport = segment.get("departureAirport") or {}
            arrival_airport = segment.get("arrivalAirport") or {}
            departure_time = segment.get("departureTimeTz") or segment.get(
                "departureTime"
            )
            arrival_time = segment.get("arrivalTimeTz") or segment.get("arrivalTime")
            duration = segment.get("totalTime")
            first_leg = (segment.get("legs") or [{}])[0]
            carrier_data = (first_leg.get("carriersData") or [{}])[0]
            airline_name = carrier_data.get("name")
            airline_code = carrier_data.get("code")
            airline_logo = carrier_data.get("logo")
            stops = len(segment.get("legs", [])) - 1
            if stops < 0:
                stops = 0
            price_info = offer.get("priceBreakdown", {}).get("total", {})
            price = None
            currency = price_info.get("currencyCode")
            if price_info:
                units = price_info.get("units", 0)
                nanos = price_info.get("nanos", 0)
                price = float(units) + float(nanos) / 1e9

            cleaned_data.append(
                {
                    "token": token,
                    "airline_name": airline_name,
                    "airline_code": airline_code,
                    "airline_logo": airline_logo,
                    "departure_airport": departure_airport.get("code"),
                    "departure_city": departure_airport.get("cityName"),
                    "arrival_airport": arrival_airport.get("code"),
                    "arrival_city": arrival_airport.get("cityName"),
                    "departure_time": departure_time,
                    "arrival_time": arrival_time,
                    "duration_seconds": duration,
                    "stops": stops,
                    "price": price,
                    "currency": currency,
                }
            )
        cleaned_data.sort(key=lambda x: x["price"])
        return {"state": "success", "result": cleaned_data}


# *************** helper functions ******************
def get_searching_service(
    db: Session = Depends(connect_db),
    client=Depends(get_rapidapi_client),
) -> SearchingService:
    return SearchingService(db=db, client=client)


def get_cheapest_hotels(hotels: list[dict], limit: int) -> list[dict]:
    def hotel_price(hotel: dict) -> float:
        price = hotel.get("gross_price")
        if price is None:
            return float("inf")
        return float(price)

    sorted_hotels = sorted(hotels, key=hotel_price)
    return sorted_hotels[:limit]
