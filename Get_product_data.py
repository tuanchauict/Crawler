import requests
import json
from bs4 import BeautifulSoup
import os

class Get_product_infor:
    def __init__(self):
        self.base_url = "https://www.amazon.co.jp/s?k={}&page={}"

    def get_products_data(self, soup):
        products = []
        for product in soup.select("div[data-component-type='s-search-result']"):
            product_data = {}
            try:
                product_data['Name'] = product.find('span', class_='a-size-base-plus a-color-base a-text-normal').text.strip()
                product_data['Price'] = product.find('span', class_='a-offscreen').text.strip()
                product_data['Link'] = "https://www.amazon.co.jp" + product.find('a', class_='a-link-normal')['href']
                product_data['Image'] = product.find('img', class_='s-image')['src']
                rating = product.find('span', {'class': 'a-icon-alt'})
                if rating is not None:
                    product_data['Rating'] = rating.text.strip().split()[0]
                else:
                    product_data['Rating'] = 'N/A'
                products.append(product_data)
            except:
                continue
        return products


    def Create_file(self, keyword):
        # Tạo thư mục chung cho tất cả các file JSON
        directory_name = keyword
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)

        pages = int(input("Enter number of pages to crawl: "))
        for i in range(1, pages + 1):
            page_url = self.base_url.format(keyword, i)
            file_name = f"{keyword}_{i}.json"
            try:
                response = requests.get(page_url, headers={'User-Agent': 'Mozilla/5.0'})
                soup = BeautifulSoup(response.content, 'html.parser')
                products = self.get_products_data(soup)
                data = {'products': products}
                file_path = os.path.join(directory_name, file_name)
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
            except:
                print(f"Error occurred while crawling {page_url}")


crawler = Get_product_infor()
keyword = input("Enter the product you want to get info: ")
crawler.Create_file(keyword)
