from pyrogram import Client, filters
import json
from filters import should_forward
from caption import format_caption

with open("config.json") as f:
    config = json.load(f)

app = Client("forwarder", api_id=config["api_id"], api_hash=config["api_hash"])

@app.on_message(filters.chat(config["source_channel"]))
def forward(client, message):
    if should_forward(message, config["keywords"]):
        caption = format_caption(message.caption, config["caption_template"])
        client.send_message(config["target_channel"], message.text or "", caption=caption)

app.run()
