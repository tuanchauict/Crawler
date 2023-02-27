import requests
from bs4 import BeautifulSoup

class Get_infor_product:
    def __init__(self, url):
        self.url = url


    def get_product_name(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title_tag = soup.find_all('span', {'id': 'productTitle'})

        product_names = set()

        for item in title_tag:
            product_name = item.text.strip()
            product_names.add(product_name)
        return product_names

    def get_product_price(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        product_price = set()

        price_tag = soup.find_all('span',{'class':'a-price-whole'})

        for item in price_tag:
            product_price = item.text.strip()
            product_price.add(product_price)
        return product_price

    def write_file(self):
        with open('product_name.txt', 'w') as f:
            for i,product_name in enumerate(self.get_product_name()):
                f.write(f'{i+1}. {product_name}\n\n')

        with open('prouct_price.txt','w') as f:
            for i, product_price in enumerate(self.get_product_price()):
                f.write(f'{i+1}. {product_price}\n\n')

    # def write_file(self):
    #     with open('product_name.txt', 'w') as f:
    #         for i,product_name in enumerate(self.get_product_name()):
    #             f.write(f'{i+1}. {product_name}\n\n')
    #
    #     with open('product_price.txt', 'w') as f:
    #         for i,product_price in enumerate(self.get_product_price()):
    #             f.write(f'{i+1}. {product_price}\n\n')


tmp = Get_infor_product('')
tmp.write_file()