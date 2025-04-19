# src/download_pages.py
import os, requests

BASE_DIR = "/Users/zunze/Desktop/search-engine-project/input_pages"
os.makedirs(BASE_DIR, exist_ok=True)

urls = [
    "https://en.wikipedia.org/wiki/Apple",
    "https://en.wikipedia.org/wiki/Banana",
    "https://zh.wikipedia.org/wiki/Orange",
    "https://en.wikipedia.org/wiki/Watermelon",
    "https://en.wikipedia.org/wiki/Grape",
    "https://en.wikipedia.org/wiki/Potato",
  # … 
]

for i, url in enumerate(urls, start=1):
    try:
        r = requests.get(url)
        r.raise_for_status()
        out_path = os.path.join(BASE_DIR, f"page{i}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(r.text)
        print(f"Saved {out_path}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")