from aiogram import Bot

from asyncio import sleep, Semaphore

from schemas import MessageSch

class Worker:
    def __init__(self, TELEGRAM_BOT_TOKEN: str, RATE_LIMIT: int):
        self.RATE_LIMIT = RATE_LIMIT
        self.bot = Bot(TELEGRAM_BOT_TOKEN)
        self.semaphore = Semaphore(RATE_LIMIT)


    async def work(self, data: MessageSch):
        await sleep(0.3)
        print( 'СООБЩЕНИЕ ОТПРАВЛЕНО')
        # async with self.semaphore:
        # try:

            # await self.bot.send_message(data.chat_id, text=data.text)
        # except:
        # print('ERROR')
            # await sleep(1)
