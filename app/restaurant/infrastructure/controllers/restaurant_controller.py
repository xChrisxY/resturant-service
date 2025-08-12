from fastapi import HTTPException, status
from ...application.use_cases.create_restaurant_use_case import CreateRestaurantUseCase
from ...application.dto.create_restaurant_dto import CreateRestaurantDTO, CreateMenuItemDTO, CreateAddressDTO
from ...application.dto.restaurant_response_dto import RestaurantResponseDTO, RestaurantCreatedResponseDTO
from ....shared.responses import SuccessResponse
from ....shared.exceptions import BusinessException

class RestaurantController: 
    
    def __init__(self, create_restaurant_use_case: CreateRestaurantUseCase):
        self.create_restaurant_use_case = create_restaurant_use_case

    async def create_restaurant(self, restaurant_dto: CreateRestaurantDTO) -> SuccessResponse:

        try: 
            
            restaurant = await self.create_restaurant_use_case.execute(restaurant_dto)

            restaurant_response = RestaurantResponseDTO(
                id=restaurant.id, 
                name=restaurant.name, 
                description=restaurant.description, 
                owner_id=restaurant.owner_id,
                address={
                    "street" : restaurant.address.street, 
                    "city" : restaurant.address.city, 
                    "state" : restaurant.address.state, 
                    "country" : restaurant.address.country, 
                    "postal_code" : restaurant.address.postal_code, 
                    "additional_info" : restaurant.address.additional_info
                },
                phone_number=restaurant.phone_number,
                email=restaurant.email, 
                menu_items=[
                    {"id": item.id, "name" : item.name, "price" : item.price, "available": item.available}
                    for item in restaurant.menu_items
                ],
                opening_hours=restaurant.opening_hours, 
                status=restaurant.status, 
                rating=restaurant.rating,
                created_at=restaurant.created_at, 
                updated_at=restaurant.updated_at
            )

            response_data = RestaurantCreatedResponseDTO(restaurant=restaurant_response)

            return SuccessResponse(
                data=response_data, 
                message="Restaurant created succesfully", 
                status_code=status.HTTP_201_CREATED
            )
            
        except BusinessException as e: 
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )