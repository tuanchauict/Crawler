import json

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.amazon.co.jp/s?k={}&page={}"
HEADERS = {'User-Agent': 'Mozilla/5.0'}


class ProductFetcher:

    def fetch_products(self, keyword, page_count):
        products = []
        for page in range(page_count):
            products += self._fetch_page(keyword, page)

        return products

    def _fetch_page(self, keyword, page):
        page_url = BASE_URL.format(keyword, page + 1)
        response = requests.get(page_url, headers=HEADERS)
        return ProductParser.parse(BeautifulSoup(response.content, 'html.parser'))


class ProductParser:

    @staticmethod
    def parse(html):
        products = html.select("div[data-component-type='s-search-result']")
        return [ProductParser._parse_single_item(item) for item in products]

    @staticmethod
    def _parse_single_item(item_node):
        rating = item_node.find('span', {'class': 'a-icon-alt'})

        return {
            "name": item_node.find('span', class_='a-size-base-plus a-color-base a-text-normal')
            .text.strip(),
            "price": item_node.find('span', class_='a-offscreen').text.strip(),
            "url": f"https://www.amazon.co.jp{item_node.find('a', class_='a-link-normal')['href']}",
            "thumbnail_url": item_node.find('img', class_='s-image')['src'],
            "rating": rating.text.strip().split()[0] if rating is not None else None
        }


class ProductStorage:

    @staticmethod
    def save(keyword, products):
        with open(keyword, 'w', encoding='utf-8') as f:
            json.dump(products, f, ensure_ascii=False, indent=4)


def main(keyword, page_count):
    fetcher = ProductFetcher()
    products = fetcher.fetch_products(keyword, page_count)
    ProductStorage.save(keyword, products)


if __name__ == '__main__':
    keyword = input("Enter the keyword: ")
    page_count = int(input("Enter number of pages: "))
    main(keyword, page_count)