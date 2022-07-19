from datetime import datetime
import requests
import json
import detail_information_tracking
from bs4 import BeautifulSoup as bs
import multiprocessing.pool
from itertools import repeat
import tor

def insertDB_P(rank, productName, product_id, price, reviewCount, purchaseCnt, keepCnt, score, store_keepCnt,  qnaCnt):
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
                sql = "INSERT INTO `product_rank_tracking_PC` (`rank`, `productName`, `product_id`, `price`, `reviewCount`, `purchaseCnt`, `keepCnt`, `score`, `store_keepCnt`,  `qnaCnt`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                curs.execute(sql,(
                    rank,
                    productName,
                    str(product_id),
                    price,
                    reviewCount,
                    purchaseCnt,
                    keepCnt,
                    str(score),
                    store_keepCnt,
                    qnaCnt
                ))
                print("product_rank_tracking_PC insert!!!!!", rank, productName, product_id, price, reviewCount, purchaseCnt, keepCnt, score, store_keepCnt,  qnaCnt)
            except Exception as ex:
                print(ex, "product_rank_tracking_PC insert!!!!!", rank, productName, product_id, price, reviewCount, purchaseCnt, keepCnt, score, store_keepCnt,  qnaCnt)
        connection.commit()
    finally:
        connection.close()

def insertDB_M(rank, productName, product_id, price, reviewCount, purchaseCnt, keepCnt, score, store_keepCnt,  qnaCnt):
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
                sql = "INSERT INTO `product_rank_tracking_MOB` (`rank`, `productName`, `product_id`, `price`, `reviewCount`, `purchaseCnt`, `keepCnt`, `score`, `store_keepCnt`,  `qnaCnt`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                curs.execute(sql,(
                    rank,
                    productName,
                    str(product_id),
                    price,
                    reviewCount,
                    purchaseCnt,
                    keepCnt,
                    str(score),
                    store_keepCnt,
                    qnaCnt
                ))
                print("product_rank_tracking_MOB insert!!!!!", rank, productName, product_id, price, reviewCount, purchaseCnt, keepCnt, score, store_keepCnt,  qnaCnt)
            except Exception as ex:
                print(ex, "product_rank_tracking_MOB insert!!!!!", rank, productName, product_id, price, reviewCount, purchaseCnt, keepCnt, score, store_keepCnt,  qnaCnt)
        connection.commit()
    finally:
        connection.close()

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

    ## setting tor
    proxies = {
        'http': 'socks5://localhost:9050',
    }

    try:
        response = requests.get('https://search.shopping.naver.com/api/search/all', params=params, proxies=proxies)
    except requests.ConnectionError as ex:
        tor.renew_tor_ip(9051)
        print("ex = ", ex)
        print()
    else:
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

            insertDB_P(rank, productName, product_id, price, reviewCount, purchaseCnt, keepCnt, score, store_keepCnt,  qnaCnt)
            #print( "{} rank = {} productName = {} price= {} reviewCount= {} purchaseCnt= {} keepCnt= {} store_keepCnt= {} score= {} qnaCnt= {} ".format(pagingIndex, rank, productName, price, reviewCount, purchaseCnt, keepCnt, store_keepCnt, score, qnaCnt))

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

    ## setting tor
    proxies = {
        'http': 'socks5://localhost:9050',
    }

    try:
        response = requests.get('https://msearch.shopping.naver.com/api/search/all', params=params, headers=headers, proxies=proxies)
    except requests.ConnectionError as ex:
        tor.renew_tor_ip(9051)
        print("ex = ", ex)
        print()
    else:
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
            
            insertDB_M(rank, productName, product_id, price, reviewCount, purchaseCnt, keepCnt, score, store_keepCnt,  qnaCnt)
            #print( "{} rank = {} productName = {} price= {} reviewCount= {} purchaseCnt= {} keepCnt= {} store_keepCnt= {} score= {} qnaCnt= {} ".format(mallProductId, rank, productName, price, reviewCount, purchaseCnt, keepCnt, store_keepCnt, score, qnaCnt))

if __name__ == "__main__":
    starttime = datetime.now()
    keyword = "마스크"
    #(ranking_tracking_PC("마스크"))
    
    pageCnt = 50
    pageCnt_list = []
    for index in range(1,pageCnt):
        pageCnt_list.append(index)

    process_pool = multiprocessing.Pool(processes = pageCnt)
    process_pool.starmap(ranking_tracking_MOB, zip(repeat(keyword), pageCnt_list))
    process_pool.close()
    process_pool.join()

    endtime = datetime.now()
    print("time : ", endtime-starttime)