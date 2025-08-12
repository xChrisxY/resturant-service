from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr
from ...domain.entities.enums import Status 

class AddressResponseDTO(BaseModel):
    street: str
    city: str
    state: str
    country: Optional[str] = "Mexico"
    postal_code: Optional[str] = None
    additional_info: Optional[str] = None


class MenuItemResponseDTO(BaseModel):
    id: Optional[str]
    name: str
    price: float
    available: bool


class RestaurantResponseDTO(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    owner_id: str
    address: Optional[AddressResponseDTO] = None
    phone_number: str
    email: EmailStr
    menu_items: List[MenuItemResponseDTO]
    opening_hours: str
    status: Status
    rating: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat() if v else None
        }


class RestaurantListResponseDTO(BaseModel):
    restaurants: List[RestaurantResponseDTO]
    total: int
    page: int
    per_page: int
    total_pages: int

    class Config:
        from_attributes = True


class RestaurantCreatedResponseDTO(BaseModel):
    restaurant: RestaurantResponseDTO
    message: str = "Restaurant created successfully"

    class Config:
        from_attributes = True
