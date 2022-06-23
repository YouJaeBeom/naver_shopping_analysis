import requests
import json
from bs4 import BeautifulSoup as bs


def getQnA(mallProductId):
    response = requests.get('https://smartstore.naver.com/i/v1/comments/PRODUCTINQUIRY/'+mallProductId)
    response_json = json.loads(response.text)
    qnaCnt =  response_json['totalElements']

    return qnaCnt 

def getinfo(mallProductId):
    response = requests.get('https://smartstore.naver.com/main/products/'+mallProductId)
    soup = bs(response.text, "html.parser")

    try:
        store_keepCnt = soup.find("span", class_ = 'number').text
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