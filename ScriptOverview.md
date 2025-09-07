# Web Scraper Script

This Python script is a **menu-driven web scraper** that extracts structured information from a webpage. It uses the `requests` library to fetch web content and `BeautifulSoup` to parse and analyze HTML.

## Key Components

### 1. Safe HTTP Request
- Function: `safe_request(url)`
- Sends a GET request to the given URL with a custom `User-Agent` header.
- Includes a **timeout** of 10 seconds.
- Handles exceptions (`RequestException`) for network issues, invalid URLs, or HTTP errors.
- Exits the program gracefully if the request fails.

### 2. HTML Parsing
- Function: `scrape(url)`
- Fetches webpage content using `safe_request`.
- Parses HTML using `BeautifulSoup` with the `html.parser`.
- Returns a `BeautifulSoup` object for further processing.

### 3. Data Extraction Functions
- **Metadata** (`show_metadata`): Prints the page `<title>` and meta description.
- **Headings** (`show_headings`): Lists all headings from `<h1>` to `<h6>`.
- **Paragraphs** (`show_paragraphs`): Lists all text within `<p>` tags.
- **Links** (`show_links`): Extracts all `<a>` elements with `href` attributes.
  - Checks if URLs are safe (starting with `http` or `/`).
- **Images** (`show_images`): Extracts all `<img>` elements with `src` attributes.
  - Displays `alt` text and checks if sources are safe.

### 4. Interactive Menu
- Function: `menu(soup)`
- Provides a **console menu** to choose which data to display:
  1. Show Metadata
  2. Show Headings
  3. Show Paragraphs
  4. Show Links
  5. Show Images
  6. Show Everything
  0. Exit
- Users can repeatedly select options until they choose to exit.

### 5. HTML Safety
- Uses `html.escape()` to safely print HTML content, avoiding potential HTML injection issues.

## Usage
1. Set the target URL in the `url` variable.
2. Ensure `requests` and `beautifulsoup4` are installed by running `pip install [library]`.
3. Run the script:
   python secure-webscraper.py
