import requests
from config import TMDB_KEY

async def get_poster_from_tmdb(imdb_id):

    url = f"https://api.themoviedb.org/3/find/{imdb_id}?api_key={TMDB_KEY}&external_source=imdb_id"

    r = requests.get(url).json()

    if not r["movie_results"]:
        return ""

    m = r["movie_results"][0]

    return "https://image.tmdb.org/t/p/w500" + m["poster_path"]
