import requests
import json
import tor
def total_count_tag(keyword):
    params = {
        '__a': '1',
        '__d': 'dis',
    }
    ## setting tor
    proxies = {
        'http': 'socks5://localhost:9050',
    }
    try:
        response = requests.get('https://www.instagram.com/explore/tags/'+keyword+'/', params=params, proxies=proxies)
    except requests.ConnectionError as ex:
        tor.renew_tor_ip(9051)
        print("ex = ", ex)
        print()
    else:
        response_json = json.loads(response.text)
        instatag_total_count = response_json['graphql']['hashtag']['edge_hashtag_to_media']['count']
        return instatag_total_count

if __name__ == "__main__":
    keyword = "댕댕이"
    instatag_total_count = total_count_tag(keyword)
    print("instatag_total_count ", instatag_total_count)