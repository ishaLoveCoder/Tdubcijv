import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

MONGO = os.getenv("MONGO")

AUTO_CHANNEL = int(os.getenv("AUTO_CHANNEL","0"))

ADMIN = [int(x) for x in os.getenv("ADMIN","").split()]

TMDB_KEY = os.getenv("TMDB_KEY")

PORT = int(os.getenv("PORT","8000"))
