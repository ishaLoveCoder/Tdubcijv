import requests
from config import TMDB_KEY

async def get_movie(imdb):

    url = f"https://api.themoviedb.org/3/find/{imdb}?api_key={TMDB_KEY}&external_source=imdb_id"

    r = requests.get(url).json()

    if not r["movie_results"]:
        return {}

    m = r["movie_results"][0]

    return {

        "title": m["title"],

        "description": m["overview"],

        "poster": "https://image.tmdb.org/t/p/w500" + m["poster_path"],

        "year": m["release_date"][:4]

    }
