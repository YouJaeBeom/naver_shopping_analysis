import requests
import json
import datetime

def total_blogCnt(keyword):
    headers = {
        'Referer': 'https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=sim&keyword='+keyword.encode('utf-8').decode('iso-8859-1'),
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

    response = requests.get('https://section.blog.naver.com/ajax/SearchList.naver', params=params, headers=headers)
    try : 
        response_json = json.loads(response.text)
    except:
        response_json = json.loads(response.text.replace(")]}',",""))
    total_blogCnt = response_json['result']['totalCount']
    
    return  total_blogCnt

def monthly_blogCnt(keyword):
    now = datetime.datetime.now()
    end = now.strftime('%Y-%m-%d')

    start = now + datetime.timedelta(days=-31)
    start = start.strftime('%Y-%m-%d')
    print("start : ", start, "end : ", end)

    headers = {
        'Referer': 'https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=sim&keyword='+keyword.encode('utf-8').decode('iso-8859-1'),
    }

    params = {
        'countPerPage': '7',
        'currentPage': '1',
        'endDate': end,
        'keyword': keyword,
        'orderBy': 'recentdate',
        'startDate': start,
        'type': 'post',
    }

    response = requests.get('https://section.blog.naver.com/ajax/SearchList.naver', params=params, headers=headers)
    try : 
        response_json = json.loads(response.text)
    except:
        response_json = json.loads(response.text.replace(")]}',",""))
    monthly_blogCnt = response_json['result']['totalCount']
    
    return  monthly_blogCnt

if __name__ == "__main__" :
    keyword = "나이키"
    total_blog_Cnt = total_blogCnt(keyword)
    monthly_blog_Cnt = monthly_blogCnt(keyword)
    print("total_blogCnt : ",total_blog_Cnt)
    print("monthly_blogCnt : ",monthly_blog_Cnt)