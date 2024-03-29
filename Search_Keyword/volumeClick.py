import requests
import json
import authorization

def click_volume(keyword):

    Authorization = authorization.authorization()

    headers = {
        'Authorization': (Authorization),
        'Referer': 'https://manage.searchad.naver.com/customers/2565665/tool/keyword-planner',
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
    monthlyAvePcClkCnt =  response_json['keywordList'][0]['monthlyAvePcClkCnt']
    monthlyAveMobileClkCnt =  response_json['keywordList'][0]['monthlyAveMobileClkCnt']

    return monthlyAvePcClkCnt, monthlyAveMobileClkCnt

if __name__ == "__main__" :
    monthlyAvePcClkCnt, monthlyAveMobileClkCnt = click_volume("마스크")
    print(monthlyAvePcClkCnt, monthlyAveMobileClkCnt)