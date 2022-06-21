import requests
import json
import datetime

def total_blogCnt(keyword):
    cookies = {
        'NNB': 'DULXWITNGSGGE',
        'nx_ssl': '2',
        'ASID': 'dc957c49000001810000e7bc00000053',
        '066c80626d06ffa5b32035f35cabe88d': 'j%C2%C3%F4F%26Bn%C1%D7KUBX%99%11%FCV0S%CB%3D%00%0C%EA%A5%29.%3E3%0C9I%F4O%40%CC_%D4%5D%02%C0%DE%7F%8Cf%89j%F9%0D%DBl%11%2F%FC%FDHnL%8B%99%C3%8E2%91%92%AC%14%F0%A7M%0C%A6%82%1B%ED%9D%5B6%FFb%D7C%80%86%F9N%F1%15%A54%BD%0B%3B%18mX%5D%1F%06%B6%F5R%BE%A8%C0%E3%EB%3A2t%9B%B4%82%CB%9A%1C%27%06%D4%F4R%A2%09%03W%5B%E6%86w%81%25%83%A1.f',
        '1a5b69166387515780349607c54875af': '%C1%F9%27nc%D2%A4%82',
        'JSESSIONID': '57F9B693EE00297DDEEB619A9BFA557F.jvm1',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Accept': 'application/json, text/plain, */*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=sim&keyword=%EB%82%98%EC%9D%B4%ED%82%A4',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'NNB=DULXWITNGSGGE; nx_ssl=2; ASID=dc957c49000001810000e7bc00000053; 066c80626d06ffa5b32035f35cabe88d=j%C2%C3%F4F%26Bn%C1%D7KUBX%99%11%FCV0S%CB%3D%00%0C%EA%A5%29.%3E3%0C9I%F4O%40%CC_%D4%5D%02%C0%DE%7F%8Cf%89j%F9%0D%DBl%11%2F%FC%FDHnL%8B%99%C3%8E2%91%92%AC%14%F0%A7M%0C%A6%82%1B%ED%9D%5B6%FFb%D7C%80%86%F9N%F1%15%A54%BD%0B%3B%18mX%5D%1F%06%B6%F5R%BE%A8%C0%E3%EB%3A2t%9B%B4%82%CB%9A%1C%27%06%D4%F4R%A2%09%03W%5B%E6%86w%81%25%83%A1.f; 1a5b69166387515780349607c54875af=%C1%F9%27nc%D2%A4%82; JSESSIONID=57F9B693EE00297DDEEB619A9BFA557F.jvm1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    params = {
        'countPerPage': '7',
        'currentPage': '1',
        'endDate': '',
        'keyword': keyword,
        'orderBy': 'recentdate',
        'startDate': '',
        'type': 'post',
    }

    response = requests.get('https://section.blog.naver.com/ajax/SearchList.naver', params=params, cookies=cookies, headers=headers)
    try : 
        response_json = json.loads(response.text)
    except:
        response_json = json.loads(response.text.replace(")]}',",""))
    total_blogCnt = response_json['result']['totalCount']
    
    return  total_blogCnt



if __name__ == "__main__" :
    keyword = "나이키"
    total_blog_Cnt = total_blogCnt(keyword)
    print("total_blogCnt : ",total_blog_Cnt)
