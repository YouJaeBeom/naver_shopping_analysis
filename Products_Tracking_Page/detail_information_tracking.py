import requests
import json
from bs4 import BeautifulSoup as bs
import tor

def getQnA(mallProductId):
    ## setting tor
    proxies = {
        'http': 'socks5://localhost:9050',
    }
    try:
        response = requests.get('https://smartstore.naver.com/i/v1/comments/PRODUCTINQUIRY/'+mallProductId, proxies=proxies)
        response_json = json.loads(response.text)
    except :
        tor.renew_tor_ip(9051)
        print("ex = ", ex)
        print()
    else:
        qnaCnt =  response_json['totalElements']

        return qnaCnt 

def getstore_keepCnt(mallProductId):
    ## setting tor
    proxies = {
        'http': 'socks5://localhost:9050',
    }

    try:
        response = requests.get('https://smartstore.naver.com/main/products/'+mallProductId, proxies=proxies)
        soup = bs(response.text, "html.parser")
    except :
        tor.renew_tor_ip(9051)
        print("ex = ", ex)
        print()
    else:
        store_keepCnt = soup.find("span", class_ = 'number').text
        return store_keepCnt

def getinfo(mallProductId):
    try:
        store_keepCnt = getstore_keepCnt(mallProductId)
    except Exception as e:
        print(e)
        store_keepCnt = None

    try:
        qnaCnt = getQnA(mallProductId)
    except Exception as e:
        print(e)
        qnaCnt = None

    return store_keepCnt, qnaCnt

if __name__ == "__main__":
    print(getQnA("6176787621"))
    print(getinfo("6176787621"))