import requests

cookies = {
    'autocomplete': 'use',
    'NNB': 'DULXWITNGSGGE',
    'AD_SHP_BID': '14',
    'nx_ssl': '2',
    'spage_uid': '',
    '066c80626d06ffa5b32035f35cabe88d': 'j%C2%C3%F4F%26Bn%C1%D7KUBX%99%11%0F%8A%7F%D5%14+%00%9EtF%3E%13%9A%B4%C80%E3%0F+%9E%A3%1Co%9Fi%A4%7D%09C%3E2%1A%E2%2F%1BCW8%15%B5HnL%8B%99%C3%8E2%91%92%AC%14%F0%A7M%0C%F9%FB%CC%5D%ED%60T%F3%A2%18%0FU%07%E7.%9F%83%9D%07r%FC%D5%22%BCC%85%B7p%7C%24%E9%B9%A8%C0%E3%EB%3A2t%9B%B4%82%CB%9A%1C%27%06%D4%08%8B%E4%9Bh%D32%BD%A1%EC%B6%5C%C4%01%85%8E',
    '1a5b69166387515780349607c54875af': '%C1%F9%27nc%D2%A4%82',
    'ASID': 'dc957c49000001810000e7bc00000053',
    'sus_val': 'a+hBVpgwfrQwZOgPRA+kf89u',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://search.shopping.naver.com/best/category/click?categoryCategoryId=ALL&categoryDemo=A00&categoryRootCategoryId=ALL&chartRank=1&period=P7D',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    'Origin': 'https://search.shopping.naver.com',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'autocomplete=use; NNB=DULXWITNGSGGE; AD_SHP_BID=14; nx_ssl=2; spage_uid=; 066c80626d06ffa5b32035f35cabe88d=j%C2%C3%F4F%26Bn%C1%D7KUBX%99%11%0F%8A%7F%D5%14+%00%9EtF%3E%13%9A%B4%C80%E3%0F+%9E%A3%1Co%9Fi%A4%7D%09C%3E2%1A%E2%2F%1BCW8%15%B5HnL%8B%99%C3%8E2%91%92%AC%14%F0%A7M%0C%F9%FB%CC%5D%ED%60T%F3%A2%18%0FU%07%E7.%9F%83%9D%07r%FC%D5%22%BCC%85%B7p%7C%24%E9%B9%A8%C0%E3%EB%3A2t%9B%B4%82%CB%9A%1C%27%06%D4%08%8B%E4%9Bh%D32%BD%A1%EC%B6%5C%C4%01%85%8E; 1a5b69166387515780349607c54875af=%C1%F9%27nc%D2%A4%82; ASID=dc957c49000001810000e7bc00000053; sus_val=a+hBVpgwfrQwZOgPRA+kf89u',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

json_data = {
    'query': '\n        query CategoryProducts(\n          $categoryId: String\n          $demo: DemoType\n          $rankType: RankType\n          $period: RankPeriod\n          $productType: ProductType\n          $productCount: Int\n          $exposeLogSourceInfo: ExposeLogSourceInfo\n        ) {\n          CategoryProducts(\n            categoryId: $categoryId\n            demo: $demo\n            rankType: $rankType\n            period: $period\n            productType: $productType\n            productCount: $productCount\n            exposeLogSourceInfo: $exposeLogSourceInfo\n          ) {\n            categoryId\n            demo\n            period\n            rankType\n            rankedDate\n            products {\n              rank\n              nvMid\n              imageUrl\n              mobileLowPrice\n              priceUnit\n              productTitle\n              productName\n              mallCount\n              mallName\n              mallProductUrl\n              mallProdMblUrl\n              isNaverPay\n              isMblNaverPay\n              nPayPcType\n              nPayMblType\n              mpTp\n              dlvryCont\n              productCrUrl\n            }\n          }\n        }\n      ',
    'variables': {
        'demo': 'A00',
        'rankType': 'CLICK',
        'categoryId': 'ALL',
        'productCount': 100,
        'period': 'P7D',
        'productType': 'ALL',
        'exposeLogSourceInfo': {
            'isMobileDomain': False,
            'pageType': 'Category',
        },
    },
}

response = requests.post('https://search.shopping.naver.com/best/api/graphql', cookies=cookies, headers=headers, json=json_data)