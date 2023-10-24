import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import pandas as pd

def get_headers(url):
    headers = {}
    
    try:
        response = requests.get(url)
        headers = response.headers
    except requests.exceptions.RequestException as e:
        print("Error making the request:", e)
    
    return headers

def get_secure_http_only_cookies(response):
    secure_http_only_cookies = []
    
    for cookie in response.cookies:
        secure = "Secure" in cookie._rest.keys()
        http_only = "HttpOnly" in cookie._rest.keys()
        
        if secure and http_only:
            secure_http_only_cookies.append(cookie)
    
    return secure_http_only_cookies

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

def analyze_url(url):
    response = requests.get(url)
    headers = response.headers
    vulnerabilities = []
    
    if not hasattr(analyze_url, 'cookies_analyzed'):
        secure_http_only_cookies = get_secure_http_only_cookies(response)
        if not secure_http_only_cookies:
            vulnerabilities.append("Falta de atributos Secure y http-only")
        elif any("Secure" not in cookie._rest.keys() for cookie in secure_http_only_cookies):
            vulnerabilities.append("Falta de atributo Secure")
        analyze_url.cookies_analyzed = True
    
    x_frame_options = headers.get("X-Frame-Options")
    content_security_policy = headers.get("Content-Security-Policy")
    
    if x_frame_options is None or content_security_policy is None:
        vulnerabilities.append("Posible Clickjacking")
    
    return {"link": url, "vulnerabilidad": ", ".join(vulnerabilities)}

def clickjacker(host):
    start_url = host  
    max_depth = 3 
    
    results = []
    queue = [(start_url, 1)]
    base_domain = urlparse(host).netloc
    
    while queue:
        current_url, depth = queue.pop(0)
        if depth > max_depth or urlparse(current_url).netloc != base_domain:
            continue
        
        print("Crawling:", current_url)
        
        result = analyze_url(current_url)
        results.append(result)
        
        linked_urls = get_links_on_page(current_url)
        for link in linked_urls:
            queue.append((link, depth + 1))
    
    df = pd.DataFrame(results)
    return {'Cabeceras': df} 

if __name__=="__main__":
    host="http://172.16.77.130:80"
    clickjacker(host)
