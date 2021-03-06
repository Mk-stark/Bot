from asyncio import sleep
from pyrogram import Client
SESSION = os.environ['SESSION']
SLEEP = int(os.environ['SLEEP'])
CHAT_ID = os.environ['CHAT_ID']
TEXT = os.environ['TEXT']
class Bot(Client):
    def __init__(self):
        super().__init__(name=CHAT_ID, session_string=SESSION)
    async def start(self):
        await super().start()
        def send():
            m = await self.send_message(chat_id=CHAT_ID, text=TEXT)
            await m.delete()
        while True:
            for i in range(5):
                send()
            await sleep(SLEEP)
Bot().run()
