import requests
import json
import authorization
import tor

def search_volume(cid, start, end, device, gender, age, keyword):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:100.0) Gecko/20100101 Firefox/100.0',
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
        'keyword': keyword,
    }
    ## setting tor
    proxies = {
        'http': 'socks5://127.0.0.1:9050',
    }
    try:
        response = requests.post('https://datalab.naver.com/shoppingInsight/getKeywordClickTrend.naver', headers=headers, proxies=proxies, data=data)
    except requests.ConnectionError as ex:
        tor.renew_tor_ip(9051)
        print("ex = ", ex)
        print()
    else:
        response_json = json.loads(response.text)
        data =  response_json['result'][0]['data']

        return data

if __name__ == "__main__":
    ## 기간 설정
    import datetime
    end = datetime.datetime.now().strftime('%Y-%m-%d')
    start = datetime.datetime.now() + datetime.timedelta(days=-31)
    start = start.strftime('%Y-%m-%d')

    ## 카테고리 id 설정
    cid = "50000000"
    
    ## device 별
    device = "pc,mo"

    ## Gener 
    gender = "f,m" 

    ## 나이별 "10,20,30,40,50,60"
    age = "20,30,40"

    ## keyword
    keyword = "나이키"

    search_volume = search_volume(cid, start, end, device, gender, age, keyword)
    print("search_volume :", (search_volume))

