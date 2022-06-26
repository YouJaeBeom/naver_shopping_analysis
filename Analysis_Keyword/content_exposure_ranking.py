import re
import requests
from bs4 import BeautifulSoup as bs
import json
import detail_cafeinfo
import detail_bloginfo
import detail_postinfo

def content_exposure_ranking(keyword):
    total_results = []
    start = 0
    while (True):
        cookies = {
            'NNB': 'DULXWITNGSGGE',
            'nx_ssl': '2',
            'ASID': 'dc957c49000001810000e7bc00000053',
            '_ga_7VKFYR6RV1': 'GS1.1.1655285848.1.1.1655287263.60',
            '_ga': 'GA1.2.678320805.1655285848',
            'page_uid': 'hqY+klprvh8ssOE5l5wssssstzG-056087',
            '_naver_usersession_': 'bBoQpWPsMCOKor31DPVA206h',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
            'Accept': '*/*',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%EB%82%98%EC%9D%B4%ED%82%A4',
            'Connection': 'keep-alive',
            # Requests sorts cookies= alphabetically
            # 'Cookie': 'NNB=DULXWITNGSGGE; nx_ssl=2; ASID=dc957c49000001810000e7bc00000053; _ga_7VKFYR6RV1=GS1.1.1655285848.1.1.1655287263.60; _ga=GA1.2.678320805.1655285848; page_uid=hqY+klprvh8ssOE5l5wssssstzG-056087; _naver_usersession_=bBoQpWPsMCOKor31DPVA206h',
            'Sec-Fetch-Dest': 'script',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-site',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }

        params = {
            'rev': '44',
            'where': 'view',
            'api_type': '11',
            'start': str(start),
            'query': keyword,
            'nso': '',
            'nqx_theme': '{"theme":{"main":{"name":"shopping_top"},"sub":[{"name":"shopping"}]}}',
            'main_q': '',
            'mode': 'normal',
            'q_material': '',
            'ac': '0',
            'aq': '0',
            'spq': '0',
            'st_coll': '',
            'topic_r_cat': '',
            'nx_search_query': '',
            'nx_and_query': '',
            'nx_sub_query': '',
            'prank': str(start),
            'sm': 'tab_jum',
            'ssc': 'tab.view.view',
            'ngn_country': 'KR',
            'lgl_rcode': '',
            'fgn_region': '',
            'fgn_city': '',
            'lgl_lat': '',
            'lgl_long': '',
            'abt': '',
            '_callback': 'viewMoreContents',
        }

        response = requests.get('https://s.search.naver.com/p/review/search.naver', params=params, cookies=cookies, headers=headers)
        url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%EB%82%98%EC%9D%B4%ED%82%A4"
        
        pure_json = response.text[response.text.index('(') + 1 : response.text.rindex(')')]
        response_json = json.loads(pure_json)
        response_json = response_json['html']
        soup = bs(response_json, "html.parser")

        results = soup.find_all("div", class_="total_area")
        #sub_txt sub_name 

        for idx, result in enumerate(results):
            title = result.find('a', class_='api_txt_lines')
            publish_title = result.find('a', class_='sub_txt sub_name')

            ## adc일 경우
            if publish_title is None:
                publish_title = result.find('span', class_='source_txt name')
            
            readCount = ""
            writeDate = ""

            if  "cafe" in str( (requests.get(title.get('href'))).url ):
                readCount, writeDate = detail_cafeinfo.getcafeinfo(title.get('href'))
            elif  "blog" in str( (requests.get(title.get('href'))).url ):
                readCount = None
                writeDate = result.find("span", class_="sub_time sub_txt").text
            elif  "post" in str( (requests.get(title.get('href'))).url ):
                readCount = None
                writeDate = detail_postinfo.getpostinfo(title.get('href'))
            
            print("start point : ",start ,"index : ",idx,  "readCount : ", readCount, "writeDate : ", writeDate , "result : ",  title.text, "publish_title : ", publish_title.text)

            title = title.text
            publish_title = publish_title.text
            readCount = readCount
            writeDate = writeDate
            total_result = [title, publish_title, readCount, writeDate]
            total_results.append(total_result)

        if len(results)==0:
            break
            
        
        start = start+len(results)+1


    return total_results
    
    

if __name__ == "__main__":
    keyword = "아디다스"
    results = content_exposure_ranking(keyword)
    print(results)
    #cafeid()
