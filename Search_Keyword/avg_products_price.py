from pip import main
import requests
import json

def avg_products_price(keyword):
    params = {
        'sort': 'rel',
        'pagingIndex': '1',
        'pagingSize': '40',
        'viewType': 'list',
        'productSet': 'total',
        'deliveryFee': '',
        'deliveryTypeValue': '',
        'frm': 'NVSHTTL',
        'query': keyword,
        'origQuery': keyword,
        'iq': '',
        'eq': '',
        'xq': '',
        'window': '',
    }

    response = requests.get('https://search.shopping.naver.com/api/search/all', params=params)

    response_json = json.loads(response.text)
    data_list =  response_json['shoppingResult']['products']

    price_list = []
    for data in data_list:
        price_list.append(float(data['price']))
    avg_products_price = sum(price_list)/len(price_list)

    return avg_products_price

if __name__ == "__main__" :
    keyword="애플워치"
    avg_products_price = avg_products_price(keyword)

    print("avg_products_price : ", avg_products_price)