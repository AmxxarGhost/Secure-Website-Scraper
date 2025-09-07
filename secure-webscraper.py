import requests  # type: ignore
from bs4 import BeautifulSoup
import html
import sys


def safe_request(url):
    """Safely request a webpage with error handling and headers."""
    headers = {
        "User-Agent": "WebScraperBot/1.0 (+https://yourdomain/contact)"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise error for bad status
        return response
    except requests.exceptions.RequestException as e:
        print(f"[!] Request failed: {e}")
        sys.exit(1)


def scrape(url):
    response = safe_request(url)
    return BeautifulSoup(response.text, "html.parser")


def show_metadata(soup):
    print("\n--- Page Metadata ---")
    print("Page Title:", html.escape(soup.title.string) if soup.title else "No title")
    meta_desc = soup.find("meta", attrs={"name": "description"})
    print("Meta Description:", html.escape(meta_desc["content"]) if meta_desc else "No description")


def show_headings(soup):
    print("\n--- Headings ---")
    for level in range(1, 7):
        headings = [html.escape(h.get_text(strip=True)) for h in soup.find_all(f"h{level}")]
        if headings:
            print(f"H{level}:", headings)


def show_paragraphs(soup):
    print("\n--- Paragraphs ---")
    paragraphs = [html.escape(p.get_text(strip=True)) for p in soup.find_all("p")]
    for i, p in enumerate(paragraphs, start=1):
        print(f"{i}. {p}")


def show_links(soup):
    print("\n--- Links ---")
    links = [(html.escape(a.get_text(strip=True)), a.get("href")) for a in soup.find_all("a", href=True)]
    for i, (text, href) in enumerate(links, start=1):
        safe_href = href if href and href.startswith(("http", "/")) else "Potentially unsafe link"
        print(f"{i}. Text: {text or 'No text'} | URL: {safe_href}")


def show_images(soup):
    print("\n--- Images ---")
    images = [(html.escape(img.get("alt", "No alt text")), img.get("src")) for img in soup.find_all("img", src=True)]
    for i, (alt, src) in enumerate(images, start=1):
        safe_src = src if src and src.startswith(("http", "/")) else "Potentially unsafe src"
        print(f"{i}. Alt: {alt} | Src: {safe_src}")


def menu(soup):
    while True:
        print("\nChoose an option:")
        print("1. Show Metadata")
        print("2. Show Headings")
        print("3. Show Paragraphs")
        print("4. Show Links")
        print("5. Show Images")
        print("6. Show Everything")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_metadata(soup)
        elif choice == "2":
            show_headings(soup)
        elif choice == "3":
            show_paragraphs(soup)
        elif choice == "4":
            show_links(soup)
        elif choice == "5":
            show_images(soup)
        elif choice == "6":
            show_metadata(soup)
            show_headings(soup)
            show_paragraphs(soup)
            show_links(soup)
            show_images(soup)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    url = "https://example.com/"
    soup = scrape(url)
    menu(soup)
