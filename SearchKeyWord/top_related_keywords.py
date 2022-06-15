import requests
import json
def top_related_keywords(cid,startDate,endDate,page):
    cookies = {
        'NNB': 'DULXWITNGSGGE',
        'nx_ssl': '2',
        'ASID': 'dc957c49000001810000e7bc00000053',
        '_datalab_cid': '50000006',
        '066c80626d06ffa5b32035f35cabe88d': 'j%C2%C3%F4F%26Bn%C1%D7KUBX%99%11%15wB%DB%D1%29K%E0%99%97g%8B%EBz%9C%FEu%40%F9%D4%9D%25b%E6%CA%19%05%BCD%C5%C0%FD%92Z%8B%BF%24%B5%60%13HnL%8B%99%C3%8E2%91%92%AC%14%F0%A7M%0C%A6%82%1B%ED%9D%5B6%FFb%D7C%80%86%F9N%F14f%22%89i%F4%09%00%96%3D%18F%FD%C2%EC%92%A8%C0%E3%EB%3A2t%9B%B4%82%CB%9A%1C%27%06%D4%BBa%8A%16i%90%2B%D2%A0%F4%D0%7E%C5%B7%2A%BE',
        '1a5b69166387515780349607c54875af': '%C1%F9%27nc%D2%A4%82',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Accept': '*/*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://datalab.naver.com/shoppingInsight/sCategory.naver',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://datalab.naver.com',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'NNB=DULXWITNGSGGE; nx_ssl=2; ASID=dc957c49000001810000e7bc00000053; _datalab_cid=50000006; 066c80626d06ffa5b32035f35cabe88d=j%C2%C3%F4F%26Bn%C1%D7KUBX%99%11%15wB%DB%D1%29K%E0%99%97g%8B%EBz%9C%FEu%40%F9%D4%9D%25b%E6%CA%19%05%BCD%C5%C0%FD%92Z%8B%BF%24%B5%60%13HnL%8B%99%C3%8E2%91%92%AC%14%F0%A7M%0C%A6%82%1B%ED%9D%5B6%FFb%D7C%80%86%F9N%F14f%22%89i%F4%09%00%96%3D%18F%FD%C2%EC%92%A8%C0%E3%EB%3A2t%9B%B4%82%CB%9A%1C%27%06%D4%BBa%8A%16i%90%2B%D2%A0%F4%D0%7E%C5%B7%2A%BE; 1a5b69166387515780349607c54875af=%C1%F9%27nc%D2%A4%82',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = {
        'cid': '50000006',
        'timeUnit': 'date',
        'startDate': '2022-05-14',
        'endDate': '2022-06-14',
        'age': '',
        'gender': '',
        'device': '',
        'page': '1',
        'count': '40',
    }

    response = requests.post('https://datalab.naver.com/shoppingInsight/getCategoryKeywordRank.naver', cookies=cookies, headers=headers, data=data)
    response_json = json.loads(response.text)
    top_related_keywords_list =  response_json['ranks']
    print(top_related_keywords_list)

if __name__ == "__main__" :
    cid,startDate,endDate,page = None
    
    top_related_keywords(cid,startDate,endDate,page)
