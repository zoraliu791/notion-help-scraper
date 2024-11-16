
# Notion Article Scraper Project

This project is a Python-based web scraping tool designed to extract and process articles from the Notion Help website. The workflow is divided into four separate scripts, each handling specific responsibilities: scraping, extracting content, chunking, and prettifying the text.

---

### Prerequisites

- Python 3.7 or higher
- `requests` library
- `beautifulsoup4` library
- `json` module (built-in)
- A basic understanding of web scraping and JSON data handling.

Install required libraries using:
```bash
pip install requests beautifulsoup4
```

---

### Files Overview

#### 1. **scraper.py**

This script handles the extraction of article links from the base URL of the Notion Help website.

**Key Functions:**
- `get_article_links(base_url)`: Scrapes the base page and collects article links.

**Usage Example:**
```bash
python scraper.py
```
**Output:**
- Saves a list of article links to `article_links.txt`.

---

#### 2. **extractor.py**

This script extracts the textual content from each article URL.

**Key Functions:**
- `extract_text_from_article(url)`: Scrapes the title and main content from a given article.
- `scrape_all_articles(links)`: Loops through all article links to fetch their content.

**Usage Example:**
```bash
python extractor.py
```
**Output:**
- Saves all article content in a structured JSON format to `articles.json`.

---

#### 3. **chunker.py**

This script splits the extracted article text into smaller chunks for easier processing or analysis.

**Key Functions:**
- `chunk_text(text, max_length=750)`: Splits the text into smaller parts, ensuring no chunk exceeds the specified character limit.
- `chunk_all_articles(articles)`: Applies `chunk_text` to all articles.

**Usage Example:**
```bash
python chunker.py
```
**Output:**
- Saves text chunks to `chunks.json`.

---

#### 4. **prettifier.py**

This script cleans up and formats the text chunks for better readability.

**Key Functions:**
- `prettify_text(text)`: Cleans up unnecessary whitespace and formatting issues.
- `prettify_all_chunks(chunks)`: Applies `prettify_text` to all chunks.

**Usage Example:**
```bash
python prettifier.py
```
**Output:**
- Saves prettified text chunks to `prettified_chunks.json`.

---

### Workflow Overview

1. **Run `scraper.py`**: Collect all article links from the Notion Help base URL.
2. **Run `extractor.py`**: Extract the content of all articles into a JSON file.
3. **Run `chunker.py`**: Split the content into smaller chunks for easy handling.
4. **Run `prettifier.py`**: Clean and format the chunks for better readability.

---

### Outputs

- `article_links.txt`: A plain text file containing all scraped article URLs.
- `articles.json`: A JSON file with the raw content of each article.
- `chunks.json`: A JSON file containing the chunked text.
- `prettified_chunks.json`: A JSON file with cleaned and formatted text chunks.

---

### Notes

- The project respects basic ethical guidelines for web scraping:
  - Includes headers in HTTP requests to mimic a browser.
  - Adds a `time.sleep(1)` delay between requests to avoid overloading the server.
- If the structure of the Notion Help website changes, the scraping logic may need to be updated.
