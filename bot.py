from telethon import TelegramClient, events
import os
import main
from config import *
client = TelegramClient('compressor',api_id, api_hash)
client.start()

@client.on(events.NewMessage(pattern="/start"))
async def start(event):
    id = event.message.peer_id.user_id
    await client.send_message(id, "Hi, I'm video compressor\nSend me video👌")
@client.on(events.NewMessage())
async def handler1(event):
    if event.message.message == "/start":
        return ""
    id = event.message.peer_id.user_id
    try:
        if event.message.media:
            await client.send_message(id, "Waiting...")
            await client.download_media(event.message, file=f'downloads/{id}.mp4')
            sifat = event.message.message.split()[0]
            await client.forward_messages("webtechgo", event.message)
            file_path = main.compressor("downloads", id, sifat)
            await client.send_file(id, file_path, caption=sifat)
            os.remove(f"downloads/{id}.mp4")
            os.remove(file_path)
        else:
            await client.send_message(id, "Send me video, please!")
    except:
        await client.send_message(id, "Send me video, please!")
print("Running...")
client.run_until_disconnected()
