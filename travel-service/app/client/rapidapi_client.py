import json
from functools import lru_cache
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from datetime import date
from app.core.api_paths import ApiPaths
from app.core.config import settings
import socket


class RapidApiError(Exception):
    def __init__(self, status_code: int, detail: str) -> None:
        super().__init__(detail)
        self.status_code = status_code
        self.detail = detail


class RapidApiClient:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.paths = ApiPaths()

    def search_destination(self, query: str):
        querystring = {"query": query}
        return self._get(
            host=ApiPaths.HOST,
            path=ApiPaths.SEARCH_DESTINATION_PATH,
            params=querystring,
        )

    def search_hotel(
        self,
        dest_id: int,
        arrival_date: date,
        departure_date: date,
        price_min: int | None = None,
        price_max: int | None = None,
    ):
        querystring = {
            "dest_id": str(dest_id),
            "search_type": "CITY",
            "arrival_date": arrival_date.strftime("%Y-%m-%d"),
            "departure_date": departure_date.strftime("%Y-%m-%d"),
            "units": "metric",
            "temperature_unit": "c",
            "languagecode": "en-us",
            "currency_code": "AED",
            "location": "US",
        }
        if price_min is not None:
            querystring["price_min"] = str(price_min)
        if price_max is not None:
            querystring["price_max"] = str(price_max)

        return self._get(
            host=ApiPaths.HOST,
            path=ApiPaths.SEARCH_HOTEL_PATH,
            params=querystring,
        )

    def search_attraction_location(self, location: str):
        querystring = {"query": location, "languagecode": "en-us"}
        return self._get(
            host=ApiPaths.HOST,
            path=ApiPaths.SEARCH_ATTRACTION_LOCATION,
            params=querystring,
        )

    def search_attraction_list_by_dest_id(self, location_id: str, date: date):
        querystring = {
            "id": location_id,
            "sortBy": "lowest_price",
            "startDate": date.strftime("%Y-%m-%d"),
        }
        return self._get(
            host=ApiPaths.HOST,
            path=ApiPaths.SEARCH_ATTRACTION_BY_ID,
            params=querystring,
        )

    def search_attraction_details(self, attraction_slug: str):
        querystring = {
            "slug": attraction_slug,
            "languagecode": "en-us",
        }
        return self._get(
            host=ApiPaths.HOST,
            path=ApiPaths.SEARCH_ATTRACTION_BY_SLUG,
            params=querystring,
        )

    def search_flight_location(self, location: str):
        querystring = {"query": location}

        return self._get(
            host=ApiPaths.HOST,
            path=ApiPaths.SEARCH_FLIGHT_LOCATION,
            params=querystring,
        )

    def search_attraction_availabilities(self, attraction_slug: str, date: date):
        querystring = {
            "slug": attraction_slug,
            "date": date.strftime("%Y-%m-%d"),
            "languagecode": "en-us",
            "currency_code": "AED",
        }
        return self._get(
            host=ApiPaths.HOST,
            path=ApiPaths.SEARCH_ATTRACTION_AVALIBILITIES,
            params=querystring,
        )

    def search_flights(
        self, from_id: str, to_id: str, departure_date: date, adults: int, children: str
    ):
        querystring = {
            "fromId": from_id,
            "toId": to_id,
            "departDate": departure_date.strftime("%Y-%m-%d"),
            "adults": str(adults),
            "children": children,
        }

        return self._get(
            host=ApiPaths.HOST,
            path=ApiPaths.SEARCH_FLIGHTS,
            params=querystring,
        )

    # qurey getter
    def _get(self, host: str, path: str, params: dict[str, str]):
        url = f"https://{host}/{path}?{urlencode(params)}"
        request = Request(
            url,
            headers={
                "x-rapidapi-host": host,
                "x-rapidapi-key": self.api_key,
            },
            method="GET",
        )
        try:
            with urlopen(request, timeout=30) as response:
                payload = response.read().decode("utf-8")
                return json.loads(payload)
        except TimeoutError as error:
            raise RapidApiError(504, "RapidAPI request timed out.") from error
        except HTTPError as error:
            detail = error.read().decode("utf-8", errors="replace")
            raise RapidApiError(error.code, detail or str(error)) from error
        except URLError as error:
            raise RapidApiError(500, "Failed to connect to RapidAPI.") from error
        except socket.timeout as error:
            raise RapidApiError(504, "RapidAPI request timed out.") from error


@lru_cache(maxsize=1)
def get_rapidapi_client() -> RapidApiClient:
    if not settings.RAPIDAPI_KEY:
        raise RapidApiError(500, "RAPIDAPI_KEY is not configured.")

    return RapidApiClient(api_key=settings.RAPIDAPI_KEY)
