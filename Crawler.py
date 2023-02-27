import requests
from bs4 import BeautifulSoup
import  os
import time

import requests
from bs4 import BeautifulSoup

class LinkCrawler:
    def __init__(self, url):
        self.url = url

    def get_all_links(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')

        all_link = set()
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            if href is not None:
                if not href.startswith('http'or 'https'):
                    href = self.url + href
                all_link.add(href)
        return all_link
        # links = {link.get('href') for link in soup.find_all('a')}
        # return links
    def write_file(self):
        with open('links.txt','w') as f:
            for link in self.get_all_links():
                f.write(link+'\n')


