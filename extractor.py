import time

import requests
from bs4 import BeautifulSoup

from scraper import HEADERS, get_article_links, BASE_URL


def extract_text_from_article(url):
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"Failed to retrieve {url}. Status code: {response.status_code}")
        return ""

    soup = BeautifulSoup(response.text, 'html.parser')

    content = []

    title_tag = soup.find('h1')
    if title_tag:
        content.append(title_tag.get_text(strip=True))

    for element in soup.find_all(['h2', 'h3', 'p', 'li']):
        text = element.get_text(strip=True)
        if text:
            content.append(text)

    article_text = '\n\n'.join(content)
    return article_text

def scrape_all_articles(links):
    articles = {}
    for idx, link in enumerate(links, 1):
        print(f"Scraping article {idx}/{len(links)}: {link}")
        text = extract_text_from_article(link)
        if text:
            articles[link] = text
        time.sleep(1)
    return articles

if __name__ == "__main__":
    links = get_article_links(BASE_URL)
    articles = scrape_all_articles(links)
    import json
    with open('articles.json', 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)