from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional, List
from .enums import Status
from .address import Address
from .menu import Menu
from datetime import datetime, timezone
from bson import ObjectId

class Restaurant(BaseModel): 
    id : Optional[str] = Field(default=None, alias="_id")
    name: str = Field(..., min_length=3, max_length=50, description="Nombre del restaurante")
    description: Optional[str] = Field(default=None)
    owner_id: str 

    address: Optional[Address] = Field(None, description="Dirección del empleado")
    
    phone_number: str = Field(..., description="Número teléfonico del restaurante")
    email: EmailStr = Field(..., description="Correo electronico del restaurante")
    menu_items: List[Menu] = Field(default=[], description="Menu del restaurante")
    opening_hours: str = Field(..., description="Horarios de apertura")
    status: Status = Field(default=Status.OPEN, description="Estado")
    rating: int = Field(..., description="Promedio de reseñas (0-5)", ge=0, le=5)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    @field_validator('id', mode='before')
    @classmethod
    def validate_object_id(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        return v

    class Config:
        populate_by_name = True 
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str, 
            datetime: lambda v: v.isoformat()
        }

    def update_status(self, new_status: Status) -> None: 
        self.status = new_status 
        self.updated_at = datetime.now(timezone.utc)

    