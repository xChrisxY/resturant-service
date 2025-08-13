from functools import lru_cache 
from ...config.database import get_database 
from .repositories.mongodb_restaurant_repository import MongoDBRestaurantRepository
from .controllers.restaurant_controller import RestaurantController
from ..domain.repositories.restaurant_repository import RestaurantRepository
from ..application.use_cases.create_restaurant_use_case import CreateRestaurantUseCase
from ..application.use_cases.get_restaurant_by_id_use_case import GetRestaurantByIdUseCase
from ..application.use_cases.delete_restaurant_use_case import DeleteRestaurantUseCase

# Repository dependencies
@lru_cache()
def get_restaurant_repository() -> RestaurantRepository:
    database = get_database()
    return MongoDBRestaurantRepository(database)

# Use case dependencies 
@lru_cache()
def get_create_restaurant_use_case() -> CreateRestaurantUseCase:
    restaurant_repository = get_restaurant_repository()
    return CreateRestaurantUseCase(restaurant_repository)

@lru_cache()
def get_get_restaurant_by_id_use_case() -> GetRestaurantByIdUseCase:
    restaurant_repository = get_restaurant_repository()
    return GetRestaurantByIdUseCase(restaurant_repository)

@lru_cache()
def get_delete_restaurant_use_case() -> DeleteRestaurantUseCase:
    restaurant_repository = get_restaurant_repository()
    return DeleteRestaurantUseCase(restaurant_repository)

@lru_cache()
def get_restaurant_controller() -> RestaurantController:
    create_restaruant_use_case = get_create_restaurant_use_case()
    get_restaurant_by_id_use_case = get_get_restaurant_by_id_use_case()
    delete_restaurant_use_case = get_delete_restaurant_use_case()
    
    return RestaurantController(
        create_restaurant_use_case=create_restaruant_use_case,
        get_restaurant_by_id_use_case=get_restaurant_by_id_use_case, 
        delete_restaurant_use_case=delete_restaurant_use_case
    )