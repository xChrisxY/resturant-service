from ...domain.entities.restaurant import Restaurant 
from ...domain.repositories.restaurant_repository import RestaurantRepository
from ..dto.create_restaurant_dto import CreateRestaurantDTO, CreateMenuItemDTO, CreateAddressDTO
from ....shared.exceptions import BusinessException

class CreateRestaurantUseCase: 
    def __init__(self, restaurant_repository: RestaurantRepository):
        self.restaurant_repository = restaurant_repository

    async def execute(self, restaurant_dto: CreateRestaurantDTO) -> Restaurant:
        
        try: 
            menu_items = []

            for menu_dto in restaurant_dto.menu_items: 
                menu_item = CreateMenuItemDTO(
                    name=menu_dto.name, 
                    price=menu_dto.price, 
                    available=menu_dto.available
                )
                menu_items.append(menu_item)

            restaurant_address = CreateAddressDTO(
                street=restaurant_dto.address.street, 
                city=restaurant_dto.address.city, 
                state=restaurant_dto.address.state, 
                postal_code=restaurant_dto.address.postal_code, 
                additional_info=restaurant_dto.address.additional_info
            )

            restaurant = CreateRestaurantDTO(
                name=restaurant_dto.name, 
                description=restaurant_dto.address, 
                owner_id=restaurant_dto.owner_id, 
                address=restaurant_address, 
                phone_number=restaurant_dto.phone_number, 
                email=restaurant_dto.email, 
                menu_items=menu_items, 
                opening_hours=restaurant_dto.opening_hours,
                status=restaurant_dto.status, 
                rating=restaurant_dto.rating
            )

            created_restaurant = await self.restaurant_repository.create(restaurant)
            
        except Exception as e: 
            raise BusinessException(f"Failed to create order: {str(e)}")
    
    
    