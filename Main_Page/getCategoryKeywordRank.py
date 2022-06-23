import json
import requests
import datetime
import time
def getkeywordrand(cid, start, end):
    ranks_list = []
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
            'age': '',
            'gender': '',
            'device': '',
            'page': str(page),
            'count': '50',
        }

        response = requests.post('https://datalab.naver.com/shoppingInsight/getCategoryKeywordRank.naver', headers=headers, data=data)
        print(response.text)
        response_json = json.loads(response.text)
        ranks =  response_json['ranks']
        for rank in ranks:
            ranks_list.append(rank)

    return ranks_list

if __name__ == "__main__":
    ## 기간 설정
    end = datetime.datetime.now().strftime('%Y-%m-%d')
    start = datetime.datetime.now() + datetime.timedelta(days=-31)
    start = start.strftime('%Y-%m-%d')

    ## 카테고리 id 설정
    cid = "50000006"
    ranks_list = getkeywordrand(cid, start, end)
    print("ranks_list : ", ranks_list)