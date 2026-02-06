import os
import time
import argparse
import zipfile
import threading
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlunparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

BASE_URL = "https://docs.sui.io"
SITEMAP = BASE_URL + "/sitemap.xml"

lock = threading.Lock()

session = requests.Session()
session.headers.update({"User-Agent": "SuiDocsCrawler/2.0"})


# ---------- helpers ----------

def normalize(url):
    parsed = urlparse(url)
    clean = parsed._replace(fragment="", query="")
    url = urlunparse(clean)
    return url.rstrip("/")


def is_valid_doc(url):
    return urlparse(url).netloc == "docs.sui.io" and not url.endswith(".md")


def to_md(url):
    return normalize(url) + ".md"


def filename(url):
    path = urlparse(url).path.strip("/") or "index"
    return path.replace("/", "_") + ".md"


# ---------- retry wrapper ----------

def fetch(url, retries=3, delay=0.5):
    for i in range(retries):
        try:
            r = session.get(url, timeout=15)
            if r.status_code == 200:
                return r
        except:
            pass

        time.sleep(delay * (2 ** i))

    return None


# ---------- sitemap parsing ----------

def parse_sitemap():
    print("📍 Parsing sitemap...")
    urls = set()

    r = fetch(SITEMAP)
    if not r:
        print("⚠ Sitemap unavailable — falling back to crawl")
        return urls

    soup = BeautifulSoup(r.text, "xml")

    for loc in soup.find_all("loc"):
        url = normalize(loc.text)
        if is_valid_doc(url):
            urls.add(url)

    return urls


# ---------- crawler fallback ----------

def crawl(seed):
    print("🔍 Crawling site...")
    visited = set()
    queue = [seed]

    while queue:
        url = normalize(queue.pop(0))
        if url in visited:
            continue

        r = fetch(url)
        if not r:
            continue

        visited.add(url)

        soup = BeautifulSoup(r.text, "html.parser")

        for a in soup.find_all("a", href=True):
            link = normalize(urljoin(BASE_URL, a["href"]))

            if is_valid_doc(link) and link not in visited:
                queue.append(link)

    return visited


# ---------- downloader worker ----------

def download_one(url, outdir, combined, rate, incremental):
    md_url = to_md(url)
    fname = filename(url)
    path = os.path.join(outdir, fname)

    if incremental and os.path.exists(path):
        return

    r = fetch(md_url)
    if not r:
        return

    content = r.text

    with lock:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        combined.write(f"\n\n---\nSOURCE: {md_url}\n---\n\n")
        combined.write(content)

    time.sleep(rate)


# ---------- zip export ----------

def zip_output(folder):
    print("📦 Creating ZIP archive...")
    zipname = folder + ".zip"

    with zipfile.ZipFile(zipname, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(folder):
            for file in files:
                path = os.path.join(root, file)
                z.write(path, arcname=file)

    print("ZIP created:", zipname)


# ---------- main ----------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--threads", type=int, default=8)
    parser.add_argument("--rate", type=float, default=0.05)
    parser.add_argument("--out", default="sui_docs_md")
    parser.add_argument("--incremental", action="store_true")
    parser.add_argument("--zip", action="store_true")

    args = parser.parse_args()

    os.makedirs(args.out, exist_ok=True)

    urls = parse_sitemap()

    if not urls:
        urls = crawl(BASE_URL)

    print(f"📚 Found {len(urls)} pages")

    combined_path = "combined.md"

    with open(combined_path, "w", encoding="utf-8") as combined:

        with ThreadPoolExecutor(max_workers=args.threads) as pool:
            futures = [
                pool.submit(
                    download_one,
                    url,
                    args.out,
                    combined,
                    args.rate,
                    args.incremental,
                )
                for url in urls
            ]

            for _ in tqdm(as_completed(futures), total=len(futures)):
                pass

    if args.zip:
        zip_output(args.out)

    print("\n✅ Done!")


if __name__ == "__main__":
    main()
