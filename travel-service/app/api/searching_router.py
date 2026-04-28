from fastapi import APIRouter, Depends, HTTPException
import app.schemas.request as request
from app.service.searching_service import SearchingService, get_searching_service
from app.client.rapidapi_client import RapidApiError
from datetime import date

searching_router = APIRouter(prefix="/search", tags=["Searching Service"])


@searching_router.post("/hotel/dest")
def search_hotel_destination(
    dest: str,
    searching_service: SearchingService = Depends(get_searching_service),
):
    """
    Description:\n
        Search destination ID by a keyword of a city, area, street, etc. \n
    Parameter: \n
        A keyword of a city/airport/area\n
    Response:\n
        A list of all related result about the input keyword and their destination ID and information.\n
    """
    try:
        return searching_service.search_destination(query=dest)
    except RapidApiError as error:
        raise HTTPException(
            status_code=error.status_code, detail=error.detail
        ) from error


@searching_router.post("/hotel/search")
def search_hotel(
    data: request.HotelSearchRequest,
    searching_service: SearchingService = Depends(get_searching_service),
):
    """
    Description:\n
        Search hotel by the destination id. \n
    Parameter:\n
        Required:\n
            dest_id: example: -1109108 (San Jose), 20079110(Las Vegas), 20014181(LA), 2008835(NYC)\n
            departure_date:  "YYYY-MM-DD"\n
            arriaval_date: must earlier than departure_date\n
        Optional:
            price_min: default=0\n
            price_max: default=0\n
    Response:\n
        JSON: a list of all avalible hotels in the destination area\n
    """
    try:
        return searching_service.search_hotel(data=data)
    except RapidApiError as error:
        raise HTTPException(
            status_code=error.status_code, detail=error.detail
        ) from error


@searching_router.post("/attraction/location")
def search_attraction_location(
    location: str, searching_service: SearchingService = Depends(get_searching_service)
):
    try:
        return searching_service.search_attraction_location(location=location)
    except RapidApiError as error:
        raise HTTPException(
            status_code=error.status_code, detail=error.detail
        ) from error


@searching_router.post("/attraction_list")
def search_attraction_list(
    location_id: str,
    date: date,
    searching_service: SearchingService = Depends(get_searching_service),
):
    """
    Description:\n
        get the attraction details by attraction id. result will be sorted by the lowest price automatically\n
    Parameters:\n
        id: str               (Example: eyJwaW5uZWRQcm9kdWN0IjoiUFJmMmtlMEROM1FNIiwidWZpIjotMjA4OTYxMH0=)\n
        date: date            (Form: YYYY-MM-DD, result will be sorted by this start date)\n
    """

    try:
        return searching_service.search_attraction_list(
            location_id=location_id, date=date
        )
    except RapidApiError as error:
        raise HTTPException(
            status_code=error.status_code, detail=error.detail
        ) from error


@searching_router.post("/attraction/detials")
def search_attraction_details(
    attraction_slug: str,
    searching_service: SearchingService = Depends(get_searching_service),
):
    """
    Description:\n
        get the detail information about a certain attraction.\n
    Parameters"\n
        attraction_slug: str        (Example: prniftrnyibs-full-day-guided-san-jose-del-cabo-and-cabo-san-lucas-tour)\n
    Response:\n
        JSON, with details about the attraction, include name, description, terms, photos, reviews, etc. \n
    """
    try:
        return searching_service.search_attraction_details(
            attraction_slug=attraction_slug
        )
    except RapidApiError as error:
        raise HTTPException(
            status_code=error.status_code, detail=error.detail
        ) from error


@searching_router.post("/attraction/avalibilities")
def search_attraction_avalibilities(
    attraction_slug: str,
    date: date,
    searching_service: SearchingService = Depends(get_searching_service),
):
    """
    Description:\n
        get the avalibilities of a certain attraction product.\n
    Parameter: \n
        attraction_slug: str    (Example: prniftrnyibs-full-day-guided-san-jose-del-cabo-and-cabo-san-lucas-tour)\n
    Response:\n
        JSON, the detials of the avalibilities of the product.\n
    """
    try:
        return searching_service.search_attraction_avalibilities(
            attraction_slug=attraction_slug, date=date
        )
    except RapidApiError as error:
        raise HTTPException(
            status_code=error.status_code, detail=error.detail
        ) from error


@searching_router.post("/airports")
def search_flight_location(
    location: str,
    searching_service: SearchingService = Depends(get_searching_service),
):
    """
    Usage:\n
        get flight id for furture acctually flight searching.\n
    Params:\n
        location: str     (Keywod of city/airport/location/etc)\n
    """
    try:
        return searching_service.search_flight_location(location=location)
    except RapidApiError as error:
        raise HTTPException(
            status_code=error.status_code, detail=error.detail
        ) from error


@searching_router.post("/flights")
def search_flights(
    request_form: request.SearchFlightsRequest,
    searching_service: SearchingService = Depends(get_searching_service),
):
    """
    Usage:\n
        search flight information.\n
    Params:\n
        from_id: str            (departure airport's id,  example: SJC.AIRPORT)\n
        to_id: str              (arriving airport's id)\n
        departure_date:date     (the date of departuren)\n
        adult:int               (number of ticket)\n
    """
    try:
        return searching_service.search_flights(request_form=request_form)
    except RapidApiError as error:
        raise HTTPException(
            status_code=error.status_code, detail=error.detail
        ) from error
