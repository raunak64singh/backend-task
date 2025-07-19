import motor.motor_asyncio
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_DETAILS = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME", "hrone_db")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client[DB_NAME]

product_collection = database.get_collection("products")
order_collection = database.get_collection("orders")
