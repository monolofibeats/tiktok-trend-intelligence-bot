import asyncio
from scraper.tiktok_scraper import scrape_tiktok_trends
from db.database import save_to_json

if __name__ == "__main__":
    trends = asyncio.run(scrape_tiktok_trends(limit=100))
    if trends:
        save_to_json(trends)
