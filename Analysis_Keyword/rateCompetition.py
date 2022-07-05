import requests
import json
import authorization
import volumeProducts
import volumeSearch_M

if __name__ == "__main__" :
    keyword="마스크"
    total_count= volumeProducts.products_count(keyword)
    print("total_count :", total_count)

    
    monthlyPcQcCnt, monthlyMobileQcCnt = volumeSearch_M.search_volume(keyword)
    print("monthlyPcQcCnt : ", monthlyPcQcCnt, "monthlyMobileQcCnt : ",monthlyMobileQcCnt)

    rateCompetition = total_count / (monthlyPcQcCnt+monthlyMobileQcCnt)
    print("경쟁률 : %.2f"%rateCompetition)