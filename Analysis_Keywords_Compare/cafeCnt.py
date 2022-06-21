import requests
import json
import datetime

def total_cafeCnt(keyword):
    now = datetime.datetime.now()
    end = now.strftime('%Y%m%d')
    cookies = {
        'NNB': 'DULXWITNGSGGE',
        'nx_ssl': '2',
        'ASID': 'dc957c49000001810000e7bc00000053',
        '066c80626d06ffa5b32035f35cabe88d': 'j%C2%C3%F4F%26Bn%C1%D7KUBX%99%11%FCV0S%CB%3D%00%0C%EA%A5%29.%3E3%0C9I%F4O%40%CC_%D4%5D%02%C0%DE%7F%8Cf%89j%F9%0D%DBl%11%2F%FC%FDHnL%8B%99%C3%8E2%91%92%AC%14%F0%A7M%0C%A6%82%1B%ED%9D%5B6%FFb%D7C%80%86%F9N%F1%15%A54%BD%0B%3B%18mX%5D%1F%06%B6%F5R%BE%A8%C0%E3%EB%3A2t%9B%B4%82%CB%9A%1C%27%06%D4%F4R%A2%09%03W%5B%E6%86w%81%25%83%A1.f',
        '1a5b69166387515780349607c54875af': '%C1%F9%27nc%D2%A4%82',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Accept': 'application/json, text/plain, */*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://section.cafe.naver.com/ca-fe/home/search/articles?q=%EB%82%98%EC%9D%B4%ED%82%A4&od=1&em=1',
        'X-Cafe-Product': 'pc',
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://section.cafe.naver.com',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'NNB=DULXWITNGSGGE; nx_ssl=2; ASID=dc957c49000001810000e7bc00000053; 066c80626d06ffa5b32035f35cabe88d=j%C2%C3%F4F%26Bn%C1%D7KUBX%99%11%FCV0S%CB%3D%00%0C%EA%A5%29.%3E3%0C9I%F4O%40%CC_%D4%5D%02%C0%DE%7F%8Cf%89j%F9%0D%DBl%11%2F%FC%FDHnL%8B%99%C3%8E2%91%92%AC%14%F0%A7M%0C%A6%82%1B%ED%9D%5B6%FFb%D7C%80%86%F9N%F1%15%A54%BD%0B%3B%18mX%5D%1F%06%B6%F5R%BE%A8%C0%E3%EB%3A2t%9B%B4%82%CB%9A%1C%27%06%D4%F4R%A2%09%03W%5B%E6%86w%81%25%83%A1.f; 1a5b69166387515780349607c54875af=%C1%F9%27nc%D2%A4%82',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
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

    response = requests.post('https://apis.naver.com/cafe-home-web/cafe-home/v1/search/articles', cookies=cookies, headers=headers, json=json_data)

    try : 
        response_json = json.loads(response.text)
    except:
        response_json = json.loads(response.text.replace(")]}',",""))
    total_cafeCnt = response_json['message']['result']['totalCount']
    
    return  total_cafeCnt

if __name__ == "__main__" :
    keyword = "나이키"
    total_cafe_Cnt = total_cafeCnt(keyword)
    print("total_cafe_Cnt : ",total_cafe_Cnt)