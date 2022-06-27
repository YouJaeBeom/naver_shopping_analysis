
import json
import requests
import most_trend_keywords_detail
import datetime
def most_trend_keywords(cid,period):
    json_data = {
        'query': '\n      query ChartList($params: ChartListInput) {\n        KeywordChartList(params: $params) {\n          rankedDate\n          period\n          demo\n          categoryId\n          charts {\n            rank\n            change\n            brandSeq\n            brandName\n            exposeBrandName\n            keyword\n            exposeKeyword\n            rankedReason\n          }\n        }\n      }\n    ',
        'variables': {
            'params': {
                'categoryId': cid,
                'demo': 'A00',
                'period': period,
                'rankStart': 1,
                'rankEnd': 20,
            },
        },
    }

    response = requests.post('https://search.shopping.naver.com/best/api/graphql', json=json_data)
    response_json = json.loads(response.text)
    charts =  response_json['data']['KeywordChartList']['charts']

    for chart in charts:
        rankedDate = datetime.datetime.now().strftime('%Y%m%d')
        keyword = chart['keyword']
        products = most_trend_keywords_detail.trend_keywords_detail(keyword,cid,period,rankedDate)
        print(keyword, products)

    return charts
    
if __name__ == "__main__":
    # cid -> ALL or 5000000 etc..
    cid = "ALL"

    # period -> P1D or P7D
    period = "P7D"
    print(most_trend_keywords(cid,period))