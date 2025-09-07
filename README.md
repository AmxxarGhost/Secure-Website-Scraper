# 🔒 Secure Web Scraper

A Python-based web scraper that extracts structured data (metadata, headings, paragraphs, links, images) from websites, with a focus on **cybersecurity best practices**. The scraper uses an interactive **menu-driven CLI**, allowing users to choose what data they want to extract.

## ✨ Features
- Extracts:
  - Page title and meta description
  - Headings (`<h1>` – `<h6>`)
  - Paragraph text
  - Links with anchor text + URLs
  - Images with `alt` text + source

- **Interactive menu** to select what to view

- **Cybersecurity-aware design**:
  - Error handling and timeouts on requests
  - Custom User-Agent header
  - Output sanitization with `html.escape`
  - Safe URL validation (flags suspicious links)
  - Graceful failure on network errors

## 🛠️ Tech Stack
- **Python 3.12+**
- [Requests](https://pypi.org/project/requests/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [lxml](https://pypi.org/project/lxml/) (for faster parsing, optional)



