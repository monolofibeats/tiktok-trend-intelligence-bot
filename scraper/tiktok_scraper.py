from TikTokApi import TikTokApi
import asyncio

async def scrape_tiktok_trends(limit=100):
    api = TikTokApi()
    results = []

    print(f"[SCRAPER] Scraping {limit} trending TikToks...")

    try:
        async for video in api.trending.videos(count=limit):
            try:
                data = {
                    "id": video.id,
                    "url": f"https://www.tiktok.com/@{video.author.username}/video/{video.id}",
                    "caption": video.desc,
                    "hashtags": [tag.name for tag in video.challenges],
                    "audio_title": video.music.title,
                    "audio_id": video.music.id,
                    "likes": video.stats.diggCount,
                    "shares": video.stats.shareCount,
                    "comments": video.stats.commentCount,
                    "created_at": video.create_time
                }
                results.append(data)
            except Exception as e:
                print(f"[ERROR] Failed to parse video: {e}")
                continue

        print(f"[SCRAPER] Fetched {len(results)} videos.")
        return results

    except Exception as e:
        print(f"[ERROR] TikTok scraping failed: {e}")
        return []
