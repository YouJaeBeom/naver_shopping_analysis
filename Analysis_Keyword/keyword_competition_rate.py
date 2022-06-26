from tkinter.messagebox import NO
import requests
import json
import authorization
import products_count
import search_volume_M

if __name__ == "__main__" :
    keyword="마스크"
    total_count= products_count.products_count(keyword)
    print(total_count)

    Authorization = authorization.authorization()
    monthlyPcQcCnt, monthlyMobileQcCnt = search_volume_M.search_volume(keyword, Authorization)
    print(monthlyPcQcCnt, monthlyMobileQcCnt)

    comp = total_count / (monthlyPcQcCnt+monthlyMobileQcCnt)
    print("경쟁률 : %.2f"%comp)