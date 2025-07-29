import json
from datetime import datetime
import os

def save_to_json(data, folder="scraped_data"):
    # Create folder if it doesn't exist
    os.makedirs(folder, exist_ok=True)

    # Create filename with current date
    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.json")
    filepath = os.path.join(folder, filename)

    # Save data
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"[DB] Saved {len(data)} items to {filepath}")
