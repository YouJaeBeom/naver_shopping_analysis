
from bs4 import BeautifulSoup
import requests
import json
import socket
import socks
import subprocess
from stem.control import Controller
from stem import Signal
import urllib3
import orjson
import tor


def insertDB(categoryId,rankedDate,period,demo,rank,mobileLowPrice,productTitle,mallCount,productCrUrl):
    import pymysql
    db_name = "test"
    
    connection = pymysql.connect(
        host='localhost', 
        user='rnrsqaure', 
        password='', 
        db=db_name,
        use_unicode=True, charset="utf8"
    )
    try:
        with connection.cursor() as curs:
            try: 
                sql = "INSERT INTO `Most_ViewProducts` (`categoryId`,`rankedDate`,`period`,`demo`,`rank`,`mobileLowPrice`,`productTitle`,`mallCount`,`productCrUrl`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                curs.execute(sql,(
                    categoryId,
                    rankedDate,
                    period,
                    demo,
                    rank,
                    mobileLowPrice,
                    productTitle,
                    mallCount,
                    productCrUrl
                ))
                print("Most_ViewProducts insert!!!!!", rank,productTitle,categoryId)
            except Exception as ex:
                print(ex, "Most_ViewProducts insert!!!!!", rank,productTitle,categoryId)
        connection.commit()
    finally:
        connection.close()

def most_viewed_products(cid,period,demo):

    json_data = {
        'query': '\n        query CategoryProducts(\n          $categoryId: String\n          $demo: DemoType\n          $rankType: RankType\n          $period: RankPeriod\n          $productType: ProductType\n          $productCount: Int\n          $exposeLogSourceInfo: ExposeLogSourceInfo\n        ) {\n          CategoryProducts(\n            categoryId: $categoryId\n            demo: $demo\n            rankType: $rankType\n            period: $period\n            productType: $productType\n            productCount: $productCount\n            exposeLogSourceInfo: $exposeLogSourceInfo\n          ) {\n            categoryId\n            demo\n            period\n            rankType\n            rankedDate\n            products {\n              rank\n              nvMid\n              imageUrl\n              mobileLowPrice\n              priceUnit\n              productTitle\n              productName\n              mallCount\n              mallName\n              mallProductUrl\n              mallProdMblUrl\n              isNaverPay\n              isMblNaverPay\n              nPayPcType\n              nPayMblType\n              mpTp\n              dlvryCont\n              productCrUrl\n            }\n          }\n        }\n      ',
        'variables': {
            'demo': demo,
            'rankType': 'CLICK',
            'categoryId': cid,
            'productCount': 100,
            'period': period,
            'productType': 'ALL',
            'exposeLogSourceInfo': {
                'isMobileDomain': False,
                'pageType': 'Category',
            },
        },
    }

    ## setting tor
    proxies = {
        'http': 'socks5://localhost:9050',
    }

    try: 
        #s = requests.Session()
        response = requests.post(
            'https://msearch.shopping.naver.com/best/api/graphql',  
            json = json_data,
            proxies = proxies
        )    
    except requests.ConnectionError as ex:
        tor.renew_tor_ip(9051)
        print("ex = ", ex)
        print()
    else:
        print("response.text = ", response.text)
        response_json = json.loads(response.text)
    
        categoryId = response_json['data']['CategoryProducts']['categoryId']
        rankedDate =  response_json['data']['CategoryProducts']['rankedDate']
        period = response_json['data']['CategoryProducts']['period']
        demo = response_json['data']['CategoryProducts']['demo']

        products =  response_json['data']['CategoryProducts']['products']

        for product in products:
            rank = product['rank']
            mobileLowPrice = product['mobileLowPrice']
            productTitle = product['productTitle']
            mallCount = product['mallCount']
            productCrUrl = product['productCrUrl']
            print("product :",product)
            insertDB(categoryId,rankedDate,period,demo,rank,mobileLowPrice,productTitle,mallCount,productCrUrl)

if __name__ == "__main__":
    # cid -> ALL or 5000000 etc..
    # dept 2까지만 하기 
    cid = "ALL"

    # period -> P1D or P7D
    period = "P7D"

    ## 나이, 성별대 
    ## M01, F01 .... M05, F05, A00
    demo = "A00"
    print(most_viewed_products(cid,period,demo))

