import re
import requests
from bs4 import BeautifulSoup as bs
import json

def top10_blog(keyword):
    cookies = {
        'NNB': 'DULXWITNGSGGE',
        'nx_ssl': '2',
        'ASID': 'dc957c49000001810000e7bc00000053',
        '_ga_7VKFYR6RV1': 'GS1.1.1655549940.3.0.1655549940.60',
        '_ga': 'GA1.2.678320805.1655285848',
        '066c80626d06ffa5b32035f35cabe88d': 'j%C2%C3%F4F%26Bn%C1%D7KUBX%99%11%0C5%00%C4B6l-%A3%7C%D2%FE%AC%D8%83%98%B4f%0D.%96n%25WA%A4Y%ED%05%3F%0A%8Ai%40%98%3F%19%2C%EE%FCHnL%8B%99%C3%8E2%91%92%AC%14%F0%A7M%0C%A6%82%1B%ED%9D%5B6%FF%21%8CN%2C%5C%1A%C0%C2%89%EC+%CA_%064%A5%3F%83J%5B%5CQ%C4%92%A8%C0%E3%EB%3A2t%9B%B4%82%CB%9A%1C%27%06%D4%C4%8E%F2%22%EE%DC%A4%1CL%02%F7%40%B5%BA%8D%AA',
        '1a5b69166387515780349607c54875af': '%C1%F9%27nc%D2%A4%82',
        'page_uid': 'hrbOUlprvhGssNaSlbVssssssr0-494720',
        '_naver_usersession_': 'mM/1K7p4mW7d5tvDxmEdmw==',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'NNB=DULXWITNGSGGE; nx_ssl=2; ASID=dc957c49000001810000e7bc00000053; _ga_7VKFYR6RV1=GS1.1.1655549940.3.0.1655549940.60; _ga=GA1.2.678320805.1655285848; 066c80626d06ffa5b32035f35cabe88d=j%C2%C3%F4F%26Bn%C1%D7KUBX%99%11%0C5%00%C4B6l-%A3%7C%D2%FE%AC%D8%83%98%B4f%0D.%96n%25WA%A4Y%ED%05%3F%0A%8Ai%40%98%3F%19%2C%EE%FCHnL%8B%99%C3%8E2%91%92%AC%14%F0%A7M%0C%A6%82%1B%ED%9D%5B6%FF%21%8CN%2C%5C%1A%C0%C2%89%EC+%CA_%064%A5%3F%83J%5B%5CQ%C4%92%A8%C0%E3%EB%3A2t%9B%B4%82%CB%9A%1C%27%06%D4%C4%8E%F2%22%EE%DC%A4%1CL%02%F7%40%B5%BA%8D%AA; 1a5b69166387515780349607c54875af=%C1%F9%27nc%D2%A4%82; page_uid=hrbOUlprvhGssNaSlbVssssssr0-494720; _naver_usersession_=mM/1K7p4mW7d5tvDxmEdmw==',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
    }

    params = {
        'query': keyword,
        'nso': '',
        'where': 'blog',
        'sm': 'tab_opt',
    }

    response = requests.get('https://search.naver.com/search.naver', params=params, cookies=cookies, headers=headers)
    soup = bs(response.text, "html.parser")

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

if __name__ == "__main__":
    keyword = "마스크"
    top10_blog(keyword)