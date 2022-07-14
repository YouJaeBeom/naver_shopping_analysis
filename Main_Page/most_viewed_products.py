
from bs4 import BeautifulSoup
import requests
import json


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
        'spage_uid': '',
        'sus_val': 'dhgXMjZuGsdxOR64oZZfo0jI',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': '*/*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://search.shopping.naver.com/best/category/click?categoryCategoryId=ALL&categoryChildCategoryId=&categoryDemo=A00&categoryMidCategoryId=&categoryRootCategoryId=ALL&chartRank=1&period=P7D',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'Origin': 'https://search.shopping.naver.com',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'autocomplete=use; NNB=DULXWITNGSGGE; AD_SHP_BID=14; ASID=dc957c49000001810000e7bc00000053; _ga_7VKFYR6RV1=GS1.1.1655549940.3.0.1655549940.60; _ga=GA1.2.678320805.1655285848; NFS=2; MM_NEW=1; SHP_BID=6; nx_ssl=2; sus_val=4RrYIFCgGHJeZHfxWxVcSdLM; spage_uid=',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }
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
        'http': 'socks5h://localhost:9050',
    }

    print(requests.get("http://httpbin.org/ip",proxies = proxies).text)
    try: 
        #s = requests.Session()
        response = requests.post(
            'https://search.shopping.naver.com/best/api/graphql',  
            cookies=cookies, headers=headers,
            json = json_data,
            proxies=proxies
        )    
        print("response.text = ", response.text)
        response_json = json.loads(response.text)
    except Exception as ex:
        print("ex = ", ex)
        print()
    

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

