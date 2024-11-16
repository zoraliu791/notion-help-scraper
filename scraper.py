import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.notion.so/help'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

def get_article_links(base_url):
    response = requests.get(base_url, headers=HEADERS)
    if response.status_code != 200:
        print(f"Failed to retrieve the base page. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    article_links = set()

    # Example: Assuming articles are within <a> tags with a specific class or pattern
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if '/help/' in href and href not in article_links:
            # Normalize the URL
            full_url = href if href.startswith('http') else f"https://www.notion.so{href}"
            article_links.add(full_url)

    print(f"Found {len(article_links)} articles.")
    return list(article_links)

if __name__ == "__main__":
    links = get_article_links(BASE_URL)
    with open('article_links.txt', 'w') as f:
        for link in links:
            f.write(f"{link}\n")