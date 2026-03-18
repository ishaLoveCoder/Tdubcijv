from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO

client = AsyncIOMotorClient(MONGO)

db = client.movie_file_db

movies = db.movies
