from tkinter.messagebox import NO
import requests
import json
import authorization

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

def search_volume(keyword):
    Authorization = authorization.authorization()

    cookies = {
    'NNB': 'DULXWITNGSGGE',
    'nx_ssl': '2',
    'ASID': 'dc957c49000001810000e7bc00000053',
    '066c80626d06ffa5b32035f35cabe88d': 'j%C2%C3%F4F%26Bn%C1%D7KUBX%99%11%15wB%DB%D1%29K%E0%99%97g%8B%EBz%9C%FEu%40%F9%D4%9D%25b%E6%CA%19%05%BCD%C5%C0%FD%92Z%8B%BF%24%B5%60%13HnL%8B%99%C3%8E2%91%92%AC%14%F0%A7M%0C%A6%82%1B%ED%9D%5B6%FFb%D7C%80%86%F9N%F14f%22%89i%F4%09%00%96%3D%18F%FD%C2%EC%92%A8%C0%E3%EB%3A2t%9B%B4%82%CB%9A%1C%27%06%D4%BBa%8A%16i%90%2B%D2%A0%F4%D0%7E%C5%B7%2A%BE',
    '1a5b69166387515780349607c54875af': '%C1%F9%27nc%D2%A4%82',
    '1b25d439ceac51f5d414df7689017f6c': '%AE%E2%BFK%3D%9B%07K%FD%15%0B%15%DC%97%95%C4%A3%B8%DD%E9%D6%3F%12a%3B%D6%CDj%DA%11%DCB%BB%2B%19%3B%C37%C1%CA%14%7D%7C%11%B9%15%25%83%13%EF%83%24%C1%CB%5C%3E%C7%A4%8DDz%92%C3%0F%82%AA%C8%DC%81%AA%ABq%B0%E7e%3D%E3%A5%A9%A3kD%A6%E8%AC%AD%CF%ED%F8%14tz%5B%F2J%EBya%B8%1D%E4%C0%C9%23%87%8F%1Am%FA%7B%E3%B4%5C6%CC%C9%D4%5D%F2F7A%E3%090K%EA%DC%FA%12%E3%F9%11%25%C0%B1%E0%EA7%8D%E5%E9%21%5E%5B%A1%93%B4%2A%27M%F2g%1D%3A%0D%F9%FD%C6Fd%9B%A5%F4%A6A%F8%EA%B1%F3%2AK%A8%7E%F4%CC%2F%E6%BDv%97%5BH%ACV%C6%1E%B3%F5%B1%B6%BE%7B%8A%BD%CAv%AE%01%ED%18%EE%10%0ARB%A7%C3%27%5Bv%14%97%83S1%7C%B4%BD%84%06%9D%91%BD%26j%B0%18%00%7D%18%8F%0F%F4%0F%1B%DF%CCW%FA%0BcM%89qA%AB%5C%E5%D1%8DD%C9%A6%E5u0%F3%FC3%7Cr%9D%EB%18%26%EB%D4%EF%AF%EF%FF%CC%3C%BF%91%0D%CDC%C3%85%5EC%BE%3E%90%89%BC%8CD%E35%25LC%E7m%CE%5B%FC%1Cj%EFn%27E%5BB%10%81+%93K%FARcJ%82%1E%EA%D3%8D%BD%A6%3B%05%E5%3D%0F%F4%0F%1B%DF%CCW%FA%0BcM%89qA%AB%5C%E5%D1%8DD%C9%A6%E5uD%FE%91e%F8%2A%F3r%EEo.%27%D6%2BXl%29K%E2%98%95p%2F%CD%C1%25%A4%8D%D7%5E%F4T%BAX%29FA%D9%12%87%DCQrO%FA%E9%EE%C7%95.A%25%88%3B%B9G%1Bw%E2U%EAV%D7%EA%27S%15%F31%83%CB%87%A6c%247%F1%88%28X%0F%FC%D7%3F%93%7DT%E6%D5%0D%CB%24%06%17%82%05f%C2%12%EE%ED%A0%BA%13%AE%BE%87%CDL%BC%0C%139%C4%251E%E0%E4%175%F0%3C%81s%17%F0.%19%EDx%BFn%9A%F8%C5%CD%97E%A1%BF%BE%AE%12%9B%CA%83%15%F2l%91%9E%A6%99%B3b%19P%B2%8ENd%22%DDpAH%DE%92%DA%C2%AC%0F%5D%E94%FC%88%82LN%F5%24J%A1E%A6%2A%24%9Dr%04%A2T%C0%EAz%2BO%3C%89%88%A0q%CB0L%15%CFy%2Cbv%CF2%DC',
    'elicjyl': 'true',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Accept': 'application/json, text/plain, */*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Authorization': (Authorization),
        'Connection': 'keep-alive',
        'Referer': 'https://manage.searchad.naver.com/customers/2565665/tool/keyword-planner',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'NNB=DULXWITNGSGGE; nx_ssl=2; ASID=dc957c49000001810000e7bc00000053; 066c80626d06ffa5b32035f35cabe88d=j%C2%C3%F4F%26Bn%C1%D7KUBX%99%11%15wB%DB%D1%29K%E0%99%97g%8B%EBz%9C%FEu%40%F9%D4%9D%25b%E6%CA%19%05%BCD%C5%C0%FD%92Z%8B%BF%24%B5%60%13HnL%8B%99%C3%8E2%91%92%AC%14%F0%A7M%0C%A6%82%1B%ED%9D%5B6%FFb%D7C%80%86%F9N%F14f%22%89i%F4%09%00%96%3D%18F%FD%C2%EC%92%A8%C0%E3%EB%3A2t%9B%B4%82%CB%9A%1C%27%06%D4%BBa%8A%16i%90%2B%D2%A0%F4%D0%7E%C5%B7%2A%BE; 1a5b69166387515780349607c54875af=%C1%F9%27nc%D2%A4%82; 1b25d439ceac51f5d414df7689017f6c=%AE%E2%BFK%3D%9B%07K%FD%15%0B%15%DC%97%95%C4%A3%B8%DD%E9%D6%3F%12a%3B%D6%CDj%DA%11%DCB%BB%2B%19%3B%C37%C1%CA%14%7D%7C%11%B9%15%25%83%13%EF%83%24%C1%CB%5C%3E%C7%A4%8DDz%92%C3%0F%82%AA%C8%DC%81%AA%ABq%B0%E7e%3D%E3%A5%A9%A3kD%A6%E8%AC%AD%CF%ED%F8%14tz%5B%F2J%EBya%B8%1D%E4%C0%C9%23%87%8F%1Am%FA%7B%E3%B4%5C6%CC%C9%D4%5D%F2F7A%E3%090K%EA%DC%FA%12%E3%F9%11%25%C0%B1%E0%EA7%8D%E5%E9%21%5E%5B%A1%93%B4%2A%27M%F2g%1D%3A%0D%F9%FD%C6Fd%9B%A5%F4%A6A%F8%EA%B1%F3%2AK%A8%7E%F4%CC%2F%E6%BDv%97%5BH%ACV%C6%1E%B3%F5%B1%B6%BE%7B%8A%BD%CAv%AE%01%ED%18%EE%10%0ARB%A7%C3%27%5Bv%14%97%83S1%7C%B4%BD%84%06%9D%91%BD%26j%B0%18%00%7D%18%8F%0F%F4%0F%1B%DF%CCW%FA%0BcM%89qA%AB%5C%E5%D1%8DD%C9%A6%E5u0%F3%FC3%7Cr%9D%EB%18%26%EB%D4%EF%AF%EF%FF%CC%3C%BF%91%0D%CDC%C3%85%5EC%BE%3E%90%89%BC%8CD%E35%25LC%E7m%CE%5B%FC%1Cj%EFn%27E%5BB%10%81+%93K%FARcJ%82%1E%EA%D3%8D%BD%A6%3B%05%E5%3D%0F%F4%0F%1B%DF%CCW%FA%0BcM%89qA%AB%5C%E5%D1%8DD%C9%A6%E5uD%FE%91e%F8%2A%F3r%EEo.%27%D6%2BXl%29K%E2%98%95p%2F%CD%C1%25%A4%8D%D7%5E%F4T%BAX%29FA%D9%12%87%DCQrO%FA%E9%EE%C7%95.A%25%88%3B%B9G%1Bw%E2U%EAV%D7%EA%27S%15%F31%83%CB%87%A6c%247%F1%88%28X%0F%FC%D7%3F%93%7DT%E6%D5%0D%CB%24%06%17%82%05f%C2%12%EE%ED%A0%BA%13%AE%BE%87%CDL%BC%0C%139%C4%251E%E0%E4%175%F0%3C%81s%17%F0.%19%EDx%BFn%9A%F8%C5%CD%97E%A1%BF%BE%AE%12%9B%CA%83%15%F2l%91%9E%A6%99%B3b%19P%B2%8ENd%22%DDpAH%DE%92%DA%C2%AC%0F%5D%E94%FC%88%82LN%F5%24J%A1E%A6%2A%24%9Dr%04%A2T%C0%EAz%2BO%3C%89%88%A0q%CB0L%15%CFy%2Cbv%CF2%DC; elicjyl=true',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        'format': 'json',
        'hintKeywords': keyword,
        'siteId': '',
        'month': '',
        'biztpId': '',
        'event': '',
        'includeHintKeywords': '0',
        'showDetail': '1',
        'keyword': '',
    }

    response = requests.get('https://manage.searchad.naver.com/keywordstool', params=params, cookies=cookies, headers=headers)

    response_json = json.loads(response.text)
    monthlyPcQcCnt =  response_json['keywordList'][0]['monthlyPcQcCnt']
    monthlyMobileQcCnt =  response_json['keywordList'][0]['monthlyMobileQcCnt']

    return monthlyPcQcCnt, monthlyMobileQcCnt

if __name__ == "__main__" :
    keyword="마스크"
    total_count= products_count(keyword)
    print(total_count)

    monthlyPcQcCnt, monthlyMobileQcCnt = search_volume(keyword)
    print(monthlyPcQcCnt, monthlyMobileQcCnt)

    comp = total_count / (monthlyPcQcCnt+monthlyMobileQcCnt)
    print("경쟁률 : %.2f"%comp)