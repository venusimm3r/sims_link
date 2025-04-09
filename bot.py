from pyrogram import Client, filters
import re
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
DEST_GROUP = int(os.getenv("DEST_GROUP"))

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

link_pattern = re.compile(r"https?://\S+")

@app.on_message(filters.text & filters.group)
async def link_filter(client, message):
    # Ignora mensagens do próprio bot
    if message.from_user and message.from_user.is_bot:
        return

    if link_pattern.search(message.text):
        try:
            await app.send_message(DEST_GROUP, f"Link detectado:\n{message.text}")
            await message.delete()
        except Exception as e:
            print("Erro:", e)

app.run()
