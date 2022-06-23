
from bs4 import BeautifulSoup
import requests
import json
def most_viewed_products(cid,period):
    params = {
        'categoryCategoryId': cid,
        'categoryChildCategoryId': '',
        'categoryDemo': 'M04',
        'categoryMidCategoryId': '',
        'categoryRootCategoryId': cid,
        'period': period,
    }

    response = requests.get('https://search.shopping.naver.com/best/_next/data/NurwgmMcJVwLajFklX6sM/category/click.json', params=params)
    response_json = json.loads(response.text)
    products =  response_json['pageProps']['dehydratedState']['queries'][2]['state']['data']['products']

    return products

if __name__ == "__main__":
    # cid -> ALL or 5000000 etc..
    cid = "ALL"

    # period -> P1D or P7D
    period = "P7D"
    print(most_viewed_products(cid,period))
