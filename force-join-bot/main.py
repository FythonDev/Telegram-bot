from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import json

with open("config.json") as f:
    config = json.load(f)

app = Client("force_join_bot", api_id=config["api_id"], api_hash=config["api_hash"], bot_token=config["bot_token"])

@app.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id
    try:
        member = await client.get_chat_member(config["channel_username"], user_id)
        if member.status in ["member", "administrator", "creator"]:
            await message.reply("👋 Hello! How can I assist you today?")
        else:
            raise Exception("Not a member")
    except:
        btn = InlineKeyboardMarkup([
            [InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{config['channel_username']}")]
        ])
        await message.reply(
            "❌ You are not a member of the required channel.\nPlease join and then press /start again.",
            reply_markup=btn
        )

app.run()
