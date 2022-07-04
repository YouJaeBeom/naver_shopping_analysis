from datetime import datetime
import requests
import json
import detail_information_tracking
from bs4 import BeautifulSoup as bs
import multiprocessing.pool
from itertools import repeat

def ranking_tracking_PC(keyword, pagingIndex):
    #for pagingIndex in range(1,51):
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

def ranking_tracking_MOB(keyword, pagingIndex):
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
    keyword = "마스크"
    #(ranking_tracking_PC("마스크"))
    
    
    pageCnt = 50
    pageCnt_list = []
    for index in range(1,pageCnt):
        pageCnt_list.append(index)

    process_pool = multiprocessing.Pool(processes = pageCnt)
    process_pool.starmap(ranking_tracking_PC, zip(repeat(keyword), pageCnt_list))
    process_pool.close()
    process_pool.join()

    endtime = datetime.now()
    print("time : ", endtime-starttime)
