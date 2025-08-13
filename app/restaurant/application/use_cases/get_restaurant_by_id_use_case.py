from ...domain.entities.restaurant import Restaurant
from ...domain.repositories.restaurant_repository import RestaurantRepository
from ....shared.exceptions import NotFoundException

class GetRestaurantByIdUseCase:
    
    def __init__(self, restaurant_repository: RestaurantRepository):
        self.restaurant_repository = restaurant_repository
        
    async def execute(self, restaurant_id: str) -> Restaurant:
        restaurant = await self.restaurant_repository.get_by_id(restaurant_id)
        
        if not restaurant:
            raise NotFoundException(f"Restaurant with id {restaurant} not found")

        return restaurant