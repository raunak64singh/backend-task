from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from database import product_collection, order_collection
from models import product_helper, order_helper
from schemas import ProductSchema, ProductResponse, OrderSchema, OrderResponse
from bson import ObjectId
import re

app = FastAPI()

@app.post("/products", status_code=201, response_model=ProductResponse)
async def create_product(product: ProductSchema):
    new_product = await product_collection.insert_one(product.dict())
    created_product = await product_collection.find_one({"_id": new_product.inserted_id})
    return product_helper(created_product)

@app.get("/products", response_model=List[ProductResponse])
async def list_products(
    name: Optional[str] = None,
    size: Optional[str] = None,
    limit: int = 10,
    offset: int = 0
):
    query = {}
    if name:
        query["name"] = {"$regex": re.escape(name), "$options": "i"}
    if size:
        query["size"] = size

    cursor = product_collection.find(query).skip(offset).limit(limit)
    products = [product_helper(p) async for p in cursor]
    return products

@app.post("/orders", status_code=201, response_model=OrderResponse)
async def create_order(order: OrderSchema):
    order_dict = order.dict()
    new_order = await order_collection.insert_one(order_dict)
    created_order = await order_collection.find_one({"_id": new_order.inserted_id})
    return order_helper(created_order)

@app.get("/orders/{user_id}", response_model=List[OrderResponse])
async def get_orders_by_user(
    user_id: str,
    limit: int = 10,
    offset: int = 0
):
    cursor = order_collection.find({"user_id": user_id}).skip(offset).limit(limit)
    orders = [order_helper(order) async for order in cursor]
    return orders
