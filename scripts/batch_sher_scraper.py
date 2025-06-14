import requests
from bs4 import BeautifulSoup
import json
import time
import os

headers = {
    "User-Agent": "Mozilla/5.0"
}

def scrape_poet_shers(poet_name, poet_url):
    print(f"📜 Scraping shayari of: {poet_name}")
    shers = []

    try:
        response = requests.get(poet_url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        shers_html = soup.find_all("div", class_="poemRender")

        for sher_div in shers_html:
            lines = [line.strip() for line in sher_div.stripped_strings]
            if len(lines) >= 2:
                shers.append({
                    "poet": poet_name,
                    "city": "Lucknow",
                    "couplet": lines[:2],
                    "themes": []
                })

    except Exception as e:
        print(f"❌ Error scraping {poet_name}: {e}")

    return shers


def save_batch(batch_shers, batch_index):
    os.makedirs("data", exist_ok=True)
    filename = f"data/raw_shers_batch{batch_index}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(batch_shers, f, indent=4, ensure_ascii=False)
    print(f"✅ Batch {batch_index} saved to {filename}")


def scrape_poet_batch(batch_links: dict, batch_index: int, delay=3):
    batch_data = []
    for poet, url in batch_links.items():
        batch_data.extend(scrape_poet_shers(poet, url))
        print(f"⏳ Waiting {delay} seconds before next poet...")
        time.sleep(delay)
    save_batch(batch_data, batch_index)


def run_all_batches(all_batches, delay_between_batches=600):
    for idx, batch in enumerate(all_batches, 1):
        print(f"\n=== 🧿 Starting Batch {idx} ===")
        scrape_poet_batch(batch, batch_index=idx)
        if idx < len(all_batches):
            print(f"🌙 Cooling off... waiting {delay_between_batches//60} minutes before next batch...\n")
            time.sleep(delay_between_batches)
    print("\n🏁 All batches completed successfully!")
