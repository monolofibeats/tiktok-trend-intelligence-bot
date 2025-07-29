# scraper/tiktok_scraper.py

import logging
from TikTokApi import TikTokApi

def scrape_trending(limit=100):
    logging.debug("[SCRAPER] Scraping %s trending TikToks...", limit)

    try:
        api = TikTokApi()
        trending = api.trending(count=limit)
        trends = []

        for video in trending:
            trends.append({
                "id": video.id,
                "author": video.author.username,
                "desc": video.desc,
                "stats": video.stats.dict()
            })

        logging.debug("[SCRAPER] Success. First 3 trends: %s", trends[:3])
        return trends

    except Exception as e:
        logging.error("[ERROR] TikTok scraping failed: %s", e)
        return []
