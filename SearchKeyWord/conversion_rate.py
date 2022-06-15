from tkinter.messagebox import NO
import requests
import json
import authorization
import click_volume
import search_volume


if __name__ == "__main__" :
    keyword="마스크"
    Authorization = authorization.authorization()

    monthlyAvePcClkCnt, monthlyAveMobileClkCnt= click_volume.click_volume(keyword,Authorization)
    print(monthlyAvePcClkCnt, monthlyAveMobileClkCnt)

    monthlyPcQcCnt, monthlyMobileQcCnt = search_volume.search_volume(keyword,Authorization)
    print(monthlyPcQcCnt, monthlyMobileQcCnt)

    CVR = (monthlyAvePcClkCnt + monthlyAveMobileClkCnt) / (monthlyPcQcCnt+monthlyMobileQcCnt)
    print("경쟁률 : %.2f"%CVR)