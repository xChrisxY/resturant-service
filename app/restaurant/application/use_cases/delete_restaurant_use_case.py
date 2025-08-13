from ...domain.entities.restaurant import Restaurant 
from ...domain.repositories.restaurant_repository import RestaurantRepository

class DeleteRestaurantUseCase:
    
    def __init__(self, restaurant_repository: RestaurantRepository):
        self.restaurant_repository = restaurant_repository 
        
    async def execute(self, restaurant_id: str) -> bool: 
        
        success = await self.restaurant_repository.delete(restaurant_id)