# src/trie_search.py

import json
from trie import CompressedTrie

def search_single(word: str, trie: CompressedTrie) -> list[int]:

    node = trie.root
    i = 0
    while i < len(word):
        for label, child in node.children.items():
            if word.startswith(label, i):
                i += len(label)
                node = child
                break
        else:
            return []
    return node.occurrence_list or []

def search_multi(words: list[str], trie: CompressedTrie) -> list[int]:

    sets = [set(search_single(w, trie)) for w in words]
    if not sets:
        return []
    res = sets[0]
    for s in sets[1:]:
        res &= s
    return sorted(res)

def rank_pages(pages: list[int], query: list[str], term_freq: dict) -> list[int]:
    scores = {p: 0 for p in pages}
    for w in query:
        freqs = term_freq.get(w, {})
        for p in pages:
            scores[p] += freqs.get(str(p), 0)
    return sorted(pages, key=lambda p: (-scores[p], p))

def search_multi_ranked(words: list[str], trie: CompressedTrie, term_freq: dict) -> list[int]:

    hit = set(search_single(words[0], trie))
    for w in words[1:]:
        hit &= set(search_single(w, trie))
    return rank_pages(sorted(hit), words, term_freq)

if __name__ == "__main__":
    trie = CompressedTrie.from_inverted_index("/Users/zunze/Desktop/search-engine-project/output/inverted_index.json")
    term_freq = json.load(open("/Users/zunze/Desktop/search-engine-project/output/term_frequency.json", encoding="utf-8"))

    for q in ["apple", "vitamin", "water"]:
        pages = search_single(q, trie)
        print(f"单词 {q} 出现在页面：{pages}")

    combo = ["apple", "vitamin"]
    print(f"同时包含 {combo} 的页面（未排序）：", search_multi(combo, trie))

    ranked = search_multi_ranked(combo, trie, term_freq)
    print(f"同时包含 {combo} 的页面（已排名）：", ranked)