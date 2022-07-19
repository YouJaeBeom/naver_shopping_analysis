import requests
import json
import detail_information_analysis

def top10_avg_info(keyword):
    headers = {
        'Referer': 'https://msearch.shopping.naver.com/search/all?query={}'.format(keyword).encode('utf-8').decode('iso-8859-1'),
    }

    params = {
        'sort': 'rel',
        'pagingIndex': "1",
        'pagingSize': '10',
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
        data_list =  response_json['shoppingResult']['products'][:10]
        avg_results = []
        for data in data_list:
            rank = data['rank']
            
            reviewCount = data['reviewCount']
            keepCnt = data['keepCnt']
            score = data['scoreInfo']

            mallProductId = data['mallProductId']
            if mallProductId != "":
                store_keepCnt, qnaCnt = detail_information_analysis.getinfo(mallProductId)
            else :
                store_keepCnt, qnaCnt = None, None
            
            print("rank : ",rank, reviewCount, keepCnt, score, store_keepCnt, qnaCnt)
            result = [rank, reviewCount, keepCnt, score, store_keepCnt, qnaCnt]
            avg_results.append(result)
        return avg_results

if __name__ == "__main__":
    avg_results = top10_avg_info("애플워치")