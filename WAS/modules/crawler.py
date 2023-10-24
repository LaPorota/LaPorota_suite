import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import pandas as pd

def web_crawler(start_url, max_depth=3):
    def get_links_on_page(url):
        links = []
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            for link in soup.find_all("a"):
                href = link.get("href")
                if href and not href.startswith("#"):
                    absolute_url = urljoin(url, href)
                    links.append(absolute_url)
        except requests.exceptions.RequestException as e:
            print("Error making the request:", e)
        return links
    
    results = []
    queue = [(start_url, 1)]
    base_domain = urlparse(start_url).netloc
    
    while queue:
        current_url, depth = queue.pop(0)
        if depth > max_depth or urlparse(current_url).netloc != base_domain:
            continue
        
        print("Crawling:", current_url)
        
        linked_urls = get_links_on_page(current_url)
        for link in linked_urls:
            queue.append((link, depth + 1))
    
    return results



if __name__ == "__main__":
    host = "https://claropay.com.ar"
    crawled_data = web_crawler(host)
    print(crawled_data)
