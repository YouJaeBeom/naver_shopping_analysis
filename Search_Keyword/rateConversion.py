
import requests
import json
import authorization
import volumeClick
import volumeSearch


if __name__ == "__main__" :
    keyword="마스크"

    monthlyAvePcClkCnt, monthlyAveMobileClkCnt= volumeClick.click_volume(keyword)
    print(monthlyAvePcClkCnt, monthlyAveMobileClkCnt)

    monthlyPcQcCnt, monthlyMobileQcCnt = volumeSearch.search_volume(keyword)
    print(monthlyPcQcCnt, monthlyMobileQcCnt)

    rateConversion = (monthlyAvePcClkCnt + monthlyAveMobileClkCnt) / (monthlyPcQcCnt+monthlyMobileQcCnt)
    print("경쟁률 : %.2f"%rateConversion)