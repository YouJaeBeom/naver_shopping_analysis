import most_viewed_products
import most_purchase_products
import most_trend_keywords
import getCategoryAgeRate, getCategoryDeviceRate, getCategoryGenderRate, getCategoryKeywordRank

import datetime

if __name__ == "__main__":
    ## 카테고리 id 설정
    cid = "50000000"
    period = "P1D"
    ## 많이 본 상품 수집 
    most_viewed_products_1d = most_viewed_products.most_viewed_products(cid,period)
    print("most_viewed_products_1d :", most_viewed_products_1d)


    ## 많이 구매한 상품 수집 
    most_purchase_products_1d = most_purchase_products.most_purchase_products(cid,period)
    print("most_purchase_products_1d :", most_purchase_products_1d)

    ## 트랜드 키워드 상품 수집 
    most_trend_keywords_1d = most_trend_keywords.most_trend_keywords(cid,period)
    print("most_trend_keywords_1d :", most_trend_keywords_1d)


    ## 기간 설정
    end = datetime.datetime.now().strftime('%Y-%m-%d')
    start = datetime.datetime.now() + datetime.timedelta(days=-31)
    start = start.strftime('%Y-%m-%d')

    ## 나이별
    agerate = getCategoryAgeRate.getagerate(cid, start, end)
    print("getCategoryAgeRate :", (agerate))

    ## 기기별 
    devicerate = getCategoryDeviceRate.getdevicerate(cid, start, end)
    print("getCategoryDeviceRate :", devicerate)

    ## 성별별
    genderrate = getCategoryGenderRate.getgenderrate(cid, start, end)
    print("getCategoryGenderRate : ", genderrate)

    ## 인기 top 500
    keywordrank = getCategoryKeywordRank.getkeywordrand(cid, start, end)
    print("getCategoryKeywordRank :", keywordrank)

