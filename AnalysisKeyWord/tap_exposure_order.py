from ast import Not
import requests
from bs4 import BeautifulSoup as bs

def tap_exposure_orderList(keyword):
    cookies = {
        'NNB': 'DULXWITNGSGGE',
        'nx_ssl': '2',
        'ASID': 'dc957c49000001810000e7bc00000053',
        '_ga_7VKFYR6RV1': 'GS1.1.1655538255.2.0.1655538255.60',
        '_ga': 'GA1.2.678320805.1655285848',
        'page_uid': 'hq2VtwprvTossvOPTW8sssssslG-366751',
        '_gid': 'GA1.2.464269409.1655538256',
        'BMR': 's=1655548603024&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.naver%3FisHttpsRedirect%3Dtrue%26blogId%3Dsw4r%26logNo%3D221117312622&r2=https%3A%2F%2Fwww.google.com%2F',
        '_naver_usersession_': 'TV0S1XqiY65L6EkdGayc6Q==',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Referer': 'https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query=%EC%95%84%EB%94%94%EB%8B%A4%EC%8A%A4',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'NNB=DULXWITNGSGGE; nx_ssl=2; ASID=dc957c49000001810000e7bc00000053; _ga_7VKFYR6RV1=GS1.1.1655538255.2.0.1655538255.60; _ga=GA1.2.678320805.1655285848; page_uid=hq2VtwprvTossvOPTW8sssssslG-366751; _gid=GA1.2.464269409.1655538256; BMR=s=1655548603024&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.naver%3FisHttpsRedirect%3Dtrue%26blogId%3Dsw4r%26logNo%3D221117312622&r2=https%3A%2F%2Fwww.google.com%2F; _naver_usersession_=TV0S1XqiY65L6EkdGayc6Q==',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        'sm': 'tab_hty.top',
        'where': 'nexearch',
        'query': keyword,
        'oquery': keyword,
        #'tqi': 'hq2VtdprvTossvqYV30ssssstYd-256131',
    }

    response = requests.get('https://search.naver.com/search.naver', params=params, cookies=cookies, headers=headers)
    soup = bs(response.text, "html.parser")


    tap_list = [
        'sc_new sp_nshop _shopping_root',
        'ad_section section _pl_section bg_type_v2',
        'brand_search section brand_new_ui',
        'sc_new sp_nsite _project_site_channel_root _section_nsite_ _sp_ntotal _prs_vsd_bas',
        'sc_new sp_nnews _prs_nws_all',
        'sc_new sp_intent_block',
        'place-app-root',
        'sc_new sp_nimage _prs_img_bas',
        'sc_new sp_nreview _prs_rvw _au_view_collection',
        'sc_new cs_stock cs_stock_same _cs_stock',
        'sc_new sp_ndic _au_dictionary _prs_ldc_btm',
        'sc_new sp_ntotal _prs_web_gen _web_gen _sp_ntotal _kin_snippet_root_web_gen _project_channel_root_web_gen _fe_kin_snippet',
        'sc_new sp_nvideo _fe_video_collection _prs_vdo_lst',
        'sc_new sp_influencer _prs_ink_mik',
        'sc_new sp_nkin _au_kin_collection'
        ]
    tap_list_str = [
        '네이버 쇼팡',
        '파워 링크',
        '홈페이지',
        '공식 스토어',
        '뉴스',
        '관련 컨텐츠',
        '플레이스',
        '이미지',
        '뷰',
        '증권정보',
        '사전',
        '외부링크',
        '동영상',
        'influencer',
        '지식인'
        ]
    results = soup.find_all(["div","section"],class_=tap_list)

    order_list = []
    for idx, result in enumerate(results):
        for indx, tap in enumerate(tap_list):
            if str(tap) in str(result):
                order_list.append(tap_list_str[indx])
                print(tap_list_str[indx])

if __name__== "__main__":
    tap_exposure_orderList("롤")