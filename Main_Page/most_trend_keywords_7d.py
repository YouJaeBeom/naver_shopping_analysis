
import json
import requests

def most_trend_keywords_7d():
    params = {
        'categoryCategoryId': 'ALL',
        'categoryChildCategoryId': '',
        'categoryDemo': 'M04',
        'categoryMidCategoryId': '',
        'categoryRootCategoryId': 'ALL',
        'chartRank': '1',
        'period': 'P7D',
    }

    response = requests.get('https://search.shopping.naver.com/best/_next/data/NurwgmMcJVwLajFklX6sM/category/keyword.json', params=params)

    response_json = json.loads(response.text)
    charts =  response_json['pageProps']['dehydratedState']['queries'][2]['state']['data']['charts']

    return charts

if __name__ == "__main__":
    print(most_trend_keywords_7d())