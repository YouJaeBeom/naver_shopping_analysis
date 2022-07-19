import requests
import json
import tor

def products_count(keyword):
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
    ## setting tor
    proxies = {
        'http': 'socks5://127.0.0.1:9050',
    }
    try:
        response = requests.get('https://search.shopping.naver.com/api/search/all', params=params)
    except requests.ConnectionError as ex:
        tor.renew_tor_ip(9051)
        print("ex = ", ex)
        print()
    else:
        response_json = json.loads(response.text)
        total_count =  response_json['shoppingResult']['total']

        return  total_count 

if __name__ == "__main__" :
    keyword="마스크"
    total_count= products_count(keyword)
    print(total_count)