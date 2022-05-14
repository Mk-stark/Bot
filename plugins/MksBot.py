from pyrogram import Client, filters
#import asyncio
#import time
#from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
#from pyrogram.errors import FloodWait

@Client.on_message(filters.media & filters.private & filters.chat([645291557, WORK_PLACE]) & ~filters.photo)
async def mk(bot, msg):
