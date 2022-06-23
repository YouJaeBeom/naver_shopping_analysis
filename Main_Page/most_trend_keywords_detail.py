import requests
import json
cookies = {
    'autocomplete': 'use',
    'NNB': 'DULXWITNGSGGE',
    'AD_SHP_BID': '14',
    'nx_ssl': '2',
    'ASID': 'dc957c49000001810000e7bc00000053',
    'spage_uid': 'hqjkmwprvxZssnWiWKossssssiZ-021170',
    'nid_inf': '1631157862',
    'NID_AUT': 'mNO+8XvZHGi+wDfIukaykGursjHL4QHNPkYFKsLDhOgh7+QGMmKkFlp7pQmQzsVL',
    'NID_SES': 'AAABg91nKuVWqyEsp6EVitlj2OAfQc+yMu/eFyYd2xJgmZXzjGLl+6f68QsPSWtltzqovjku8wKxAfquxdlNsPs3aQNLEjSM2M7yAla3vtDOnQR37XRwj45uRJoavyvZC0yZvoRz/5q33E4GMDsgsfxbdYIcEHc0IyK3WBi4icNuUXOr1VAAp7hl4svHUDl0R/bwNa3HZO8S2mZ/lerE6J0hELK6rzDy5O0ez+lxMxlkq+7R/ac99qUCe+lUgC0ahZEK2K/S5o5fQXMCHXjaBkrcCioHbW0zZtmbnTzSuOcv8L4HW3ENHsHeEL7PYLW6s/0GS2a+bE0rTwQMppm0uJfFQwTfqO1JtyMvMQ8nMCl0SREzxJlKJoR0t/zs5ypEwW+HF7wQgWOa/AE9rKYPqHLZRHundFQZp+DAEy/cRLldXFfRJeNIdrj6gBdyXJJbOoQFwx8lJpNJmx1tKp6RuI+l2/aeiM+hUAM5u4CjfpG10BOHfbmgZ2/5sSM8B06zhPMUsfL+/oAV7fYHfxnSwBte380=',
    'NID_JKL': 'LJInBtlDv57Cw5ymKhME3AL6TFoX0rDIhlHPSnitVvQ=',
    'ncpa': '4858315|l4c1twbk|927c5e8482564b12efddb8c575f00f5681a192cf|s_13896d3b7eb40|80d374f4447f0553390bd4a7a2222ba0bef775e5:24|l4c223ug|16b3d132050c58936acc83d407694a7f82eb0e7f|s_419afe53a6bb|216ef0a30e6d34008cf0f68fe952a9cce5495d89:17703|l4c2566o|b24d363fd3e9061389bd93ce70695d674b6ac017|s_1f0b6dd345b2|c562e5d711af772c2575bbc0de754568bf7bfd61:95694|l4c6438w|e2dd271a1f76c70407bb2aca54d87405d35dcd8b|null|6616f5118b0e16be4b405a2e6498994a689f5051',
    'page_uid': 'hqjkmwprvxZssnWiWKossssssiZ-021170',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://search.shopping.naver.com/best/category/keyword?categoryCategoryId=ALL&categoryChildCategoryId=&categoryDemo=M04&categoryMidCategoryId=&categoryRootCategoryId=ALL&chartRank=2&period=P1D',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    'Origin': 'https://search.shopping.naver.com',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'autocomplete=use; NNB=DULXWITNGSGGE; AD_SHP_BID=14; nx_ssl=2; ASID=dc957c49000001810000e7bc00000053; spage_uid=hqjkmwprvxZssnWiWKossssssiZ-021170; nid_inf=1631157862; NID_AUT=mNO+8XvZHGi+wDfIukaykGursjHL4QHNPkYFKsLDhOgh7+QGMmKkFlp7pQmQzsVL; NID_SES=AAABg91nKuVWqyEsp6EVitlj2OAfQc+yMu/eFyYd2xJgmZXzjGLl+6f68QsPSWtltzqovjku8wKxAfquxdlNsPs3aQNLEjSM2M7yAla3vtDOnQR37XRwj45uRJoavyvZC0yZvoRz/5q33E4GMDsgsfxbdYIcEHc0IyK3WBi4icNuUXOr1VAAp7hl4svHUDl0R/bwNa3HZO8S2mZ/lerE6J0hELK6rzDy5O0ez+lxMxlkq+7R/ac99qUCe+lUgC0ahZEK2K/S5o5fQXMCHXjaBkrcCioHbW0zZtmbnTzSuOcv8L4HW3ENHsHeEL7PYLW6s/0GS2a+bE0rTwQMppm0uJfFQwTfqO1JtyMvMQ8nMCl0SREzxJlKJoR0t/zs5ypEwW+HF7wQgWOa/AE9rKYPqHLZRHundFQZp+DAEy/cRLldXFfRJeNIdrj6gBdyXJJbOoQFwx8lJpNJmx1tKp6RuI+l2/aeiM+hUAM5u4CjfpG10BOHfbmgZ2/5sSM8B06zhPMUsfL+/oAV7fYHfxnSwBte380=; NID_JKL=LJInBtlDv57Cw5ymKhME3AL6TFoX0rDIhlHPSnitVvQ=; ncpa=4858315|l4c1twbk|927c5e8482564b12efddb8c575f00f5681a192cf|s_13896d3b7eb40|80d374f4447f0553390bd4a7a2222ba0bef775e5:24|l4c223ug|16b3d132050c58936acc83d407694a7f82eb0e7f|s_419afe53a6bb|216ef0a30e6d34008cf0f68fe952a9cce5495d89:17703|l4c2566o|b24d363fd3e9061389bd93ce70695d674b6ac017|s_1f0b6dd345b2|c562e5d711af772c2575bbc0de754568bf7bfd61:95694|l4c6438w|e2dd271a1f76c70407bb2aca54d87405d35dcd8b|null|6616f5118b0e16be4b405a2e6498994a689f5051; page_uid=hqjkmwprvxZssnWiWKossssssiZ-021170',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

json_data = {
    'query': '\n      query ChartProductList($params: ChartProductListInput, $exposeLogSourceInfo: ExposeLogSourceInfo) {\n        KeywordChartProductList(params: $params, exposeLogSourceInfo: $exposeLogSourceInfo) {\n            nvMid\n            imageUrl\n            mobileLowPrice\n            priceUnit\n            productTitle\n            purchaseCnt\n            mallCount\n            mpTp\n            reviewCount\n            mallProductUrl\n            mallProdMblUrl\n            dlvryCd\n            productCrUrl\n        }\n      }\n    ',
    'variables': {
        'params': {
            'chartTitle': '종이가구',
            'categoryId': 'ALL',
            'rankedDate': '20220612',
            'demo': 'M04',
            'period': 'P1D',
            'productType': 'ALL',
            'rankStart': 1,
            'rankEnd': 20,
        },
        'exposeLogSourceInfo': {
            'isMobileDomain': False,
            'pageType': 'Category',
        },
    },
}

response = requests.post('https://search.shopping.naver.com/best/api/graphql', cookies=cookies, headers=headers, json=json_data)

response_json = json.loads(response.text)
charts =  response_json['data']['KeywordChartProductList']


print(charts[len(charts)-1])
print(len(charts))