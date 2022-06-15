import requests
from bs4 import BeautifulSoup as bs


def content_exposure_ranking(keyword):
    cookies = {
        'NNB': 'DULXWITNGSGGE',
        'nx_ssl': '2',
        'ASID': 'dc957c49000001810000e7bc00000053',
        '066c80626d06ffa5b32035f35cabe88d': 'j%C2%C3%F4F%26Bn%C1%D7KUBX%99%11%FCV0S%CB%3D%00%0C%EA%A5%29.%3E3%0C9I%F4O%40%CC_%D4%5D%02%C0%DE%7F%8Cf%89j%F9%0D%DBl%11%2F%FC%FDHnL%8B%99%C3%8E2%91%92%AC%14%F0%A7M%0C%A6%82%1B%ED%9D%5B6%FFb%D7C%80%86%F9N%F1%15%A54%BD%0B%3B%18mX%5D%1F%06%B6%F5R%BE%A8%C0%E3%EB%3A2t%9B%B4%82%CB%9A%1C%27%06%D4%F4R%A2%09%03W%5B%E6%86w%81%25%83%A1.f',
        '1a5b69166387515780349607c54875af': '%C1%F9%27nc%D2%A4%82',
        'page_uid': 'hqEoZdp0J1sssUUDgWKssssstph-029950',
        '_naver_usersession_': '9t5csILXF0KD5XZssqMRnw==',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Accept': '*/*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%EB%82%98%EC%9D%B4%ED%82%A4',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'NNB=DULXWITNGSGGE; nx_ssl=2; ASID=dc957c49000001810000e7bc00000053; 066c80626d06ffa5b32035f35cabe88d=j%C2%C3%F4F%26Bn%C1%D7KUBX%99%11%FCV0S%CB%3D%00%0C%EA%A5%29.%3E3%0C9I%F4O%40%CC_%D4%5D%02%C0%DE%7F%8Cf%89j%F9%0D%DBl%11%2F%FC%FDHnL%8B%99%C3%8E2%91%92%AC%14%F0%A7M%0C%A6%82%1B%ED%9D%5B6%FFb%D7C%80%86%F9N%F1%15%A54%BD%0B%3B%18mX%5D%1F%06%B6%F5R%BE%A8%C0%E3%EB%3A2t%9B%B4%82%CB%9A%1C%27%06%D4%F4R%A2%09%03W%5B%E6%86w%81%25%83%A1.f; 1a5b69166387515780349607c54875af=%C1%F9%27nc%D2%A4%82; page_uid=hqEoZdp0J1sssUUDgWKssssstph-029950; _naver_usersession_=9t5csILXF0KD5XZssqMRnw==',
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
        'start': '0',
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
        'prank': '0',
        'sm': 'tab_jum',
        'ssc': 'tab.view.view',
        'ngn_country': 'KR',
        'lgl_rcode': '',
        'fgn_region': '',
        'fgn_city': '',
        'lgl_lat': '',
        'lgl_long': '',
        'abt': '[{"eid":"PWC-AD-UP","value":{"bucket":"1","for":"impression-neo","is_control":true}}]',
        '_callback': 'viewMoreContents',
    }

    response = requests.get('https://s.search.naver.com/p/review/search.naver', params=params, cookies=cookies, headers=headers)

    soup = bs(response.text, "html.parser")

    # li._svp_item:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(2)
    # li._svp_item:nth-child(3) > div:nth-child(1) > div:nth-child(1) > a:nth-child(2)
    # li._svp_item:nth-child(1) > div:nth-child(1) > div:nth-child(1)
    #related_keywords = soup.select('li._svp_item:nth-child(1) > div:nth-child(1) > div:nth-child(1)')[0]

    print(response.text)


if __name__ == "__main__":
    keyword = "나이키"
    content_exposure_ranking(keyword)