from pip import main
import requests
import json

def avg_products_price(keyword):

    headers = {
        'Referer': 'https://msearch.shopping.naver.com/search/all?query={}'.format(keyword).encode('utf-8').decode('iso-8859-1'),
    }

    params = {
        'sort': 'rel',
        'pagingIndex': '1',
        'pagingSize': '40',
        'viewType': 'list',
        'productSet': 'total',
        'deliveryFee': '',
        'deliveryTypeValue': '',
        'query': keyword,
        'origQuery': keyword,
    }

    ## setting tor
    proxies = {
        'http': 'socks5://localhost:9050',
    }
    try:
        response = requests.get('https://msearch.shopping.naver.com/api/search/all', headers=headers, params=params, proxies=proxies)
    except requests.ConnectionError as ex:
        tor.renew_tor_ip(9051)
        print("ex = ", ex)
        print()
    else:
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