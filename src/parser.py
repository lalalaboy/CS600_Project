# src/parser.py

import os
import json
import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords


BASE_DIR   = "/Users/zunze/Desktop/search-engine-project"
INPUT_DIR  = os.path.join(BASE_DIR, "input_pages")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)


STOP_WORDS = set(stopwords.words("english"))  


def extract_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose()
    return soup.get_text(separator=" ")

def tokenize(text: str) -> list[str]:
    tokens = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    return [w for w in tokens if w not in STOP_WORDS]


def build_term_frequency() -> dict[str, dict[int, int]]:

    tf: dict[str, dict[int, int]] = {}
    for fname in sorted(os.listdir(INPUT_DIR)):
        if not fname.endswith(".html"):
            continue
        pid = int(fname.replace("page", "").replace(".html", ""))
        html = open(os.path.join(INPUT_DIR, fname), encoding="utf-8").read()
        words = tokenize(extract_text(html))
        for w in words:
            tf.setdefault(w, {}).setdefault(pid, 0)
            tf[w][pid] += 1
    return tf

def save_term_frequency(tf: dict[str, dict[int, int]]):
    out = os.path.join(OUTPUT_DIR, "term_frequency.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(tf, f, ensure_ascii=False, indent=2)
    print("► 写入 词频 表：", out)


def build_inverted_index(tf: dict[str, dict[int, int]]) -> dict[str, list[int]]:
    idx = {w: sorted(list(pages.keys())) for w, pages in tf.items()}
    return idx

def save_index(index: dict[str, list[int]]):
    out = os.path.join(OUTPUT_DIR, "inverted_index.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    print("► 写入 倒排索引：", out)


if __name__ == "__main__":
    tf = build_term_frequency()
    save_term_frequency(tf)
    idx = build_inverted_index(tf)
    save_index(idx)