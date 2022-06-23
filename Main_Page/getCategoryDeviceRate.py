import requests
import json
def getdevicerate(cid, start, end):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:100.0) Gecko/20100101 Firefox/100.0',
        'Referer': 'https://datalab.naver.com/shoppingInsight/sCategory.naver',
    }

    data = {
        'cid': cid, ## category unique id 
        'timeUnit': 'date',
        'startDate': start,
        'endDate': end,
        'age': '',
        'gender': '',
        'device': '',
    }

    response = requests.post('https://datalab.naver.com/shoppingInsight/getCategoryDeviceRate.naver', headers=headers, data=data)

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
    ## 나이별

    agerate = getdevicerate(cid, start, end)
    print("getdevicerate :", (agerate))