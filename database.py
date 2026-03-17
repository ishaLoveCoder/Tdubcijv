from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO

client = AsyncIOMotorClient(MONGO)

db = client.moviesite

movies = db.movies
