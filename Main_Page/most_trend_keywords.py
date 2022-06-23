
import json
import requests

def most_trend_keywords(cid,period):
    params = {
        'categoryCategoryId': cid,
        'categoryChildCategoryId': '',
        'categoryDemo': 'M04',
        'categoryMidCategoryId': '',
        'categoryRootCategoryId': cid,
        'chartRank': '1',
        'period': period,
    }

    response = requests.get('https://search.shopping.naver.com/best/_next/data/NurwgmMcJVwLajFklX6sM/category/keyword.json', params=params)

    response_json = json.loads(response.text)
    charts =  response_json['pageProps']['dehydratedState']['queries'][2]['state']['data']['charts']

    return charts
    
if __name__ == "__main__":
    # cid -> ALL or 5000000 etc..
    cid = "ALL"

    # period -> P1D or P7D
    period = "P7D"
    print(most_trend_keywords(cid,period))