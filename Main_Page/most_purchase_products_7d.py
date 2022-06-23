import requests
import json

def most_purchase_products_7d():
    params = {
        'categoryCategoryId': 'ALL',
        'categoryChildCategoryId': '',
        'categoryDemo': 'M04',
        'categoryMidCategoryId': '',
        'categoryRootCategoryId': 'ALL',
        'period': 'P7D',
    }

    response = requests.get('https://search.shopping.naver.com/best/_next/data/NurwgmMcJVwLajFklX6sM/category/purchase.json', params=params)
    response_json = json.loads(response.text)
    products =  response_json['pageProps']['dehydratedState']['queries'][2]['state']['data']['products']

    return products

if __name__ == "__main__":
    print(most_purchase_products_7d())