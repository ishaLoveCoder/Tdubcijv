from fastapi import FastAPI
from database import movies

app = FastAPI()


@app.get("/movies")
async def get_movies():

    data = []

    async for m in movies.find():

        m["_id"] = str(m["_id"])

        data.append(m)

    return data
