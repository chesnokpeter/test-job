from faststream import FastStream, ContextRepo, Context
from faststream.rabbit import RabbitBroker, RabbitQueue

from schemas import MessageSch
from config import QUEUE, RABBITMQ_URL, TELEGRAM_BOT_TOKEN, RATE_LIMIT
from worker import Worker
from bucket import TokenBucket
from datetime import datetime
import asyncio

broker = RabbitBroker(RABBITMQ_URL)

app = FastStream(broker)


@app.on_startup
async def setup(context: ContextRepo):
    import time
    time.sleep(5)
    context.set_global('worker', Worker(TELEGRAM_BOT_TOKEN, RATE_LIMIT))
    context.set_global('token', TokenBucket(rate=RATE_LIMIT, capacity=RATE_LIMIT))

@broker.subscriber(RabbitQueue(QUEUE, durable=True, arguments={"x-max-priority": 10}))
async def consume_message(message: MessageSch, worker: Worker = Context(), token: TokenBucket = Context()):
    await token.consume()
    await worker.work(message)