import requests

cookies = {
    'autocomplete': 'use',
    'NNB': 'DULXWITNGSGGE',
    'AD_SHP_BID': '14',
    'ncpa': '577694|l3jhfkb4|5c4aebfb3ae71c9d046d64b03ea02baef29c2da0|s_322e2a23da456|e29bb1084901f870391d6e5eb631b0f7e0af83bb',
    'nx_ssl': '2',
    'BMR': 's=1653361410979&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.naver%3FisHttpsRedirect%3Dtrue%26blogId%3Dtjdgus0804%26logNo%3D221483452609&r2=https%3A%2F%2Fwww.google.com%2F',
    'page_uid': 'hoxEXlp0JXossQyWmH0ssssss6Z-382117',
    'spage_uid': 'hoxEXlp0JXossQyWmH0ssssss6Z-382117',
    'sus_val': 'DU+jGrUx764rkBLp7kywSuz6',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Accept': 'application/json, text/plain, */*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://search.shopping.naver.com/search/all?frm=NVSCTAB&origQuery=%EB%A7%88%EC%8A%A4%ED%81%AC&pagingIndex=2&pagingSize=40&productSet=total&query=%EB%A7%88%EC%8A%A4%ED%81%AC&sort=rel&timestamp=&viewType=list',
    'logic': 'PART',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'autocomplete=use; NNB=DULXWITNGSGGE; AD_SHP_BID=14; ncpa=577694|l3jhfkb4|5c4aebfb3ae71c9d046d64b03ea02baef29c2da0|s_322e2a23da456|e29bb1084901f870391d6e5eb631b0f7e0af83bb; nx_ssl=2; BMR=s=1653361410979&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.naver%3FisHttpsRedirect%3Dtrue%26blogId%3Dtjdgus0804%26logNo%3D221483452609&r2=https%3A%2F%2Fwww.google.com%2F; page_uid=hoxEXlp0JXossQyWmH0ssssss6Z-382117; spage_uid=hoxEXlp0JXossQyWmH0ssssss6Z-382117; sus_val=DU+jGrUx764rkBLp7kywSuz6',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'sort': 'rel',
    'pagingIndex': '1',
    'pagingSize': '80',
    'viewType': 'list',
    'productSet': 'total',
    'deliveryFee': '',
    'deliveryTypeValue': '',
    'frm': 'NVSCTAB',
    'query': '마스크',
    'origQuery': '마스크',
    'iq': '',
    'eq': '',
    'xq': '',
}

response = requests.get('https://search.shopping.naver.com/api/search/all', params=params, cookies=cookies, headers=headers)
print(response.text)