from fastapi import APIRouter, Depends, HTTPException
import app.schemas.request as request
from app.service.searching_service import SearchingService, get_searching_service
from app.client.rapidapi_client import RapidApiError

searching_router = APIRouter(prefix="/search", tags=["Searching Service"])


@searching_router.post("/hotel/dest")
async def search_hotel_destination(    
    data: request.HotelDestinationRequest,
    searching_service: SearchingService = Depends(get_searching_service),
):
    """ 
    Parameter: A key word of a city/airport/area
    """
    try:
        return searching_service.search_destination(query=data.query)
    except RapidApiError as error:
        raise HTTPException(
            status_code=error.status_code, detail=error.detail
        ) from error


@searching_router.post("/hotel/search")
async def search_hotel(
    data: request.HotelSearchRequest,
    searching_service: SearchingService = Depends(get_searching_service),
):
    """ 
    Parameter:\n
        dest_id: example: 2008835 (NYC)
    """
    try:
        return searching_service.search_hotel(data=data)
    except RapidApiError as error:
        raise HTTPException(
            status_code=error.status_code, detail=error.detail
        ) from error
