# main.py

import logging
from scraper.tiktok_scraper import scrape_trending

logging.basicConfig(level=logging.DEBUG)
logging.debug("main.py started")

scrape_trending(100)
