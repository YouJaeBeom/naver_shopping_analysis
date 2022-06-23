import requests
import json
from bs4 import BeautifulSoup as bs

def getrelated_tag(mallProductId): 
    response = requests.get('https://smartstore.naver.com/main/products/'+mallProductId)
    soup = bs(response.text, "html.parser")
    
    # _2RkVi-H2ze N=a:itm.tag
    # _2RkVi-H2ze N=a:itm.tag
    related_tags = soup.find_all("a",class_='_3SMi-TrYq2')

    return related_tags

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

    try :
        related_tag = getrelated_tag(mallProductId)
    except Exception as e:
        print(e)
        related_tag = None

    return store_keepCnt, qnaCnt, related_tag


if __name__ == "__main__":
    print(getrelated_tag("6176787621"))