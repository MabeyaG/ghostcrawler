import asyncio
from core.scheduler import Scheduler
from core.request_handler import RequestHandler
from utils.logger import logger

class Crawler:
    def __init__(self, urls):
        self.scheduler = Scheduler(urls)
        self.request_handler = RequestHandler()

    async def crawl(self):
        while not self.scheduler.is_empty():
            url = self.scheduler.get_next()
            logger.info(f"Crawling: {url}")
            response = await self.request_handler.fetch(url)
            if response:
                print(response[:200])

    def run(self):
        asyncio.run(self.crawl())