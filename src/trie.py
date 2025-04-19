# src/trie.py

import json
from typing import Dict, List, Optional

class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.occurrence_list: Optional[List[int]] = None

class CompressedTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, pages: List[int]):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.occurrence_list = pages

    def compress(self):

        def _compress(node: TrieNode):
            for key, child in list(node.children.items()):
                _compress(child)

                if child.occurrence_list is None and len(child.children) == 1:
                    sub_key, grand = next(iter(child.children.items()))
                    new_key = key + sub_key
                    node.children[new_key] = grand
                    del node.children[key]
                    _compress(node)
                    break
        _compress(self.root)

    @classmethod
    def from_inverted_index(cls, path: str) -> "CompressedTrie":
        trie = cls()
        with open(path, encoding="utf-8") as f:
            index = json.load(f)
        for word, pages in index.items():
            trie.insert(word, pages)
        trie.compress()
        return trie