from pip import main
import requests
import json
import tor
def avg_products_price(keyword, top,repeat):
    price_list = []
    ## setting tor
    proxies = {
        'http': 'socks5://127.0.0.1:9050',
    }
    for pagenumber in range(1,repeat+1):
        params = {
            'sort': 'rel',
            'pagingIndex': str(pagenumber),
            'pagingSize': "40",
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
        try:
            response = requests.get('https://search.shopping.naver.com/api/search/all', params=params, proxies=proxies)
        except requests.ConnectionError as ex:
            tor.renew_tor_ip(9051)
            print("ex = ", ex)
            print()
        else:
            response_json = json.loads(response.text)
            data_list =  response_json['shoppingResult']['products']

            for data in data_list[:]:
                price_list.append(float(data['price']))
    
    return price_list[:top]
    
    

if __name__ == "__main__" :
    keyword="μ νμμΉ"
    top_10 = avg_products_price(keyword,10,1)
    top_10_avg_price = sum(top_10)/len(top_10)
    print(top_10)
    print("sum(top_10) :", sum(top_10), "len(top_10 : ", len(top_10) , "avg_price : ", top_10_avg_price )

    top_40 = avg_products_price(keyword,40,1)
    top_40_avg_price = sum(top_40)/len(top_40)
    print(top_40)
    print("sum(top_40) :", sum(top_40), "len(top_40 : ", len(top_40) , "avg_price : ", top_40_avg_price )

    top_120 = avg_products_price(keyword,120,3)
    top_120_avg_price = sum(top_120)/len(top_120)
    print(top_120)
    print("sum(top_120) :", sum(top_120), "len(top_10 : ", len(top_120) , "avg_price : ", top_120_avg_price )