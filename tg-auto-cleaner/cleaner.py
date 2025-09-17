from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
import json

with open("config.json") as f:
    config = json.load(f)

bot = Client(
    name="CleanerBot",
    api_id=config["api_id"],
    api_hash=config["api_hash"],
    bot_token=config["bot_token"]
)

DELETE_DELAY = config["delete_delay"]
KEYWORDS = [kw.lower() for kw in config["keywords"]]
WHITELIST = config["whitelist"]

@bot.on_message(filters.group)
async def auto_clean(client: Client, message: Message):
    if message.from_user and message.from_user.id in WHITELIST:
        return

    if message.text and any(word in message.text.lower() for word in KEYWORDS):
        await asyncio.sleep(DELETE_DELAY)
        await message.delete()

bot.run()