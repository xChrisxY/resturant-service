from fastapi import APIRouter, Depends, status 
from typing import Optional 

from ....shared.responses import SuccessResponse
from ...application.dto.restaurant_response_dto import RestaurantCreatedResponseDTO, RestaurantResponseDTO
from ...application.dto.create_restaurant_dto import CreateRestaurantDTO
from ..controllers.restaurant_controller import RestaurantController
from ..dependencies import get_restaurant_controller

router = APIRouter(prefix="/api/v1/restaurant", tags=["restaurant"])

@router.post(
    "/", 
    response_model=SuccessResponse[RestaurantCreatedResponseDTO],
    status_code=status.HTTP_201_CREATED, 
    summary="Create a new restaurant", 
    description="Create a new restaurant with menu list and delivery address"
)
async def create_restaurant(restaurant_dto: CreateRestaurantDTO, controller: RestaurantController = Depends(get_restaurant_controller)):
    return await controller.create_restaurant(restaurant_dto)

@router.get(
    "/{restaurant_id}", 
    response_model=SuccessResponse[RestaurantResponseDTO],
    status_code=status.HTTP_200_OK, 
    summary="Get restaurant by id", 
    description="Obtain a specific restaurant by id"
)
async def get_restaurant(restaurant_id: str, controller : RestaurantController = Depends(get_restaurant_controller)):
    return await controller.get_by_id(restaurant_id)

@router.delete(
    "/{restaurant_id}", 
    response_model=SuccessResponse, 
    status_code=status.HTTP_200_OK, 
    summary="Delete a restaurant",
    description="Delete a specific restaurant by id",
)
async def delete_restaurant(restaurant_id, controller: RestaurantController = Depends(get_restaurant_controller)):
    return await controller.delete_restaurant(restaurant_id)