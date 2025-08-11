from pydantic import BaseModel, Field 
from typing import Optional

class Menu(BaseModel): 
    id: Optional[str] = Field(default=None, alias="_id")
    name: str = Field(..., description="Descripción del platillo", min_length=1, max_length=250)
    price: float = Field(..., description="Precio del platillo", gt=0)
    available: bool = Field(default=True, description="Disponibilidad y existencia")