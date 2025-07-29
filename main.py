print("[BOOT] Trend Intelligence Bot starting...")

import asyncio
from scraper.tiktok_scraper import scrape_tiktok_trends
from db.database import save_to_json

if __name__ == "__main__":
    print("[MAIN] Starting async scrape...")
    trends = asyncio.run(scrape_tiktok_trends(limit=100))

    print(f"[MAIN] Scrape complete. Found: {len(trends)} videos")
    if trends:
        save_to_json(trends)
