from motor.motor_asyncio import AsyncIOMotorDatabase
from ...domain.entities.restaurant import Restaurant
from ...domain.repositories.restaurant_repository import RestaurantRepository

class MongoDBRestaurantRepository(RestaurantRepository):
    
    def __init__(self, database: AsyncIOMotorDatabase):
        self.database = database
        self.collection = database.restaurant

    async def create(self, restaurant: Restaurant) -> Restaurant:
        pass 
    
    async def get_by_id(self, restaurant_id):
        return await super().get_by_id(restaurant_id)

    async def get_by_status(self, status):
        return await super().get_by_status(status)

    async def update_status(self, restaurant_id, new_status):
        return await super().update_status(restaurant_id, new_status)

    async def update(self, restaurant):
        return await super().update(restaurant)

    async def delete(self, restaurant_id):
        return await super().delete(restaurant_id)