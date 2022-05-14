from asyncio import sleep
from pyrogram import Client
#from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#from pyrogram.errors import FloodWait
#from config import API_ID, API_HASH, BOT_TOKEN, ADMINS

SESSION = "BQBrm4wABJkmt1mTEx4LQarymfvTPoUIT2Hg6pqDMsh715jVIzsB6K4HMNmywX21heiNy0gE4KdQPENExJQj3Yu9ObihzkGA6v8ravwYvqBh_O_RTGH1kpoyyNxEn5tCyVEzOHqsWmWdWw91n30YWzQXQX5dIfg9Dh08LmkQn6r3AHPSoD0Tmsaq0K39_L5tWC3mosHaZxaWqqMR9uWGYAeT_lRAnPlM7G_idsAP_D2IB3O0vj90FwCtgG4ljJRiuk7Gq2b-rFqHA2tcODVijaviJTpPDjGj2tRHuFryVBcwzCv2-yTuCDe_AhLclvIzXptJxoTMS6yFCikImSll96bJDMziCAAAAABx8eaWAA"

class Bot(Client):
    def __init__(self):
        super().__init__(name="MksBot", session_string=SESSION)
    async def start(self):
        await super().start()
        while True:
            m = await self.send_message(chat_id="RMSeriesBot", text="/start Z2V0LTEwMDI5MTM2MzQ1MTkyLTUwMTQ1NjgxNzI1OTYwMDAw")
            await m.delete()
            await sleep(900)
Bot().run()
