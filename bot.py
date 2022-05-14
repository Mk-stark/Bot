#import asyncio
from pyrogram import Client
#from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#from pyrogram.errors import FloodWait
from config import API_ID, API_HASH, BOT_TOKEN, ADMINS

class Bot(Client):
    def __init__(self):
        super().__init__("BOT",api_hash=API_HASH,api_id=API_ID,bot_token=BOT_TOKEN,workers=200,plugins={"root":"plugins"})
        
    async def start(self):
        await super().start()
        for chat_id in ADMINS:
            try:
                await self.send_message(text="`Bot Re-Started`", chat_id=chat_id)
            except:
                pass
        
Bot().run()

