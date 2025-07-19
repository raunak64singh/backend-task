from pydantic import BaseModel, Field
from typing import List, Optional

class ProductSchema(BaseModel):
    name: str
    size: str
    price: float

class ProductResponse(ProductSchema):
    id: str

class OrderItem(BaseModel):
    product_id: str
    quantity: int

class OrderSchema(BaseModel):
    user_id: str
    items: List[OrderItem]

class OrderResponse(OrderSchema):
    id: str
