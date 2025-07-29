from TikTokApi import TikTokApi
import asyncio
import logging

async def scrape_trending(limit=100):
    try:
        logging.info("[SCRAPER] Scraping %s trending TikToks...", limit)
        async with TikTokApi() as api:
            trends = await api.trending(count=limit)
            logging.info("[SCRAPER] Success. First 3 trends:")
            for trend in trends[:3]:
                logging.info(f" - {trend.author.username} - {trend.desc[:40]}")
            return trends
    except Exception as e:
        logging.error(f"[ERROR] TikTok scraping failed: {e}")
        return []
