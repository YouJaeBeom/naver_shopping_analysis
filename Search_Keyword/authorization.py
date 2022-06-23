import requests
import json
def authorization():
    cookies = {
        'NNB': 'DULXWITNGSGGE',
        'wcs_bt': 's_18b113b581b2:1655273118|s_116ad1cb421c:1655269226',
        'nx_ssl': '2',
        'ASID': 'dc957c49000001810000e7bc00000053',
        'welcome-sa-popup-mnetsol': '1',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Accept': 'application/json, text/plain, */*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'Origin': 'https://searchad.naver.com',
        'Connection': 'keep-alive',
        'Referer': 'https://searchad.naver.com/',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'NNB=DULXWITNGSGGE; wcs_bt=s_18b113b581b2:1655273118|s_116ad1cb421c:1655269226; nx_ssl=2; ASID=dc957c49000001810000e7bc00000053; welcome-sa-popup-mnetsol=1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    json_data = {
        'loginId': 'mnetsol',
        'loginPwd': 'dpasptthffntus1!',
    }

    response = requests.post('https://searchad.naver.com/auth/login', cookies=cookies, headers=headers, json=json_data)

    response_json = json.loads(response.text)
    Authorization = "Bearer "+response_json['token']

    #print(Authorization)
    return Authorization

# Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbklkIjoibW5ldHNvbCIsInJvbGUiOjAsImNsaWVudElkIjoibWFydmVsIiwiaXNBcGkiOmZhbHNlLCJ1c2VySWQiOjI4NDUyMTAsInVzZXJLZXkiOiI5Y2RhMWFiYS1hZmE0LTRhMzItODQ5My05YTBiYzRhMzkzYmEiLCJjbGllbnRDdXN0b21lcklkIjoyNTY1NjY1LCJpc3N1ZVR5cGUiOiJ1c2VyIiwibmJmIjoxNjU1MjcwNDU3LCJpZHAiOiJpZC1wd2QiLCJjdXN0b21lcklkIjoyNTY1NjY1LCJleHAiOjE2NTUyNzExMTcsImlhdCI6MTY1NTI3MDUxNywianRpIjoiZjczZTc1YzUtZjM4MC00NThkLWFhYzEtZGZiYjk1M2U1YzNmIn0.-sM7uXLyu2dxai1Hpw0OtoAIkzv5qMT7uMplui-0A-k
# Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbklkIjoibW5ldHNvbCIsInJvbGUiOjAsImNsaWVudElkIjoibWFydmVsIiwiaXNBcGkiOmZhbHNlLCJ1c2VySWQiOjI4NDUyMTAsInVzZXJLZXkiOiI5Y2RhMWFiYS1hZmE0LTRhMzItODQ5My05YTBiYzRhMzkzYmEiLCJjbGllbnRDdXN0b21lcklkIjoyNTY1NjY1LCJpc3N1ZVR5cGUiOiJ1c2VyIiwibmJmIjoxNjU1MjcwNDU3LCJpZHAiOiJpZC1wd2QiLCJjdXN0b21lcklkIjoyNTY1NjY1LCJleHAiOjE2NTUyNzExMTcsImlhdCI6MTY1NTI3MDUxNywianRpIjoiZjczZTc1YzUtZjM4MC00NThkLWFhYzEtZGZiYjk1M2U1YzNmIn0.-sM7uXLyu2dxai1Hpw0OtoAIkzv5qMT7uMplui-0A-k
# Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbklkIjoibW5ldHNvbCIsInJvbGUiOjAsImNsaWVudElkIjoibWFydmVsIiwiaXNBcGkiOmZhbHNlLCJ1c2VySWQiOjI4NDUyMTAsInVzZXJLZXkiOiI5Y2RhMWFiYS1hZmE0LTRhMzItODQ5My05YTBiYzRhMzkzYmEiLCJjbGllbnRDdXN0b21lcklkIjoyNTY1NjY1LCJpc3N1ZVR5cGUiOiJ1c2VyIiwibmJmIjoxNjU1MjY5Nzc0LCJpZHAiOiJpZC1wd2QiLCJjdXN0b21lcklkIjoyNTY1NjY1LCJleHAiOjE2NTUyNzA0MzQsImlhdCI6MTY1NTI2OTgzNCwianRpIjoiZDgwNDhiOGYtNjA0Zi00ODk0LWEwZWUtNWM4Njc4NWVlY2MyIn0.tM2Eir209KnZtHM6hhjX7u-Yi7sbTVYekKYs8SkXGdw