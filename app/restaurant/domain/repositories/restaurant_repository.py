from abc import ABC, abstractmethod
from typing import Optional, List
from ..entities.restaurant import Restaurant 
from ..entities.enums import Status

class RestaurantRepository(ABC):
    
    @abstractmethod 
    async def create(self, restaurant: Restaurant) -> Restaurant: 
        pass 
    
    @abstractmethod 
    async def get_by_id(self, restaurant_id: str) -> Optional[Restaurant]: 
        pass 
    
    @abstractmethod 
    async def get_by_status(self, status: Status) -> List[Restaurant]: 
        pass 
    
    @abstractmethod 
    async def update_status(self, restaurant_id: str, new_status: Status) -> bool: 
        pass 
    
    @abstractmethod 
    async def update(self, restaurant: Restaurant) -> Restaurant: 
        pass 
    
    @abstractmethod 
    async def delete(self, restaurant_id: str) -> bool: 
        pass