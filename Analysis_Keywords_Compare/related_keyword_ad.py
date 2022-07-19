import requests
import json
import authorization
import tor 
def ads_related_keywords(keyword):
    Authorization = authorization.authorization()

    headers = {
        'Authorization': Authorization,
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
        response = requests.get('https://manage.searchad.naver.com/keywordstool', params=params,  headers=headers, proxies=proxies)
    except requests.ConnectionError as ex:
        tor.renew_tor_ip(9051)
        print("ex = ", ex)
        print()
    else:
        response_json = json.loads(response.text)
        ads_related_keywords_list =  response_json['keywordList']

        return ads_related_keywords_list
    

if __name__ == "__main__" :
    keyword = "마스크"
    ads_related_keywords_list = ads_related_keywords(keyword)

    print(ads_related_keywords_list)
