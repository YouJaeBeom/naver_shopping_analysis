import requests
import json
import tor

def products_count(keyword):
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
        response = requests.get('https://msearch.shopping.naver.com/api/search/all', params=params, proxies=proxies, headers=headers)
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