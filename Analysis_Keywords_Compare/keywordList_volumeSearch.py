
import volumeSearch
import authorization
import getCategoryAgeRate
import getCategoryGenderRate
import datetime

if __name__ == "__main__":
    keyword_list = ["마스크","나이키"]

    for keyword in keyword_list:
        monthlyPcQcCnt, monthlyMobileQcCnt = volumeSearch.search_volume(keyword)

        total_volume = monthlyPcQcCnt + monthlyMobileQcCnt

        monthlyPcQcRat = (monthlyPcQcCnt/total_volume)*100
        monthlyMobileQcRat = (monthlyMobileQcCnt/total_volume)*100

        end = datetime.datetime.now().strftime('%Y-%m-%d')

        start = datetime.datetime.now() + datetime.timedelta(days=-31)
        start = start.strftime('%Y-%m-%d')

        agerate = getCategoryAgeRate.getagerate(start, end, keyword)
        genderrate = getCategoryGenderRate.getgenderrate(start, end, keyword)

        print("total_volume : ", total_volume, "monthlyPcQcRat : ", monthlyPcQcRat, "monthlyMobileQcRat : ",monthlyMobileQcRat, "agerate : ", agerate, "genderrate : ", genderrate)
