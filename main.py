import asyncio
import logging
from scraper.tiktok_scraper import scrape_trending

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    logging.debug("main.py started")
    asyncio.run(scrape_trending(100))
