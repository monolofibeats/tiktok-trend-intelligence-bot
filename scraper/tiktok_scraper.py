from TikTokApi import TikTokApi
import time

def scrape_tiktok_trends(limit=100):
    api = TikTokApi()

    print(f"[SCRAPER] Scraping {limit} trending TikToks...")
    try:
        trending = api.trending(count=limit)
    except Exception as e:
        print(f"[ERROR] TikTok scraping failed: {e}")
        return []

    results = []
    for video in trending:
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

