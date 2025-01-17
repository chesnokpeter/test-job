from aiogram import Bot

from asyncio import sleep

from schemas import MessageSch

class Worker:
    def __init__(self, TELEGRAM_BOT_TOKEN: str, RATE_LIMIT: int):
        self.RATE_LIMIT = RATE_LIMIT
        self.bot = Bot(TELEGRAM_BOT_TOKEN)

    async def work(self, data: MessageSch):
        await self.bot.send_message(data.chat_id, text=data.text)
        await sleep(1 / self.RATE_LIMIT)
