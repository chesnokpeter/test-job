from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager

from schemas import MessageSch
from producer import Producer
from config import RABBITMQ_URL, QUEUE


@asynccontextmanager
async def lifespan(app: FastAPI):
    import time
    time.sleep(5)
    async with Producer(RABBITMQ_URL, QUEUE) as producer:
        app.state.producer = producer
        yield

async def get_producer(app: FastAPI = Depends(lambda: app)):
    return app.state.producer


app = FastAPI(lifespan=lifespan)

@app.post("/send_message")
async def send_message(message: MessageSch, producer: Producer = Depends(get_producer)):
    await producer.send(message)
    return {"status": "Message added to queue"}
