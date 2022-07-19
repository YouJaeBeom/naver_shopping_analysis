import requests
import json
import authorization
import tor 

def search_volume(keyword):
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

    ## setting tor
    proxies = {
        'http': 'socks5://localhost:9050',
    }
    try:
        response = requests.get('https://manage.searchad.naver.com/keywordstool', params=params, headers=headers, proxies=proxies)
    except requests.ConnectionError as ex:
        tor.renew_tor_ip(9051)
        print("ex = ", ex)
        print()
    else:
        response_json = json.loads(response.text)
        monthlyPcQcCnt =  response_json['keywordList'][0]['monthlyPcQcCnt']
        monthlyMobileQcCnt =  response_json['keywordList'][0]['monthlyMobileQcCnt']

        return monthlyPcQcCnt, monthlyMobileQcCnt

if __name__ == "__main__":
    keyword = "마스크"
    monthlyPcQcCnt, monthlyMobileQcCnt = search_volume(keyword)
    print(monthlyPcQcCnt, monthlyMobileQcCnt)

