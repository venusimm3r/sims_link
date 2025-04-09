from pyrogram import Client, filters
import re
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
DEST_GROUP = int(os.getenv("DEST_GROUP"))

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

link_pattern = re.compile(r"https?://\S+")

# Vamos guardar os IDs das mensagens já processadas
processed_messages = set()

@app.on_message(filters.text & filters.group)
async def link_filter(client, message):
    # Ignora mensagens do grupo de destino
    if message.chat.id == DEST_GROUP:
        return

    # Ignora se já processou essa mensagem
    if message.id in processed_messages:
        return

    if link_pattern.search(message.text):
        processed_messages.add(message.id)
        sender = message.from_user.first_name if message.from_user else "Alguém"
        await app.send_message(DEST_GROUP, f"Link detectado de {sender}:\n{message.text}")

app.run()
