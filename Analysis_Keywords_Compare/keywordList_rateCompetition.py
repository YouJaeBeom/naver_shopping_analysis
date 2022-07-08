
import requests
import json
import authorization
import volumeProducts
import volumeSearch

if __name__ == "__main__" :
    keyword_list = ["마스크","나이키"]

    for keyword in keyword_list:
        total_count= volumeProducts.products_count(keyword)
        print(total_count)

        monthlyPcQcCnt, monthlyMobileQcCnt = volumeSearch.search_volume(keyword)
        print(monthlyPcQcCnt, monthlyMobileQcCnt)

        comp = total_count / (monthlyPcQcCnt+monthlyMobileQcCnt)
        print("경쟁률 : %.2f"%comp)