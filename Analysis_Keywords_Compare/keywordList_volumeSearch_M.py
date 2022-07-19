
import volumeSearch_M
import authorization
import getCategoryAgeRate
import getCategoryGenderRate
import datetime

if __name__ == "__main__":
    keyword_list = ["마스크","나이키"]

    for keyword in keyword_list:
        monthlyPcQcCnt, monthlyMobileQcCnt = volumeSearch_M.search_volume(keyword)

        total_volume = monthlyPcQcCnt + monthlyMobileQcCnt

        monthlyPcQcRat = (monthlyPcQcCnt/total_volume)*100
        monthlyMobileQcRat = (monthlyMobileQcCnt/total_volume)*100


        print(keyword, "total_volume : ", total_volume, "monthlyPcQcRat : ", monthlyPcQcRat, "monthlyMobileQcRat : ",monthlyMobileQcRat)
