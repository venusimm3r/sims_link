
from pyrogram import Client, filters
import re
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
DEST_GROUP = int(os.getenv("DEST_GROUP"))

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Expressão pra detectar links
link_pattern = re.compile(r"https?://\S+")

@app.on_message(filters.text & filters.group)
async def link_filter(client, message):
    if link_pattern.search(message.text):
        await app.send_message(DEST_GROUP, f"Link detectado:\n{message.text}")

app.run()
