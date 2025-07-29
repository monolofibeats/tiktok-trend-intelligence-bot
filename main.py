import asyncio
from scraper.tiktok_scraper import scrape_tiktok_trends

async def main():
    print("[DEBUG] main.py started")

    try:
        print("[SCRAPER] Scraping 100 trending TikToks...")
        trends = await scrape_tiktok_trends(limit=100)
        print("[SCRAPER] Success. First 3 trends:")
        for trend in trends[:3]:
            print(trend)
    except Exception as e:
        print("[ERROR] TikTok scraping failed:", e)

if __name__ == "__main__":
    asyncio.run(main())
