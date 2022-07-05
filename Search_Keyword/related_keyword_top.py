import requests
import json
import time 

def top_related_keywords(cid,start,end):

    top_related_keywords_list = []

    for pageInd in range(1,26):
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
            'page': str(pageInd),
            'count': '20',
        }

        response = requests.post('https://datalab.naver.com/shoppingInsight/getCategoryKeywordRank.naver', headers=headers, data=data)
        response_json = json.loads(response.text)
        ranks = response_json['ranks']
        
        for rank in ranks: 
            top_related_keywords_list.append(rank)
    
    return top_related_keywords_list

if __name__ == "__main__" :
    cid = "50000006"
    
    ## 기간 설정
    import datetime
    end = datetime.datetime.now().strftime('%Y-%m-%d')
    start = datetime.datetime.now() + datetime.timedelta(days=-31)
    start = start.strftime('%Y-%m-%d')
    
    top_related_keywords_list = top_related_keywords(cid,start,end)
    print(top_related_keywords_list)
