import requests
import json


def products_count(keyword):
    cookies = {
        'autocomplete': 'use',
        'NNB': 'DULXWITNGSGGE',
        'AD_SHP_BID': '14',
        'nx_ssl': '2',
        'ASID': 'dc957c49000001810000e7bc00000053',
        'spage_uid': 'hqkXgwp0JXVssl%2BA4O4sssssses-212213',
        'nid_inf': '1631157862',
        'NID_AUT': 'mNO+8XvZHGi+wDfIukaykGursjHL4QHNPkYFKsLDhOgh7+QGMmKkFlp7pQmQzsVL',
        'NID_SES': 'AAABh259TUUHZQsWwogvQUfaRXTSQGwK9a2StlRX6j1NwEoKamx2/9c91GRfQZ/tFvp33QkbmTe1Ik0a0tcf9NptksIZSsQWOp5sXTy8AY7mAvhKPmQiHOtg+cr5VyhBc9Hjwm8+wmlAORPMn0L3fQCJjLYVPerEGGZMHXqxstXtYQQIOHM1SrSWmzaltFYqANfkcCDefr1LNKqLDrWwIMOAbF5NH5BKLOmK4W+PUc5K7bkR/4Rs9w8CK+tdyHsl1zUw5sUWtZTdM2jQlAl/3414ipPPn20rDbaVtS+9RWxRKX52YFzbNUq9vPkheHXPgKqfxyaV6yT8UtgS3kUSqhFI+ADKHQwji3mwKeNehsNkSOEVMuUFcyJBJMRpno9yrBr8vj1RPPFCnocaTwVTypspVCnZuj2M4wqGGgLTEKud9YdaJ8MFZYFDq3pJt8k13leGHL8YbcEGfCYAKICZEKPIZ1JDxoW7vpLdH4h8t46YVVAw4AmeIwPf//tIitkP/b4a4ZYZdIxC5NsJZIdH4lUlDeU=',
        'NID_JKL': 'LJInBtlDv57Cw5ymKhME3AL6TFoX0rDIhlHPSnitVvQ=',
        'ncpa': '4858315|l4c1twbk|927c5e8482564b12efddb8c575f00f5681a192cf|s_13896d3b7eb40|80d374f4447f0553390bd4a7a2222ba0bef775e5:24|l4c223ug|16b3d132050c58936acc83d407694a7f82eb0e7f|s_419afe53a6bb|216ef0a30e6d34008cf0f68fe952a9cce5495d89:17703|l4c2566o|b24d363fd3e9061389bd93ce70695d674b6ac017|s_1f0b6dd345b2|c562e5d711af772c2575bbc0de754568bf7bfd61:95694|l4c6438w|e2dd271a1f76c70407bb2aca54d87405d35dcd8b|null|6616f5118b0e16be4b405a2e6498994a689f5051:3397058|l4cgfvi8|68c46f74bc8222f37936b0030b185d436a1c117e|s_1889b764f1ab1|5997dc1d0fcc96d3f81fc165e9fae0f24da2cae7:840287|l4chv9tc|856381a940f83e36da19aaf455912f373230c980|s_b8805abdaa43|8a4d7ba04e238314e761f1d4cd12cfbbb90980de:2938149|l4cirrkg|2aa7de5a2656034185f93545581918e1c9885b58|s_1c4c50d92220|06cba5a379a0a1fa7a6d145674ffde9c7c0a2e72:13|l4cixjwg|85fc531067a7babf9adb1fe5f04e6ee3e9183b57|s_108048c3874|09e1f3929a1a78fde305e3585a1bd3ab8fd8ab4e',
        'page_uid': 'hqkXgwp0JXVssl+A4O4sssssses-212213',
        'sus_val': 'R+Us1My4+ot7NM6LjIBH1FIj',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Accept': 'application/json, text/plain, */*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://search.shopping.naver.com/search/all?frm=NVSHTTL&origQuery=%EB%82%98%EC%9D%B4%ED%82%A4&pagingIndex=1&pagingSize=40&productSet=total&query=%EB%82%98%EC%9D%B4%ED%82%A4&sort=rel&timestamp=&viewType=list',
        'logic': 'PART',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'autocomplete=use; NNB=DULXWITNGSGGE; AD_SHP_BID=14; nx_ssl=2; ASID=dc957c49000001810000e7bc00000053; spage_uid=hqkXgwp0JXVssl%2BA4O4sssssses-212213; nid_inf=1631157862; NID_AUT=mNO+8XvZHGi+wDfIukaykGursjHL4QHNPkYFKsLDhOgh7+QGMmKkFlp7pQmQzsVL; NID_SES=AAABh259TUUHZQsWwogvQUfaRXTSQGwK9a2StlRX6j1NwEoKamx2/9c91GRfQZ/tFvp33QkbmTe1Ik0a0tcf9NptksIZSsQWOp5sXTy8AY7mAvhKPmQiHOtg+cr5VyhBc9Hjwm8+wmlAORPMn0L3fQCJjLYVPerEGGZMHXqxstXtYQQIOHM1SrSWmzaltFYqANfkcCDefr1LNKqLDrWwIMOAbF5NH5BKLOmK4W+PUc5K7bkR/4Rs9w8CK+tdyHsl1zUw5sUWtZTdM2jQlAl/3414ipPPn20rDbaVtS+9RWxRKX52YFzbNUq9vPkheHXPgKqfxyaV6yT8UtgS3kUSqhFI+ADKHQwji3mwKeNehsNkSOEVMuUFcyJBJMRpno9yrBr8vj1RPPFCnocaTwVTypspVCnZuj2M4wqGGgLTEKud9YdaJ8MFZYFDq3pJt8k13leGHL8YbcEGfCYAKICZEKPIZ1JDxoW7vpLdH4h8t46YVVAw4AmeIwPf//tIitkP/b4a4ZYZdIxC5NsJZIdH4lUlDeU=; NID_JKL=LJInBtlDv57Cw5ymKhME3AL6TFoX0rDIhlHPSnitVvQ=; ncpa=4858315|l4c1twbk|927c5e8482564b12efddb8c575f00f5681a192cf|s_13896d3b7eb40|80d374f4447f0553390bd4a7a2222ba0bef775e5:24|l4c223ug|16b3d132050c58936acc83d407694a7f82eb0e7f|s_419afe53a6bb|216ef0a30e6d34008cf0f68fe952a9cce5495d89:17703|l4c2566o|b24d363fd3e9061389bd93ce70695d674b6ac017|s_1f0b6dd345b2|c562e5d711af772c2575bbc0de754568bf7bfd61:95694|l4c6438w|e2dd271a1f76c70407bb2aca54d87405d35dcd8b|null|6616f5118b0e16be4b405a2e6498994a689f5051:3397058|l4cgfvi8|68c46f74bc8222f37936b0030b185d436a1c117e|s_1889b764f1ab1|5997dc1d0fcc96d3f81fc165e9fae0f24da2cae7:840287|l4chv9tc|856381a940f83e36da19aaf455912f373230c980|s_b8805abdaa43|8a4d7ba04e238314e761f1d4cd12cfbbb90980de:2938149|l4cirrkg|2aa7de5a2656034185f93545581918e1c9885b58|s_1c4c50d92220|06cba5a379a0a1fa7a6d145674ffde9c7c0a2e72:13|l4cixjwg|85fc531067a7babf9adb1fe5f04e6ee3e9183b57|s_108048c3874|09e1f3929a1a78fde305e3585a1bd3ab8fd8ab4e; page_uid=hqkXgwp0JXVssl+A4O4sssssses-212213; sus_val=R+Us1My4+ot7NM6LjIBH1FIj',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    params = {
        'sort': 'rel',
        'pagingIndex': '1',
        'pagingSize': '40',
        'viewType': 'list',
        'productSet': 'total',
        'deliveryFee': '',
        'deliveryTypeValue': '',
        'frm': 'NVSHTTL',
        'query': keyword,
        'origQuery': keyword,
        'iq': '',
        'eq': '',
        'xq': '',
        'window': '',
    }

    response = requests.get('https://search.shopping.naver.com/api/search/all', params=params, cookies=cookies, headers=headers)

    response_json = json.loads(response.text)
    total_count =  response_json['shoppingResult']['total']

    return  total_count 

if __name__ == "__main__" :
    keyword="마스크"
    total_count= products_count(keyword)
    print(total_count)