import requests

cookies = {
    'NNB': 'DULXWITNGSGGE',
    'nx_ssl': '2',
    'ASID': 'dc957c49000001810000e7bc00000053',
    '_datalab_cid': '50000008',
    '_ga_7VKFYR6RV1': 'GS1.1.1655549940.3.0.1655549940.60',
    '_ga': 'GA1.2.678320805.1655285848',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://datalab.naver.com/keyword/trendResult.naver?hashKey=N_93b845b7c2bcae2475a49b30882cb541',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'NNB=DULXWITNGSGGE; nx_ssl=2; ASID=dc957c49000001810000e7bc00000053; _datalab_cid=50000008; _ga_7VKFYR6RV1=GS1.1.1655549940.3.0.1655549940.60; _ga=GA1.2.678320805.1655285848',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'hashKey': 'N_7a07f3b97e81395371edf504131320b3',
}

response = requests.get('https://datalab.naver.com/keyword/trendResult.naver', params=params, cookies=cookies, headers=headers)