from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr, validator

class CreateAddressDTO(BaseModel):
    street: str = Field(..., min_length=3, max_length=100, description="Calle y número")
    city: str = Field(..., min_length=3, max_length=100, description="Ciudad del restaurante")
    state: str = Field(..., min_length=3, max_length=100, description="Estado del restaurante")
    country: Optional[str] = Field(default="Mexico", min_length=3, max_length=100)
    postal_code: Optional[str] = Field(default=None, description="Código postal")
    additional_info: Optional[str] = Field(default=None, description="Información adicional del restaurante")

    @validator('street', 'city', 'state')
    def validate_required_fields(cls, v):
        if not v or not v.strip():
            raise ValueError('Este campo no puede estar vacío')
        return v.strip()

class CreateMenuItemDTO(BaseModel):
    name: str = Field(..., description="Nombre del platillo", min_length=1, max_length=250)
    price: float = Field(..., description="Precio del platillo", gt=0)
    available: bool = Field(default=True, description="Disponibilidad del platillo")

    @validator('name')
    def validate_name(cls, v):
        if not v or not v.strip():
            raise ValueError('El nombre del platillo no puede estar vacío')
        return v.strip()

class CreateRestaurantDTO(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Nombre del restaurante")
    description: Optional[str] = Field(default=None, description="Descripción breve del restaurante")
    owner_id: str = Field(..., description="ID del propietario del restaurante")
    address: CreateAddressDTO
    phone_number: str = Field(..., description="Número telefónico del restaurante")
    email: EmailStr = Field(..., description="Correo electrónico del restaurante")
    menu_items: List[CreateMenuItemDTO] = Field(default=[], description="Lista de platillos del restaurante")
    opening_hours: str = Field(..., description="Horarios de apertura y cierre")
    status: str = Field(default="open", description="Estado del restaurante: open, closed o suspended")
    rating: Optional[int] = Field(default=0, description="Promedio de reseñas (0-5)", ge=0, le=5)

    @validator('name', 'owner_id', 'phone_number', 'opening_hours')
    def validate_non_empty_fields(cls, v):
        if not v or not v.strip():
            raise ValueError('Este campo no puede estar vacío')
        return v.strip()

    @validator('status')
    def validate_status(cls, v):
        allowed_statuses = ["open", "closed", "suspended"]
        if v not in allowed_statuses:
            raise ValueError(f"Estado inválido. Debe ser uno de: {', '.join(allowed_statuses)}")
        return v

    class Config:
        schema_extra = {
            "example": {
                "name": "Pizzería Don Luigi",
                "description": "Auténtica pizza italiana con ingredientes frescos",
                "owner_id": "6571234567890abcdef12345",
                "address": {
                    "street": "Av. Revolución 123",
                    "city": "Ciudad de México",
                    "state": "CDMX",
                    "country": "Mexico",
                    "postal_code": "06700",
                    "additional_info": "Frente al parque central"
                },
                "phone_number": "+525512345678",
                "email": "contacto@donluigi.com",
                "menu_items": [
                    {
                        "name": "Pizza Margherita",
                        "price": 150.0,
                        "available": True
                    },
                    {
                        "name": "Lasagna Bolognese",
                        "price": 180.0,
                        "available": True
                    }
                ],
                "opening_hours": "Lunes-Domingo 12:00-23:00",
                "status": "open",
                "rating": 5
            }
        }
