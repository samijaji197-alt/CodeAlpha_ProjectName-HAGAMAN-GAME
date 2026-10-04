import re
import requests

# --- Configuration ---
URL = "https://www.python.org"      # the fixed webpage to scrape
OUTPUT_FILE = "page_title.txt"      # where the title gets saved

# Regex pattern to pull out whatever is between <title> and </title>
TITLE_PATTERN = r"<title[^>]*>(.*?)</title>"


def fetch_page(url):
    """Download the raw HTML of the page. Returns None if it fails."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # raises an error for bad status codes (404, 500, etc.)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch the page: {e}")
        return None


def extract_title(html):
    """Find and return the page title from raw HTML, or None if not found."""
    match = re.search(TITLE_PATTERN, html, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(1).strip()
    return None


def save_title(title, filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(title + "\n")


def main():
    print("=== Webpage Title Scraper ===\n")
    print(f"Fetching: {URL}")

    html = fetch_page(URL)
    if html is None:
        return

    title = extract_title(html)
    if title is None:
        print("Could not find a <title> tag on that page.")
        return

    save_title(title, OUTPUT_FILE)
    print(f"\nPage title: {title}")
    print(f"Saved to '{OUTPUT_FILE}'.")


if __name__ == "__main__":
    main()
