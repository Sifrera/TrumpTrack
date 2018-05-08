import urllib.request
from bs4 import BeautifulSoup
import os

path = os.path.join("/home", "pi", "Documents", "links.txt")

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        response = urllib.request.urlopen(self.site)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        with open(path, 'w') as f:
            for tag in soup.find_all("a"):
                url = tag.get("href")
                if url and "html" in url:
                    f.write('\n' + url)

Scraper('https://news.google.com/').scrape()
