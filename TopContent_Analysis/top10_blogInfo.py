import re
import requests
from bs4 import BeautifulSoup as bs
import json

def top10_blog(keyword):
    params = {
        'query': keyword,
        'nso': '',
        'where': 'blog',
        'sm': 'tab_opt',
    }
    ## setting tor
    proxies = {
        'http': 'socks5://localhost:9050',
    }
    try:
        response = requests.get('https://search.naver.com/search.naver', params=params, proxies=proxies)
        soup = bs(response.text, "html.parser")
    except requests.ConnectionError as ex:
        tor.renew_tor_ip(9051)
        print("ex = ", ex)
        print()
    else:
        blog_list = soup.find_all("a", class_="sub_thumb")
        cnt_list = []
        for blog_info in blog_list[:10]:
            blogId =  str(blog_info.get("href")).split("/")[3]
            ## blog 방문자 수 조회 url
            base_url = "http://blog.naver.com/NVisitorgp4Ajax.nhn?blogId="+blogId
            response = requests.get(base_url)
            soup = bs(response.text, "html.parser")
            cnts = soup.find_all("visitorcnt")
            for cnt in cnts:
                cnt_list.append(float(cnt['cnt']))
                print("blogID : ", blogId, "\n response : ",cnt['cnt'], cnt['id'])
        
        print("cnt_list : ", cnt_list)
        print("avg cnt_list : ", sum(cnt_list)/len(cnt_list))
    return sum(cnt_list)/len(cnt_list)

if __name__ == "__main__":
    keyword = "마스크"
    top10_blog_avgCnt = top10_blog(keyword)
    print("top10_blog_avgCnt :", top10_blog_avgCnt)