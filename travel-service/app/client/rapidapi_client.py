import json
from functools import lru_cache
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from datetime import date

from app.core.config import settings

HOST = "booking-com15.p.rapidapi.com"
SEARCH_DESTINATION_PATH = "api/v1/hotels/searchDestination"
SEARCH_HOTEL_PATH = "api/v1/hotels/searchHotels"


class RapidApiError(Exception):
    def __init__(self, status_code: int, detail: str) -> None:
        super().__init__(detail)
        self.status_code = status_code
        self.detail = detail


class RapidApiClient:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def search_destination(self, query: str):
        querystring = {"query": query}
        return self._get(host=HOST, path=SEARCH_DESTINATION_PATH, params=querystring)

    def search_hotel(
        self,
        dest_id: int,
        arrival_date: date,
        departure_date: date,
        price_min: int | None = None,
        price_max: int | None = None,
        sort_by: str | None = None,
        categories_filter: str | None = None,
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
        if sort_by:
            querystring["sort_by"] = sort_by
        if categories_filter:
            querystring["categories_filter"] = categories_filter

        print(querystring)
        return self._get(
            host=HOST,
            path=SEARCH_HOTEL_PATH,
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
        except HTTPError as error:
            detail = error.read().decode("utf-8", errors="replace")
            raise RapidApiError(error.code, detail or str(error)) from error
        except URLError as error:
            raise RapidApiError(500, "Failed to connect to RapidAPI.") from error


@lru_cache(maxsize=1)
def get_rapidapi_client() -> RapidApiClient:
    if not settings.RAPIDAPI_KEY:
        raise RapidApiError(500, "RAPIDAPI_KEY is not configured.")

    return RapidApiClient(api_key=settings.RAPIDAPI_KEY)
