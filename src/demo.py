# src/demo.py

import os
import json
from trie import CompressedTrie
from trie_search import search_multi_ranked

# Determine project base directory
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Load the compressed trie from the inverted index
trie = CompressedTrie.from_inverted_index(
    os.path.join(BASE, "output", "inverted_index.json")
)
# Load the term frequency table for ranking
term_freq = json.load(
    open(os.path.join(BASE, "output", "term_frequency.json"), encoding="utf-8")
)

# Build a mapping from page ID to filename
PAGE_MAP = {}
for fname in sorted(os.listdir(os.path.join(BASE, "input_pages"))):
    if fname.endswith(".html"):
        pid = int(fname.replace("page", "").replace(".html", ""))
        PAGE_MAP[pid] = fname

def main():
    print("=== Simplified Search Engine Demo ===")
    print("Type space-separated keywords and press Enter to search.")
    print("Type 'exit' or 'quit' to leave the demo.")

    while True:
        line = input("\nSearch> ").strip()
        if not line or line.lower() in ("exit", "quit"):
            print("Exiting demo.")
            break

        # Prepare query words
        query = [w.lower() for w in line.split()]

        # Perform ranked multi-keyword search
        results = search_multi_ranked(query, trie, term_freq)

        if not results:
            print("No matching pages found.")
        else:
            print("Search results (ranked):")
            for rank, pid in enumerate(results, start=1):
                filename = PAGE_MAP.get(pid, f"page{pid}.html")
                print(f"  {rank}. [{pid}] {filename}")

if __name__ == "__main__":
    main()