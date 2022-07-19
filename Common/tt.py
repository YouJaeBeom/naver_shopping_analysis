import requests
from stem.control import Controller
from stem import Signal

def renew_tor_ip(port_num):
    with Controller.from_port(port = port_num) as controller:
        controller.authenticate(password="mnet")
        controller.signal(Signal.NEWNYM)
## setting tor
proxies = {
    'http': 'socks5://localhost:9050',
}

cookies = {
    'autocomplete': 'use',
    'NNB': 'DULXWITNGSGGE',
    'AD_SHP_BID': '14',
    'ASID': 'dc957c49000001810000e7bc00000053',
    '_ga_7VKFYR6RV1': 'GS1.1.1655549940.3.0.1655549940.60',
    '_ga': 'GA1.2.678320805.1655285848',
    'NFS': '2',
    'MM_NEW': '1',
    'SHP_BID': '6',
    'nx_ssl': '2',
    'sus_val': 'Py7yXiuxaXx/29ZBt0JCZl7N',
    'spage_uid': '',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:102.0) Gecko/20100101 Firefox/102.0',
}

params = {
    'sort': 'rel',
    'pagingIndex': '2',
    'pagingSize': '40',
    'viewType': 'list',
    'productSet': 'total',
    'deliveryFee': '',
    'deliveryTypeValue': '',
    'frm': 'NVSHATC',
    'query': '마스크',
    'origQuery': '마스크',
    'iq': '',
    'eq': '',
    'xq': '',
}

response = requests.get('https://search.shopping.naver.com/api/search/all', params=params,  headers=headers, proxies=proxies)

print(response.text)

renew_tor_ip(9051)
print(requests.get('http://icanhazip.com/', timeout=24, proxies = proxies).text) # outputs proxy IP