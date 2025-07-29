from TikTokApi import TikTokApi
import asyncio

async def scrape_tiktok_trends(limit=100):
    async with TikTokApi() as api:
        await api.create_sessions()
        trending = api.trending()

        results = []
        async for video in trending:
            results.append({
                "id": video.id,
                "desc": video.desc,
                "author": video.author.username,
                "stats": video.stats,
            })
            if len(results) >= limit:
                break

        return results

    except Exception as e:
        print(f"[ERROR] TikTok scraping failed: {e}")
        return []
