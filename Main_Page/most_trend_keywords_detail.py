import requests
import json

def trend_keywords_detail(keyword,cid,period,demo,rankedDate):
    
    json_data = {
        'query': '\n      query ChartProductList($params: ChartProductListInput, $exposeLogSourceInfo: ExposeLogSourceInfo) {\n        KeywordChartProductList(params: $params, exposeLogSourceInfo: $exposeLogSourceInfo) {\n            nvMid\n            imageUrl\n            mobileLowPrice\n            priceUnit\n            productTitle\n            purchaseCnt\n            mallCount\n            mpTp\n            reviewCount\n            mallProductUrl\n            mallProdMblUrl\n            dlvryCd\n            productCrUrl\n        }\n      }\n    ',
        'variables': {
            'params': {
                'chartTitle': keyword,
                'categoryId': cid,
                'rankedDate': rankedDate,
                'demo': demo,
                'period': period,
                'productType': "ALL",
                'rankStart': 1,
                'rankEnd': 20,
            },
            'exposeLogSourceInfo': {
                'isMobileDomain': False,
                'pageType': 'Category',
            },
        },
    }

    ## setting tor
    proxies = {
        'http': 'socks5://127.0.0.1:9050',
    }

    try:
        response = requests.post(
        'https://msearch.shopping.naver.com/best/api/graphql', 
        json=json_data,
        proxies = proxies
        )
    except requests.ConnectionError as ex:
        tor.renew_tor_ip(9051)
        print("ex = ", ex)
        print()
    else:
        response_json = json.loads(response.text)
        charts =  response_json['data']['KeywordChartProductList']
    
    return charts
