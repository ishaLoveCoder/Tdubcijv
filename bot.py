import telebot
import asyncio
from config import *
from parser import *
from imdb_fetch import get_poster_from_tmdb
from database import movies

bot = telebot.TeleBot(BOT_TOKEN)


def build_download_links(downloads):

    result = []

    for d in downloads:

        if "file_id" in d:

            link = f"https://t.me/{BOT_USERNAME}?start={d['file_id']}"

        else:

            link = d["link"]

        result.append({

            "quality": d["quality"],
            "size": d["size"],
            "url": link

        })

    return result


@bot.message_handler(func=lambda m: True, content_types=["text","video","document"])
def handle_post(message):

    if message.chat.id != AUTO_CHANNEL:
        return

    text = message.text or message.caption or ""

    title = detect_title(text)

    quality = detect_quality(text)

    size = detect_size(text)

    imdb_id = None

    if "tt" in text:
        imdb_id = "tt" + text.split("tt")[1][:7]

    downloads = []

    # TEXT LINKS
    links = extract_links(text)

    for link in links:

        downloads.append({
            "quality": quality,
            "size": size,
            "link": link
        })

    # VIDEO FILE
    if message.video or message.document:

        file = message.video or message.document

        downloads.append({
            "quality": quality,
            "size": str(round(file.file_size/1024/1024,2)) + " MB",
            "file_id": file.file_id
        })

    # POSTER
    poster = ""

    if imdb_id:
        poster = asyncio.run(get_poster_from_tmdb(imdb_id))

    doc = {

        "title": title,

        "imdb_id": imdb_id,

        "poster": poster,

        "downloads": build_download_links(downloads)

    }

    asyncio.run(movies.insert_one(doc))

    print("Saved:", title)


print("Bot Running...")

bot.infinity_polling()
