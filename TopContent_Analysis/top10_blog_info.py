import requests

cookies = {
    'NNB': 'DULXWITNGSGGE',
    'nx_ssl': '2',
    'ASID': 'dc957c49000001810000e7bc00000053',
    '_ga_7VKFYR6RV1': 'GS1.1.1655549940.3.0.1655549940.60',
    '_ga': 'GA1.2.678320805.1655285848',
    '066c80626d06ffa5b32035f35cabe88d': 'j%C2%C3%F4F%26Bn%C1%D7KUBX%99%11%0C5%00%C4B6l-%A3%7C%D2%FE%AC%D8%83%98%B4f%0D.%96n%25WA%A4Y%ED%05%3F%0A%8Ai%40%98%3F%19%2C%EE%FCHnL%8B%99%C3%8E2%91%92%AC%14%F0%A7M%0C%A6%82%1B%ED%9D%5B6%FF%21%8CN%2C%5C%1A%C0%C2%89%EC+%CA_%064%A5%3F%83J%5B%5CQ%C4%92%A8%C0%E3%EB%3A2t%9B%B4%82%CB%9A%1C%27%06%D4%C4%8E%F2%22%EE%DC%A4%1CL%02%F7%40%B5%BA%8D%AA',
    '1a5b69166387515780349607c54875af': '%C1%F9%27nc%D2%A4%82',
    'page_uid': 'hra9EsprvhGssnoGkFwssssstHw-110491',
    'JSESSIONID': '4A271B567628D4B0CBC52E5697016437.jvm1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://blog.naver.com/hearteffect',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'NNB=DULXWITNGSGGE; nx_ssl=2; ASID=dc957c49000001810000e7bc00000053; _ga_7VKFYR6RV1=GS1.1.1655549940.3.0.1655549940.60; _ga=GA1.2.678320805.1655285848; 066c80626d06ffa5b32035f35cabe88d=j%C2%C3%F4F%26Bn%C1%D7KUBX%99%11%0C5%00%C4B6l-%A3%7C%D2%FE%AC%D8%83%98%B4f%0D.%96n%25WA%A4Y%ED%05%3F%0A%8Ai%40%98%3F%19%2C%EE%FCHnL%8B%99%C3%8E2%91%92%AC%14%F0%A7M%0C%A6%82%1B%ED%9D%5B6%FF%21%8CN%2C%5C%1A%C0%C2%89%EC+%CA_%064%A5%3F%83J%5B%5CQ%C4%92%A8%C0%E3%EB%3A2t%9B%B4%82%CB%9A%1C%27%06%D4%C4%8E%F2%22%EE%DC%A4%1CL%02%F7%40%B5%BA%8D%AA; 1a5b69166387515780349607c54875af=%C1%F9%27nc%D2%A4%82; page_uid=hra9EsprvhGssnoGkFwssssstHw-110491; JSESSIONID=4A271B567628D4B0CBC52E5697016437.jvm1',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'blogId': 'hearteffect',
    'widgetTypeCall': 'true',
    'directAccess': 'true',
}

response = requests.get('https://blog.naver.com/PostList.naver', params=params, cookies=cookies, headers=headers)

with open("TextFile.txt", "w") as file:
    file.write(response.text)

print(response.text)