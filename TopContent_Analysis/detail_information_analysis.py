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
    except :
        tor.renew_tor_ip(9051)
        print("ex = ", ex)
        print()
    else:
        response_json = json.loads(response.text)
        qnaCnt =  response_json['totalElements']

        return qnaCnt 

def getStoreKeepCnt(mallProductId):
    ## setting tor
    proxies = {
        'http': 'socks5://localhost:9050',
    }
    try:
        response = requests.get('https://smartstore.naver.com/main/products/'+mallProductId, proxies=proxies)
    except :
        tor.renew_tor_ip(9051)
        print("ex = ", ex)
        print()
    else:
        soup = bs(response.text, "html.parser")

        store_keepCnt = soup.find("span", class_ = 'number').text

        return store_keepCnt 

def getinfo(mallProductId):
    try:
        store_keepCnt = getStoreKeepCnt(mallProductId)
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
    print(getrelated_tag("6176787621"))