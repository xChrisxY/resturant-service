from motor.motor_asyncio import AsyncIOMotorDatabase
from ...domain.entities.restaurant import Restaurant
from ...domain.repositories.restaurant_repository import RestaurantRepository

from typing import Optional
from bson import ObjectId

class MongoDBRestaurantRepository(RestaurantRepository):
    
    def __init__(self, database: AsyncIOMotorDatabase):
        self.database = database
        self.collection = database.restaurant

    async def create(self, restaurant: Restaurant) -> Restaurant:

        restaurant_dict = restaurant.model_dump(by_alias=True, exclude={"id"})

        result = await self.collection.insert_one(restaurant_dict)

        created_restaurant = await self.collection.find_one({"_id": result.inserted_id})

        if created_restaurant and "_id" in created_restaurant:
            created_restaurant["_id"] = str(created_restaurant["_id"])
            
        return Restaurant(**created_restaurant)
    
    async def get_by_id(self, restaurant_id: str) -> Optional[Restaurant]:

        try: 
            object_id = ObjectId(restaurant_id)
            restaurant_doc = await self.collection.find_one({"_id": object_id})

            if restaurant_doc:
                # Convertir ObjectId to string for Pydantic model
                restaurant_doc["_id"] = str(restaurant_doc["_id"])
                return Restaurant(**restaurant_doc)
            
            return None
            
        except Exception:
            return None
        
        
    async def get_by_status(self, status):
        return await super().get_by_status(status)

    async def update_status(self, restaurant_id, new_status):
        return await super().update_status(restaurant_id, new_status)

    async def update(self, restaurant):
        return await super().update(restaurant)

    async def delete(self, restaurant_id):

        try:
            
            object_id = ObjectId(restaurant_id)
            
            result = await self.collection.delete_one({
                "_id" : object_id
            })

            return result.delete_count > 0

        except Exception as e:
            return False