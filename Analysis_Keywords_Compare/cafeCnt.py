import requests
import json
import datetime

def total_cafeCnt(keyword):
    now = datetime.datetime.now()
    end = now.strftime('%Y%m%d')

    headers = {
        'Referer': 'https://section.cafe.naver.com/ca-fe/home/search/articles?q='+keyword.encode('utf-8').decode('iso-8859-1')+'&od=1&em=1',
    }

    json_data = {
        'query': keyword,
        'page': 1,
        'sortBy': 1,
        'exceptMarketArticle': 1,
        'period': [
            '20031201',
            end,
        ],
    }

    response = requests.post('https://apis.naver.com/cafe-home-web/cafe-home/v1/search/articles',  headers=headers, json=json_data)

    try : 
        response_json = json.loads(response.text)
    except:
        response_json = json.loads(response.text.replace(")]}',",""))
    total_cafeCnt = response_json['message']['result']['totalCount']
    
    return  total_cafeCnt

def monthly_cafeCnt(keyword):
    now = datetime.datetime.now()
    end = now.strftime('%Y%m%d')

    start = now + datetime.timedelta(days=-31)
    start = start.strftime('%Y%m%d')
    print("start : ", start, "end : ", end)


    headers = {
        'Referer': 'https://section.cafe.naver.com/ca-fe/home/search/articles?q='+keyword.encode('utf-8').decode('iso-8859-1')+'&od=1&em=1',
    }

    json_data = {
        'query': keyword,
        'page': 1,
        'sortBy': 1,
        'exceptMarketArticle': 1,
        'period': [
            start,
            end,
        ],
    }

    response = requests.post('https://apis.naver.com/cafe-home-web/cafe-home/v1/search/articles', headers=headers, json=json_data)

    try : 
        response_json = json.loads(response.text)
    except:
        response_json = json.loads(response.text.replace(")]}',",""))
    monthly_blogCnt = response_json['message']['result']['totalCount']
    
    return  monthly_blogCnt

if __name__ == "__main__" :
    keyword = "나이키"
    total_cafe_Cnt = total_cafeCnt(keyword)
    monthly_cafe_Cnt = monthly_cafeCnt(keyword)
    print("total_cafe_Cnt : ",total_cafe_Cnt)
    print("monthly_cafe_Cnt : ",monthly_cafe_Cnt)