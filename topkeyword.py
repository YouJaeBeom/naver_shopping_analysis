import requests

cookies = {
    'NNB': 'DULXWITNGSGGE',
    '_datalab_cid': '50000001',
    'nx_ssl': '2',
    'BMR': 's=1653361410979&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.naver%3FisHttpsRedirect%3Dtrue%26blogId%3Dtjdgus0804%26logNo%3D221483452609&r2=https%3A%2F%2Fwww.google.com%2F',
    'page_uid': 'hoxEXlp0JXossQyWmH0ssssss6Z-382117',
    '066c80626d06ffa5b32035f35cabe88d': 'j%C2%C3%F4F%26Bn%C1%D7KUBX%99%11%0F%8A%7F%D5%14+%00%9EtF%3E%13%9A%B4%C80%E3%0F+%9E%A3%1Co%9Fi%A4%7D%09C%3E2%1A%E2%2F%1BCW8%15%B5HnL%8B%99%C3%8E2%91%92%AC%14%F0%A7M%0C%F9%FB%CC%5D%ED%60T%F3%A2%18%0FU%07%E7.%9F%83%9D%07r%FC%D5%22%BCC%85%B7p%7C%24%E9%B9%A8%C0%E3%EB%3A2t%9B%B4%82%CB%9A%1C%27%06%D4%08%8B%E4%9Bh%D32%BD%A1%EC%B6%5C%C4%01%85%8E',
    '1a5b69166387515780349607c54875af': '%C1%F9%27nc%D2%A4%82',
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
    # 'Cookie': 'NNB=DULXWITNGSGGE; _datalab_cid=50000001; nx_ssl=2; BMR=s=1653361410979&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.naver%3FisHttpsRedirect%3Dtrue%26blogId%3Dtjdgus0804%26logNo%3D221483452609&r2=https%3A%2F%2Fwww.google.com%2F; page_uid=hoxEXlp0JXossQyWmH0ssssss6Z-382117; 066c80626d06ffa5b32035f35cabe88d=j%C2%C3%F4F%26Bn%C1%D7KUBX%99%11%0F%8A%7F%D5%14+%00%9EtF%3E%13%9A%B4%C80%E3%0F+%9E%A3%1Co%9Fi%A4%7D%09C%3E2%1A%E2%2F%1BCW8%15%B5HnL%8B%99%C3%8E2%91%92%AC%14%F0%A7M%0C%F9%FB%CC%5D%ED%60T%F3%A2%18%0FU%07%E7.%9F%83%9D%07r%FC%D5%22%BCC%85%B7p%7C%24%E9%B9%A8%C0%E3%EB%3A2t%9B%B4%82%CB%9A%1C%27%06%D4%08%8B%E4%9Bh%D32%BD%A1%EC%B6%5C%C4%01%85%8E; 1a5b69166387515780349607c54875af=%C1%F9%27nc%D2%A4%82',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

data = {
    'cid': '50000001',
    'timeUnit': 'date',
    'startDate': '2022-04-25',
    'endDate': '2022-05-25',
    'age': '',
    'gender': '',
    'device': '',
    'page': '1',
    'count': '20',
}

response = requests.post('https://datalab.naver.com/shoppingInsight/getCategoryKeywordRank.naver', cookies=cookies, headers=headers, data=data)

print(response.text)