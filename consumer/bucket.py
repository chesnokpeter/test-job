import asyncio
import time


class TokenBucket:
    def __init__(self, rate: int, capacity: int):
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity
        self.last_refill = time.perf_counter()

    async def consume(self, tokens: int = 1):
        while True:
            now = time.perf_counter()
            elapsed = now - self.last_refill
            print('СЕКУНД ПРОШЛО', elapsed)
            print('ТОКЕНОВ ', self.tokens)

            if elapsed >= 1:
                self.tokens = self.capacity
                self.last_refill = now

            if self.tokens >= tokens:
                self.tokens -= tokens
                return

            await asyncio.sleep(1 - elapsed)