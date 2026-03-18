from fastapi import FastAPI
from database import movies

app = FastAPI()


@app.get("/")
async def home():

    data = []

    async for m in movies.find():

        m["_id"] = str(m["_id"])
        data.append(m)

    return data


@app.get("/search")
async def search(q: str):

    data = []

    async for m in movies.find({"title": {"$regex": q, "$options": "i"}}):

        m["_id"] = str(m["_id"])
        data.append(m)

    return data
