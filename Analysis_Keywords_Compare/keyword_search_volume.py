
import search_volume
import authorization
import getCategoryAgeRate
import getCategoryGenderRate
import datetime

if __name__ == "__main__":
    keyword = "마스크"
    Authorization = authorization.authorization()
    monthlyPcQcCnt, monthlyMobileQcCnt = search_volume.search_volume(keyword, Authorization)

    total_volume = monthlyPcQcCnt + monthlyMobileQcCnt

    monthlyPcQcRat = (monthlyPcQcCnt/total_volume)*100
    monthlyMobileQcRat = (monthlyMobileQcCnt/total_volume)*100

    end = datetime.datetime.now().strftime('%Y-%m-%d')

    start = datetime.datetime.now() + datetime.timedelta(days=-31)
    start = start.strftime('%Y-%m-%d')

    agerate = getCategoryAgeRate.getagerate(start, end, keyword)
    genderrate = getCategoryGenderRate.getgenderrate(start, end, keyword)

    print("total_volume : ", total_volume, "monthlyPcQcRat : ", monthlyPcQcRat, "monthlyMobileQcRat : ",monthlyMobileQcRat, "agerate : ", agerate, "genderrate : ", genderrate)
