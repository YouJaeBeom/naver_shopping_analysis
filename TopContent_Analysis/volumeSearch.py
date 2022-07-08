import requests
import json
import authorization


def search_volume(keyword):
    Authorization = authorization.authorization()
    headers = {
        'Authorization': str(Authorization),
    }

    params = {
        'format': 'json',
        'hintKeywords': keyword,
        'siteId': '',
        'month': '',
        'biztpId': '',
        'event': '',
        'includeHintKeywords': '0',
        'showDetail': '1',
        'keyword': '',
    }

    response = requests.get('https://manage.searchad.naver.com/keywordstool', params=params, headers=headers)

    response_json = json.loads(response.text)
    monthlyPcQcCnt =  response_json['keywordList'][0]['monthlyPcQcCnt']
    monthlyMobileQcCnt =  response_json['keywordList'][0]['monthlyMobileQcCnt']

    return monthlyPcQcCnt, monthlyMobileQcCnt

if __name__ == "__main__":
    keyword = "마스크"
    monthlyPcQcCnt, monthlyMobileQcCnt = search_volume(keyword)
    print(monthlyPcQcCnt, monthlyMobileQcCnt)

