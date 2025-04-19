# Simplified Search Engine

This project implements a simplified search engine for a small set of local HTML pages, based on the algorithms and data structures from **Section 23.6** of the textbook (tries, compressed tries, inverted indexes). It supports single- and multi-keyword queries with a basic ranking mechanism.

---

## 🚀 Features

- **HTML Parsing & Tokenization**: Extract visible text from HTML files, normalize & tokenize, remove stop words.
- **Term Frequency & Inverted Index**: Build a term frequency table and an inverted index (`word → [page IDs]`).
- **Compressed Trie**: Store index terms in a compressed trie for fast lookup.
- **Query Interface**:
  - **Single-word search**: Find pages containing a given keyword.
  - **Multi-word search**: Compute intersection of per-word results.
- **Ranking**: Sort multi-keyword results by total term frequency (descending).
- **Demo CLI**: Interactive command‑line demo script covering lookup and ranking.

---

## 📁 Directory Structure

```
search-engine-project/
├── environment.yml          # Conda environment configuration
├── input_pages/             # Local HTML pages (e.g. page1.html … pageN.html)
├── output/                  # Generated data
│   ├── term_frequency.json  # word → {page_id: count}
│   └── inverted_index.json  # word → [page_id, ...]
├── src/                     # Source code
│   ├── parser.py            # Extract text, build term frequency & inverted index
│   ├── trie.py              # CompressedTrie implementation
│   ├── trie_search.py       # Query functions and ranking logic
│   └── demo.py              # CLI demo script
└── demo/                    # Video demonstration (demo.mp4)
```

---

## 🔧 Environment Setup

1. Install Anaconda or Miniconda.
2. Create and activate the `search-engine` environment:
   ```bash
   conda env create -f environment.yml
   conda activate search-engine
   ```
3. Download NLTK data (first time only):
   ```bash
   python - <<EOF
import nltk
nltk.download("stopwords")
nltk.download("punkt")
EOF
   ```

---

## 📝 Workflow

### 1. Prepare Input Pages

- Place 5–10 local HTML files into `input_pages/`. Ensure at least one local hyperlink connects them (e.g. `<a href="page2.html">Next</a>`).

### 2. Parse & Build Indexes

Run the parser to extract text, build term frequencies and the inverted index:
```bash
python src/parser.py
```
- Outputs:
  - `output/term_frequency.json`
  - `output/inverted_index.json`

### 3. Build & Query Compressed Trie

Test single- and multi-keyword searches:
```bash
python src/trie_search.py
```
- Validates Trie construction and ranking logic.

### 4. Interactive Demo

Launch the CLI demo for ad-hoc searches:
```bash
python src/demo.py
```
- Enter space-separated keywords at the `Search>` prompt.
- Results are printed in ranked order.
- Type `exit` or `quit` to end.

---

## 🎥 Demo Video

A short demo video (`demo/demo.mp4`) illustrates:
1. Environment activation and directory overview
2. Running `parser.py` to generate indexes
3. Running `demo.py` with example queries
4. Exiting the demo

---

## 📚 References

- **Textbook**: Section 23.6, Tries and Search Engines
- **Libraries**:
  - [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
  - [NLTK](https://www.nltk.org/)

---

_This project demonstrates the core principles of information retrieval in a self-contained setting._

