from pyrogram import Client, filters
from pyrogram.types import Message
import json, os
from datetime import datetime

with open("config.json") as f:
    config = json.load(f)

bot = Client("ActivityTracker", api_id=config["api_id"], api_hash=config["api_hash"], bot_token=config["bot_token"])

DATA_FILE = "activity.json"
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

def log_activity(user_id):
    with open(DATA_FILE) as f:
        data = json.load(f)

    today = datetime.now().strftime("%Y-%m-%d")
    if user_id not in data:
        data[user_id] = {}
    data[user_id][today] = data[user_id].get(today, 0) + 1

    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

@bot.on_message(filters.group)
async def track(client: Client, message: Message):
    if message.from_user:
        log_activity(str(message.from_user.id))

bot.run()