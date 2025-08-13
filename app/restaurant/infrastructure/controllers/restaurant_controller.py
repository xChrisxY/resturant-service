from fastapi import HTTPException, status
from ...application.use_cases.create_restaurant_use_case import CreateRestaurantUseCase
from ...application.use_cases.get_restaurant_by_id_use_case import GetRestaurantByIdUseCase
from ...application.use_cases.delete_restaurant_use_case import DeleteRestaurantUseCase
from ...application.dto.create_restaurant_dto import CreateRestaurantDTO, CreateMenuItemDTO, CreateAddressDTO
from ...application.dto.restaurant_response_dto import RestaurantResponseDTO, RestaurantCreatedResponseDTO
from ....shared.responses import SuccessResponse
from ....shared.exceptions import BusinessException, NotFoundException, ValidationException

class RestaurantController: 
    
    def __init__(
        self, 
        create_restaurant_use_case: CreateRestaurantUseCase,
        get_restaurant_by_id_use_case: GetRestaurantByIdUseCase,
        delete_restaurant_use_case: DeleteRestaurantUseCase
    ):
        self.create_restaurant_use_case = create_restaurant_use_case
        self.get_restaurant_by_id_use_case = get_restaurant_by_id_use_case
        self.delete_restaurant_use_case = delete_restaurant_use_case

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

        except ValidationException as e: 
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
                detail=f"Error de negocio: {str(e)}"
            )

    async def get_by_id(self, restaurant_id: str) -> SuccessResponse:
        
        try: 
            
            restaurant = await self.get_restaurant_by_id_use_case.execute(restaurant_id)

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

            return SuccessResponse(
                data=restaurant_response, 
                message="Restaurant created successfully",
                status_code=status.HTTP_200_OK
            )
            
        except NotFoundException as e: 
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=str(e)
            )
        
        except Exception as e: 
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                detail=f"Internal Server Error: {str(e)}"
            )

    async def delete_restaurant(self, restaurant_id: str) -> SuccessResponse:
        
        try: 
            
            success = await self.delete_restaurant_use_case.execute(restaurant_id)
            
            return SuccessResponse(
                data={"deleted_restaurant_id": restaurant_id},
                message="Restaurant deleted successfully", 
                status_code=status.HTTP_200_OK
            )
                
        except NotFoundException as e: 
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=str(e)
            )

        except HTTPException:
            raise

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error interno al eliminar el restaurante: {str(e)}"
            ) 
            
