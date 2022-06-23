from datetime import datetime
import requests
import json
import detail_information_tracking
from bs4 import BeautifulSoup as bs

def ranking_tracking_PC(keyword):
    for pagingIndex in range(1,51):
        params = {
            'sort': 'rel',
            'pagingIndex': str(pagingIndex),
            'pagingSize': '80',
            'viewType': 'list',
            'productSet': 'checkout',
            'frm': 'NVSHCHK',
            'query': keyword,
            'origQuery': keyword,
        }

        response = requests.get('https://search.shopping.naver.com/api/search/all', params=params)
        response_json = json.loads(response.text)
        data_list =  response_json['shoppingResult']['products']

        for data in data_list:
            product_id = data['id']
            rank = data['rank']
            imageUrl = data['imageUrl']
            productName = data['productName']
            price = data['price']
            reviewCount = data['reviewCount']
            purchaseCnt = data['purchaseCnt']
            keepCnt = data['keepCnt']
            score = data['scoreInfo']

            mallProductId = data['mallProductId']
            if mallProductId != "":
                store_keepCnt, qnaCnt = detail_information_tracking.getinfo(mallProductId)
            else :
                store_keepCnt, qnaCnt = None, None

            print( "{} rank = {} productName = {} price= {} reviewCount= {} purchaseCnt= {} keepCnt= {} store_keepCnt= {} score= {} qnaCnt= {} ".format(pagingIndex, rank, productName, price, reviewCount, purchaseCnt, keepCnt, store_keepCnt, score, qnaCnt))

def ranking_tracking_MOB(keyword):
    for pagingIndex in range(1,51):
        headers = {
            'Referer': 'https://msearch.shopping.naver.com/search/all?query={}&frm=NVSHSRC&prevQuery={}'.format(keyword,keyword).encode('utf-8').decode('iso-8859-1'),
        }

        params = {
            'query': keyword,
            'sort': 'rel',
            'pagingIndex': str(pagingIndex),
            'pagingSize': '80',
            'viewType': 'lst',
            'productSet': 'total',
            'frm': 'NVSHPAG',
            'origQuery': keyword,
        }
        
        response = requests.get('https://msearch.shopping.naver.com/api/search/all', params=params, headers=headers)
        response_json = json.loads(response.text)
        data_list =  response_json['shoppingResult']['products']

        for data in data_list:
            product_id = data['id']
            rank = data['rank']
            imageUrl = data['imageUrl']
            productName = data['productName']
            price = data['price']
            reviewCount = data['reviewCount']
            purchaseCnt = data['purchaseCnt']
            keepCnt = data['keepCnt']
            score = data['scoreInfo']
            
            mallProductId = data['mallProductId']
            if mallProductId != "":
                store_keepCnt, qnaCnt = detail_information_tracking.getinfo(mallProductId)
            else :
                store_keepCnt, qnaCnt = None, None
            print( "{} rank = {} productName = {} price= {} reviewCount= {} purchaseCnt= {} keepCnt= {} store_keepCnt= {} score= {} qnaCnt= {} ".format(mallProductId, rank, productName, price, reviewCount, purchaseCnt, keepCnt, store_keepCnt, score, qnaCnt))

if __name__ == "__main__":
    starttime = datetime.now()
    (ranking_tracking_PC("마스크"))
    endtime = datetime.now()
    print("time : ", endtime-starttime)
