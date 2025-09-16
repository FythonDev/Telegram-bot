from pyrogram import Client, filters
import json
from filters import is_sensitive
from actions import handle_action

with open("config.json") as f:
    config = json.load(f)

app = Client("detector", api_id=config["api_id"], api_hash=config["api_hash"], bot_token=config["bot_token"])

@app.on_message(filters.chat(config["target_chat"]))
async def detect(client, message):
    if is_sensitive(message.text, config["bad_words"]):
        await handle_action(client, message, config["action"])

app.run()