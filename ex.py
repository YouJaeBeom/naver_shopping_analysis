import requests

cookies = {
    'NNB': 'DULXWITNGSGGE',
    'nx_ssl': '2',
    'ASID': 'dc957c49000001810000e7bc00000053',
    'nid_inf': '1631157862',
    'NID_AUT': 'mNO+8XvZHGi+wDfIukaykGursjHL4QHNPkYFKsLDhOgh7+QGMmKkFlp7pQmQzsVL',
    'NID_SES': 'AAABfA5Na0tDrKMMGrG6BMfr7mqWz56faQm+q9a5O+WZ4ZpAMgWOcIxV+z++EMyQk0qB+Nu9TTJYUGCZsuzi4qL/57aDQYcC4F9vjc1WTJLO2fLSXSYHbFRbbtDDL5t4p47HXLk9Twzdzmi8hK/NYiAXJcLpj4mk8I3bPuKjh86DVFD66qrEnG5IfGJDYCloU1Ry8g0elLXH3YT7v6EZhh1PJJD/YxNbzrneCEMtg+kWYhhrkAsmSAMMDQi5FazPZJ2FYdwLWKRDTrGnhFzJ7iCD8vMiQ+dj1eEe9jxPrKZO/0kdmpU2nLb4S9rj1dDLWhxskjkLGEFsiM47RIyY8CrUYbQikKZqZHC1xFaVbz/JggidJWMIk4q2NBDVqHXP9lDpFRqkaptARpG1BiCIfROm52aFyK/UrpvqJ7CHfxvXQXSqp0ZDV1t/Mdo5xoDptPzO8at7GNiZ8l7bQWhQOhypNNL4vuQgB29BMD9rk79Pbmx3l6x2ZvUwUZq92rdp3uEqlQ==',
    'NID_JKL': 'LJInBtlDv57Cw5ymKhME3AL6TFoX0rDIhlHPSnitVvQ=',
    '_naver_usersession_': '08M+asn3uAx3SMqojoVr1f3u',
    'page_uid': 'hqjRylprvxZssnErd/wssssstRl-494571',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%EC%BB%A4%ED%94%BC',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'NNB=DULXWITNGSGGE; nx_ssl=2; ASID=dc957c49000001810000e7bc00000053; nid_inf=1631157862; NID_AUT=mNO+8XvZHGi+wDfIukaykGursjHL4QHNPkYFKsLDhOgh7+QGMmKkFlp7pQmQzsVL; NID_SES=AAABfA5Na0tDrKMMGrG6BMfr7mqWz56faQm+q9a5O+WZ4ZpAMgWOcIxV+z++EMyQk0qB+Nu9TTJYUGCZsuzi4qL/57aDQYcC4F9vjc1WTJLO2fLSXSYHbFRbbtDDL5t4p47HXLk9Twzdzmi8hK/NYiAXJcLpj4mk8I3bPuKjh86DVFD66qrEnG5IfGJDYCloU1Ry8g0elLXH3YT7v6EZhh1PJJD/YxNbzrneCEMtg+kWYhhrkAsmSAMMDQi5FazPZJ2FYdwLWKRDTrGnhFzJ7iCD8vMiQ+dj1eEe9jxPrKZO/0kdmpU2nLb4S9rj1dDLWhxskjkLGEFsiM47RIyY8CrUYbQikKZqZHC1xFaVbz/JggidJWMIk4q2NBDVqHXP9lDpFRqkaptARpG1BiCIfROm52aFyK/UrpvqJ7CHfxvXQXSqp0ZDV1t/Mdo5xoDptPzO8at7GNiZ8l7bQWhQOhypNNL4vuQgB29BMD9rk79Pbmx3l6x2ZvUwUZq92rdp3uEqlQ==; NID_JKL=LJInBtlDv57Cw5ymKhME3AL6TFoX0rDIhlHPSnitVvQ=; _naver_usersession_=08M+asn3uAx3SMqojoVr1f3u; page_uid=hqjRylprvxZssnErd/wssssstRl-494571',
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
    'start': '61',
    'query': '커피',
    'nso': '',
    'nqx_theme': '',
    'main_q': '',
    'mode': 'normal',
    'q_material': '',
    'ac': '1',
    'aq': '0',
    'spq': '0',
    'st_coll': '',
    'topic_r_cat': '',
    'nx_search_query': '',
    'nx_and_query': '',
    'nx_sub_query': '',
    'prank': '61',
    'sm': 'tab_jum',
    'ssc': 'tab.view.view',
    'ngn_country': 'KR',
    'lgl_rcode': '',
    'fgn_region': '',
    'fgn_city': '',
    'lgl_lat': '',
    'lgl_long': '',
    'abt': '[{"eid":"PWC-AD-UP","value":{"bucket":"0","for":"impression-neo","is_control":true}}]',
    '_callback': 'viewMoreContents',
}

response = requests.get('https://s.search.naver.com/p/review/search.naver', params=params, cookies=cookies, headers=headers)

print(response.text)