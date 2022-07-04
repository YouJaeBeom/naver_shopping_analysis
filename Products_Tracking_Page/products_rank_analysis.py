#from tkinter.messagebox import NO
import requests
import json
import detail_information_analysis
from bs4 import BeautifulSoup as bs
from datetime import datetime
import multiprocessing.pool
from itertools import repeat

def ranking_analysis_PC(keyword, pagingIndex):
    params = {
        'sort': 'rel',
        'pagingIndex': pagingIndex,
        'pagingSize': '80',
        'viewType': 'list',
        'productSet': 'total',
        'frm': 'NVSHTTL',
        'query': keyword,
        'origQuery': keyword,
    }

    response = requests.get('https://search.shopping.naver.com/api/search/all', params=params)
    response_json = json.loads(response.text)
    data_list =  response_json['shoppingResult']['products']

    for data in data_list:
        rank = data['rank']
        imageUrl = data['imageUrl']
        productName = data['productName']

        ## category_n_id 
        category1Id = data['category1Id']
        category2Id = data['category2Id']
        category3Id = data['category3Id']
        category4Id = data['category4Id']

        ## category_n_name 
        category1Name = data['category1Name']
        category2Name = data['category2Name']
        category3Name = data['category3Name']
        category4Name = data['category4Name']

        mallName = data['mallName']
        try:
            mallGrade = data['mallInfoCache']['mallGrade']
        except:
            mallGrade = None
        price = data['price']
        reviewCount = data['reviewCount']
        purchaseCnt = data['purchaseCnt']
        keepCnt = data['keepCnt']
        openDate = data['openDate']
        score = data['scoreInfo']

        mallProductId = data['mallProductId']
        if mallProductId != "":
            store_keepCnt, qnaCnt, related_tag= detail_information_analysis.getinfo(mallProductId)
        else :
            store_keepCnt, qnaCnt, related_tag = None, None, None
        print( "{} rank = {} productName = {} price= {} reviewCount= {} purchaseCnt= {} keepCnt= {} store_keepCnt= {} score= {} qnaCnt= {} ".format(pagingIndex, rank, productName, price, reviewCount, purchaseCnt, keepCnt, store_keepCnt, score, qnaCnt))
        #print("related_tag : ",related_tag)

if __name__ == "__main__":
    starttime = datetime.now()
    keyword = "마스크"

    pageCnt = 50
    pageCnt_list = []
    for index in range(1,pageCnt):
        pageCnt_list.append(index)

    process_pool = multiprocessing.Pool(processes = pageCnt)
    process_pool.starmap(ranking_analysis_PC, zip(repeat(keyword), pageCnt_list))
    process_pool.close()
    process_pool.join()

    endtime = datetime.now()
    print("time : ", endtime-starttime)