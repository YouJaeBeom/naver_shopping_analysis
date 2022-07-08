from ast import Not
import requests
from bs4 import BeautifulSoup as bs

def tap_exposure_orderList(keyword):
    params = {
        'sm': 'tab_hty.top',
        'where': 'nexearch',
        'query': keyword,
        'oquery': keyword,
        #'tqi': 'hq2VtdprvTossvqYV30ssssstYd-256131',
    }

    response = requests.get('https://search.naver.com/search.naver', params=params)
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
    keyword_list = ['롤', "애플워치", "애플"]
    for keyword in keyword_list:
        tap_exposure_orderList(keyword)