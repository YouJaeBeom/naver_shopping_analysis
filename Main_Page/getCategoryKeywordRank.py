import json
import requests
import datetime
import time
def getkeywordrand(cid, start, end, device, gender, age):
    keywordrank = []
    for page in range(1,26):
        time.sleep(0.1)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
            'Referer': 'https://datalab.naver.com/shoppingInsight/sCategory.naver',
        }

        data = {
            'cid': cid,
            'timeUnit': 'date',
            'startDate': start,
            'endDate': end,
            'age': age,
            'gender': gender,
            'device': device,
            'page': str(page),
            'count': '50',
        }
        ## setting tor
        proxies = {
            'http': 'socks5://localhost:9050',
        }
        try:
            response = requests.post('https://datalab.naver.com/shoppingInsight/getCategoryKeywordRank.naver', headers=headers, data=data, proxies=proxies)
        except requests.ConnectionError as ex:
            tor.renew_tor_ip(9051)
            print("ex = ", ex)
            print()
        else:
            response_json = json.loads(response.text)
            ranks =  response_json['ranks']
            for rank in ranks:
                keywordrank.append(rank)

    return keywordrank

if __name__ == "__main__":
    ## 기간 설정
    end = datetime.datetime.now().strftime('%Y-%m-%d')
    start = datetime.datetime.now() + datetime.timedelta(days=-31)
    start = start.strftime('%Y-%m-%d')

    ## 카테고리 id 설정
    cid = "50000006"
    
    ## device 별
    device = "pc,mo"

    ## Gener 
    gender = "f,m" 

    ## 나이별 "10,20,30,40,50,60"
    age = "20,30,40"

    keywordrank = getkeywordrand(cid, start, end, device, gender, age)
    print("keywordrank : ", keywordrank)