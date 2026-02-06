# Sui Docs Markdown Downloader

A fast, production-grade crawler that downloads **all Sui documentation pages** as Markdown files and optionally combines them into a single dataset.

This tool uses sitemap parsing + crawling to discover pages, downloads `.md` exports, and supports multithreading, retries, rate limiting, and incremental sync.

Perfect for:

- Offline documentation archive
- LLM dataset preparation
- Knowledge base ingestion
- Research or indexing

---

## ✨ Features

- ⚡ Multithreaded downloads
- 🔁 Retry with exponential backoff
- 🗺 Sitemap parsing (fast discovery)
- 🔍 Fallback crawler
- 🧠 Incremental sync (resume-safe)
- 🐢 Rate limiting (server-friendly)
- 📦 ZIP export
- 🧵 Thread-safe combined Markdown output
- 🖥 CLI arguments

---

## 📦 Requirements

- Python 3.9+
- [uv](https://github.com/astral-sh/uv) (recommended package manager)

---

## 🚀 Installation

Clone the repo:

```bash
git clone https://github.com/YOURNAME/sui-docs-downloader.git
cd sui-docs-downloader
```

Install dependencies:

```bash
uv sync
```

_or manually:_

```bash
uv add requests beautifulsoup4 tqdm lxml
```

---

## ▶ Basic Usage

Run downloader:

```bash
uv run downloader.py
```

---

## ⚙ Advanced Usage

### Faster multithread download

```bash
uv run downloader.py --threads 16
```

### Incremental sync (skip existing files)

```bash
uv run downloader.py --incremental
```

### Polite rate-limited crawl

```bash
uv run downloader.py --rate 0.2
```

### ZIP export

```bash
uv run downloader.py --zip
```

### Full power mode

```bash
uv run downloader.py \
  --threads 16 \
  --incremental \
  --rate 0.1 \
  --zip
```

---

## 📁 Output Structure

```
project/
│
├── sui_docs_md/       → individual markdown files
│   ├── guides.md
│   ├── concepts.md
│   └── ...
│
└── combined.md        → all docs merged
```

Each section in `combined.md` is labeled with its original source URL.

---

## 🧠 CLI Options

| Flag            | Description                       |
| --------------- | --------------------------------- |
| `--threads`     | Number of parallel downloads      |
| `--rate`        | Delay between downloads (seconds) |
| `--out`         | Output directory                  |
| `--incremental` | Skip already downloaded files     |
| `--zip`         | Create ZIP archive                |

---

## ⚠ Notes

- Designed specifically for Sui docs `.md` export
- Rate limiting helps avoid overwhelming servers
- Incremental mode allows safe re-runs

---

## 🤝 Contributing

Pull requests welcome!

Ideas:

- Progress persistence
- JSON index export
- Vector DB formatting
- Dataset splitting
- HTML fallback parsing

---

## 📜 License

MIT — use freely.

---

## ⭐ Support

If this tool helped you, consider starring the repo!
