import requests
import json
def getagerate(start, end, keyword):
    cookies = {
        'NNB': 'DULXWITNGSGGE',
        'nx_ssl': '2',
        'ASID': 'dc957c49000001810000e7bc00000053',
        '_datalab_cid': '50000000',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:100.0) Gecko/20100101 Firefox/100.0',
        'Accept': '*/*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://datalab.naver.com/shoppingInsight/sCategory.naver',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://datalab.naver.com',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'NNB=DULXWITNGSGGE; nx_ssl=2; ASID=dc957c49000001810000e7bc00000053; _datalab_cid=50000000',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = {
        'cid': '50000000', ## category unique id 
        'timeUnit': 'date',
        'startDate': start,
        'endDate': end,
        'age': '',
        'gender': '',
        'device': '',
        'keyword': keyword,
    }

    response = requests.post('https://datalab.naver.com/shoppingInsight/getCategoryAgeRate.naver', cookies=cookies, headers=headers, data=data)

    response_json = json.loads(response.text)
    data =  response_json['result'][0]['data']


    return data