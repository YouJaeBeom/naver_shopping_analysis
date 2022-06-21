import requests
import json

def total_count_tag(keyword):
    
    cookies = {
        'mid': 'YqahPwAEAAGWZVF_6aUHmQU7JjXR',
        'ig_did': '1578BA99-4383-4CB4-86BC-6AE4612E7DB7',
        'ig_nrcb': '1',
        'datr': 'wKGmYsLCb6d9s-HJjO-N0tCV',
        'shbid': '"14581\\05421904400673\\0541687347005:01f74bc2effad7623c3ba961c7bec763a967388632c13d068395101da5e16607c74b7107"',
        'shbts': '"1655811005\\05421904400673\\0541687347005:01f7e143f735536381c6093f536aac28d62c8228b5191c4277194a7fe29f6a1cf028aced"',
        'rur': '"VLL\\05421904400673\\0541687347447:01f777b23a55eedadc0b3fe06e32b868b34865396185a2cf2e5da8b6081d6015e62a92b4"',
        'csrftoken': 'ZKAhKb9uxnnjhEbBOlE2p3mFQ9SOCSXb',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Accept': '*/*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'X-CSRFToken': 'ZKAhKb9uxnnjhEbBOlE2p3mFQ9SOCSXb',
        'X-IG-App-ID': '936619743392459',
        'X-ASBD-ID': '198387',
        'X-IG-WWW-Claim': 'hmac.AR2SK8CwEbEnW0JrEC5CPRkvxFPJcpfBw-s-RWIpx-CT0S2Q',
        'X-Requested-With': 'XMLHttpRequest',
        'Alt-Used': 'www.instagram.com',
        'Connection': 'keep-alive',
        'Referer': 'https://www.instagram.com/explore/tags/%EB%8C%95%EB%8C%95%EC%9D%B4/',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'mid=YqahPwAEAAGWZVF_6aUHmQU7JjXR; ig_did=1578BA99-4383-4CB4-86BC-6AE4612E7DB7; ig_nrcb=1; datr=wKGmYsLCb6d9s-HJjO-N0tCV; shbid="14581\\05421904400673\\0541687347005:01f74bc2effad7623c3ba961c7bec763a967388632c13d068395101da5e16607c74b7107"; shbts="1655811005\\05421904400673\\0541687347005:01f7e143f735536381c6093f536aac28d62c8228b5191c4277194a7fe29f6a1cf028aced"; rur="VLL\\05421904400673\\0541687347447:01f777b23a55eedadc0b3fe06e32b868b34865396185a2cf2e5da8b6081d6015e62a92b4"; csrftoken=ZKAhKb9uxnnjhEbBOlE2p3mFQ9SOCSXb',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        '__a': '1',
        '__d': 'dis',
    }

    response = requests.get('https://www.instagram.com/explore/tags/'+keyword+'/', params=params, cookies=cookies, headers=headers)
    response_json = json.loads(response.text)
    instatag_total_count = response_json['graphql']['hashtag']['edge_hashtag_to_media']['count']
    print(instatag_total_count)

if __name__ == "__main__":
    keyword = "댕댕이"
    total_count_tag(keyword)