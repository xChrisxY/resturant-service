from pydantic import BaseModel, Field 
from typing import Optional

class Address(BaseModel):
    street: str = Field(..., min_length=3, max_length=100, description="Calle y número")
    city: str = Field(..., min_length=3, max_length=100, description="Ciudad del restaurante")
    state: str = Field(..., min_length=3, max_length=100, description="Estado del restaurante")
    country: Optional[str] = Field(default="Mexico", min_length=3, max_length=100)
    postal_code: Optional[str] = Field(default=None, description="Código postal")
    additional_info: Optional[str] = Field(default=None, description="Información adicional del restaurante")