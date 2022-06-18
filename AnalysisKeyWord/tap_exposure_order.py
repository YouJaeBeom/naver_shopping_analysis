import requests
from bs4 import BeautifulSoup as bs

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
    'query': '아디다스',
    'oquery': '아디다스',
    #'tqi': 'hq2VtdprvTossvqYV30ssssstYd-256131',
}

response = requests.get('https://search.naver.com/search.naver', params=params, cookies=cookies, headers=headers)

soup = bs(response.text, "html.parser")
with open("TextFile.txt", "w") as file:
    file.write(response.text)

## 다이랙트 홈페이지 div, brand_wrap

## 공식 스토어 div , api_subject_bx _nsiteTop

## 파워 링크 div , power_link_body

## 사전 section  , sc_new sp_ndic _au_dictionary _prs_ldc_btm 

## place div id place-app-root

## naver shopping section class sc_new sp_nshop _shopping_root

## related section class sc_new sp_intent_block

## 인플루언서 참여 콘텐ㅊ으 section class sc_new sp_intent_block

## 뉴스 section class sc_new sp_nnews _prs_nws_all

## 뷰 section class sc_new sp_nreview _prs_rvw _au_view_collection

## 카페 중고거래 section class sc_new sp_ncafe_used _prs_shc _au_preowned_collection

## 이미지 section class sc_new sp_nimage _prs_img_bas