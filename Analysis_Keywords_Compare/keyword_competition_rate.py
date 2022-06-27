from tkinter.messagebox import NO
import requests
import json
import authorization
import products_count
import search_volume

if __name__ == "__main__" :
    keyword_list = ["마스크","나이키"]

    for keyword in keyword_list:
        total_count= products_count.products_count(keyword)
        print(total_count)

        Authorization = authorization.authorization()
        monthlyPcQcCnt, monthlyMobileQcCnt = search_volume.search_volume(keyword, Authorization)
        print(monthlyPcQcCnt, monthlyMobileQcCnt)

        comp = total_count / (monthlyPcQcCnt+monthlyMobileQcCnt)
        print("경쟁률 : %.2f"%comp)