from pip import main
import requests
import json

def avg_products_purchaseCnt(keyword, top,repeat):
    purchaseCnt_list = []
    ## setting tor
    proxies = {
        'http': 'socks5://localhost:9050',
    }

    for pagenumber in range(1,repeat+1):
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
        
        try:
            response = requests.get('https://msearch.shopping.naver.com/api/search/all', params=params,  headers=headers)
        except requests.ConnectionError as ex:
            tor.renew_tor_ip(9051)
            print("ex = ", ex)
            print()
        else:
            response_json = json.loads(response.text)
            data_list =  response_json['shoppingResult']['products']

            print(len(data_list))

            for data in data_list:
                purchaseCnt = data['purchaseCnt']
                purchaseCnt_list.append(float(purchaseCnt))
    
    return purchaseCnt_list[:top]
    
    

if __name__ == "__main__" :
    keyword="애플워치"
    top_10 = avg_products_purchaseCnt(keyword,10,1)
    top_10_avg_purchaseCnt = sum(top_10)/len(top_10)
    print(top_10)
    print("sum(top_10) :", sum(top_10), "len(top_10 : ", len(top_10) , "top_10_avg_purchaseCnt : ", top_10_avg_purchaseCnt )

    top_40 = avg_products_purchaseCnt(keyword,40,1)
    top_40_avg_purchaseCnt = sum(top_40)/len(top_40)
    print(top_40)
    print("sum(top_40) :", sum(top_10), "len(top_40 : ", len(top_40) , "top_40_avg_purchaseCnt : ", top_40_avg_purchaseCnt )