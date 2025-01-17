import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    ContentType,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)

from producer import Producer
from schemas import MessageSch
from config import TELEGRAM_BOT_TOKEN, RABBITMQ_URL, QUEUE

dp = Dispatcher()
bot = Bot(TELEGRAM_BOT_TOKEN)




@dp.message()
async def command_start_handler(message: Message, producer: Producer) -> None:
    await producer.send(MessageSch(chat_id=message.chat.id, text=message.text))


async def main():
    import time
    time.sleep(5)
    print(12313123)
    async with Producer(RABBITMQ_URL, QUEUE) as producer:
        dp['producer'] = producer
        await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())