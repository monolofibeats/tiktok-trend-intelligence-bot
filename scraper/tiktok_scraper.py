from TikTokApi import TikTokApi

async def scrape_tiktok_trends(limit=100):
    print(f"[SCRAPER] Scraping {limit} trending TikToks...")

    try:
        async with TikTokApi() as api:
            await api.create_sessions()

            results = []
            # NEW: Use api.feed.trending instead of api.trending()
            async for video in api.feed.trending():
                results.append({
                    "id": video.id,
                    "desc": video.desc,
                    "author": video.author.username,
                    "plays": video.stats.play_count,
                    "likes": video.stats.like_count,
                    "shares": video.stats.share_count,
                    "comments": video.stats.comment_count,
                    "saves": video.stats.save_count,
                    "music_title": video.music.title,
                    "music_author": video.music.author,
                })

                if len(results) >= limit:
                    break

            return results

    except Exception as e:
        print(f"[ERROR] TikTok scraping failed: {e}")
        return []
