import requests
from bs4 import BeautifulSoup
import os
import time

class Get_link:
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


    def get_product_name(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title_tag = soup.find_all('span', {'class': 'a-size-base-plus a-color-base a-text-normal'})

        product_names = set()

        for item in title_tag:
            product_name = item.text.strip()
            product_names.add(product_name)
        return product_names

    # def write_file(self):
    #     with open('links.txt','w') as f:
    #         for i,link in enumerate(self.get_all_links()):
    #             f.write(f'{i+1}. {link}\n\n')
    #
    #     with open('product_name.txt', 'w') as f:
    #         for i,product_name in enumerate(self.get_product_name()):
    #             f.write(f'{i+1}. {product_name}\n\n')



# tmp = Get_link('https://www.amazon.co.jp/-/en/dp/B08MPWLJFT/ref=sr_1_10?keywords=%E3%83%8A%E3%82%A4%E3%83%95&qid=1677491754&s=home&sprefix=kni%2Ckitchen%2C903&sr=1-10')
# tmp.write_file()

