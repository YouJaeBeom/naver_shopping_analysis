
from bs4 import BeautifulSoup
import requests
import json
def most_viewed_products(cid,period):
    json_data = {
        'query': '\n        query CategoryProducts(\n          $categoryId: String\n          $demo: DemoType\n          $rankType: RankType\n          $period: RankPeriod\n          $productType: ProductType\n          $productCount: Int\n          $exposeLogSourceInfo: ExposeLogSourceInfo\n        ) {\n          CategoryProducts(\n            categoryId: $categoryId\n            demo: $demo\n            rankType: $rankType\n            period: $period\n            productType: $productType\n            productCount: $productCount\n            exposeLogSourceInfo: $exposeLogSourceInfo\n          ) {\n            categoryId\n            demo\n            period\n            rankType\n            rankedDate\n            products {\n              rank\n              nvMid\n              imageUrl\n              mobileLowPrice\n              priceUnit\n              productTitle\n              productName\n              mallCount\n              mallName\n              mallProductUrl\n              mallProdMblUrl\n              isNaverPay\n              isMblNaverPay\n              nPayPcType\n              nPayMblType\n              mpTp\n              dlvryCont\n              productCrUrl\n            }\n          }\n        }\n      ',
        'variables': {
            'demo': 'A00',
            'rankType': 'CLICK',
            'categoryId': cid,
            'productCount': 100,
            'period': period,
            'productType': cid,
            'exposeLogSourceInfo': {
                'isMobileDomain': False,
                'pageType': 'Category',
            },
        },
    }


    response = requests.post('https://search.shopping.naver.com/best/api/graphql',  json=json_data)    
    response_json = json.loads(response.text)
    products =  response_json['data']['CategoryProducts']['products']

    return products

if __name__ == "__main__":
    # cid -> ALL or 5000000 etc..
    cid = "ALL"

    # period -> P1D or P7D
    period = "P1D"
    print(most_viewed_products(cid,period))
