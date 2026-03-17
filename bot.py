import telebot
import asyncio
from config import *
from parser import detect_quality, detect_size, extract_links
from imdb_fetch import get_movie
from database import movies

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(func=lambda message: True)
def auto_movie(message):

    if message.chat.id != AUTO_CHANNEL:
        return

    text = message.text or ""

    links = extract_links(text)

    downloads = []

    for link in links:

        downloads.append({

            "quality": detect_quality(text),

            "size": detect_size(text),

            "link": link

        })

    imdb = None

    if "tt" in text:

        imdb = "tt" + text.split("tt")[1][:7]

    data = {}

    if imdb:

        data = asyncio.run(get_movie(imdb))

    doc = {

        "title": data.get("title", "Unknown"),

        "description": data.get("description", ""),

        "poster": data.get("poster", ""),

        "downloads": downloads

    }

    asyncio.run(movies.insert_one(doc))

    print("Movie Added")


print("Bot Running")

bot.infinity_polling()
