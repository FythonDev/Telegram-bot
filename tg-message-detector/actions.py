from pyrogram.types import Message

async def handle_action(client, message: Message, action: str):
    if action == "delete":
        await message.delete()
    elif action == "warn":
        await message.reply("⚠️ Please avoid using sensitive words.")
    elif action == "reply":
        await message.reply("🔍 Message flagged for review.")