import requests
import json

def trend_keywords_detail(keyword,cid,period,rankedDate):
    
    json_data = {
        'query': '\n      query ChartProductList($params: ChartProductListInput, $exposeLogSourceInfo: ExposeLogSourceInfo) {\n        KeywordChartProductList(params: $params, exposeLogSourceInfo: $exposeLogSourceInfo) {\n            nvMid\n            imageUrl\n            mobileLowPrice\n            priceUnit\n            productTitle\n            purchaseCnt\n            mallCount\n            mpTp\n            reviewCount\n            mallProductUrl\n            mallProdMblUrl\n            dlvryCd\n            productCrUrl\n        }\n      }\n    ',
        'variables': {
            'params': {
                'chartTitle': keyword,
                'categoryId': cid,
                'rankedDate': rankedDate,
                'demo': 'A00',
                'period': period,
                'productType': cid,
                'rankStart': 1,
                'rankEnd': 20,
            },
            'exposeLogSourceInfo': {
                'isMobileDomain': False,
                'pageType': 'Category',
            },
        },
    }
    response = requests.post('https://search.shopping.naver.com/best/api/graphql', json=json_data)

    response_json = json.loads(response.text)
    charts =  response_json['data']['KeywordChartProductList']
    return charts