import json
import requests
import most_trend_keywords_detail
import datetime

def insertDB(categoryId,rankedDate,period,demo,rank, keyword, rankedReason ,mobileLowPrice,productTitle,productCrUrl):
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
                sql = "INSERT INTO `Most_TrendKeywords` (`categoryId`,`rankedDate`,`period`,`demo`,`rank`, `keyword`, `rankedReason` ,`mobileLowPrice`,`productTitle`,`productCrUrl`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                curs.execute(sql,(
                    categoryId,
                    rankedDate,
                    period,
                    demo,
                    rank, 
                    keyword, 
                    rankedReason,
                    mobileLowPrice,
                    productTitle,
                    productCrUrl
                ))
                print("Most_PurchaseProducts insert!!!!!", rank,productTitle,categoryId)
            except Exception as ex:
                print(ex, "Most_PurchaseProducts insert!!!!!", rank,productTitle,categoryId)
        connection.commit()
    finally:
        connection.close()


def most_trend_keywords(cid,period,demo):
    json_data = {
        'query': '\n      query ChartList($params: ChartListInput) {\n        KeywordChartList(params: $params) {\n          rankedDate\n          period\n          demo\n          categoryId\n          charts {\n            rank\n            change\n            brandSeq\n            brandName\n            exposeBrandName\n            keyword\n            exposeKeyword\n            rankedReason\n          }\n        }\n      }\n    ',
        'variables': {
            'params': {
                'categoryId': cid,
                'demo': demo,
                'period': period,
                'rankStart': 1,
                'rankEnd': 20,
            },
        },
    }

    response = requests.post('https://search.shopping.naver.com/best/api/graphql', json=json_data)
    response_json = json.loads(response.text)

    rankedDate =  response_json['data']['KeywordChartList']['rankedDate']
    period =  response_json['data']['KeywordChartList']['period']
    demo =  response_json['data']['KeywordChartList']['demo']
    categoryId =  response_json['data']['KeywordChartList']['categoryId']
    charts =  response_json['data']['KeywordChartList']['charts']

    for chart in charts:
        rank = chart['rank']
        keyword = chart['keyword']
        rankedReason = chart['rankedReason']

        products = most_trend_keywords_detail.trend_keywords_detail(keyword,cid,period,demo,rankedDate)
        for product in products:
            mobileLowPrice = product['mobileLowPrice']
            productTitle = product['productTitle']
            productCrUrl = product['productCrUrl']
            
            print(rank, keyword, productTitle)
            insertDB(categoryId,rankedDate,period,demo,rank, keyword, rankedReason ,mobileLowPrice,productTitle,productCrUrl)

    return charts
    
if __name__ == "__main__":
    # cid -> ALL or 5000000 etc..
    # dept 2까지만 하기 
    cid = "50000153"

    # period -> P1D or P7D
    period = "P1D"

    ## 나이, 성별대 
    ## M01, F01 .... M05, F05, A00
    demo = "A00"
    print(most_trend_keywords(cid,period,demo))