import aio_pika

from schemas import MessageSch

class Producer:
    def __init__(self, RABBITMQ_URL: str, QUEUE: str):
        self.RABBITMQ_URL = RABBITMQ_URL
        self.QUEUE = QUEUE

        self.connection = None
        self.channel = None

    async def connect(self):
        self.connection = await aio_pika.connect_robust(self.RABBITMQ_URL)
        self.channel = await self.connection.channel()
        await self.channel.declare_queue(self.QUEUE, durable=True, arguments={"x-max-priority": 10})

    async def send(self, data: MessageSch) -> None:
        message = data.model_dump_json()
        await self.channel.default_exchange.publish(
            aio_pika.Message(
                body=message.encode(),
                delivery_mode=aio_pika.DeliveryMode.PERSISTENT,
                priority=data.priority
            ),
            routing_key=self.QUEUE
        )

    async def close(self):
        if self.connection:
            await self.connection.close()
            self.connection = None
            self.channel = None

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()




