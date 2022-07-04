import requests
import json
def getagerate(cid, start, end, device, gender, age):
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:100.0) Gecko/20100101 Firefox/100.0',
        'Referer': 'https://datalab.naver.com/shoppingInsight/sCategory.naver',
    }

    data = {
        'cid': cid, ## category unique id 
        'timeUnit': 'date',
        'startDate': start,
        'endDate': end,
        'age': age,
        'gender': gender,
        'device': device,
    }

    response = requests.post('https://datalab.naver.com/shoppingInsight/getCategoryAgeRate.naver',  headers=headers, data=data)
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
    cid = "50000006"
    
    ## device 별
    device = "pc,mo"

    ## Gener 
    gender = "f,m" 

    ## 나이별
    age = "20,30,40"
    print(cid, start, end, device, gender, age)
    agerate = getagerate(cid, start, end, device, gender, age)
    print("getCategoryAgeRate :", (agerate))