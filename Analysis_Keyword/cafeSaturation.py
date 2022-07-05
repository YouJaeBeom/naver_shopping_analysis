import volumeSearch_M
import blogCnt
import cafeCnt
import authorization

if __name__ == "__main__" :
    keyword = "나이키"

    Authorization = authorization.authorization()
    monthlyPcQcCnt, monthlyMobileQcCnt = volumeSearch_M.search_volume(keyword,Authorization)
    print("monthlyPcQcCnt : ", monthlyPcQcCnt, "monthlyMobileQcCnt : ", monthlyMobileQcCnt)


    ## 카페 포화도
    monthly_cafeCnt = cafeCnt.monthly_cafeCnt(keyword)
    cafe_sat = monthly_cafeCnt / (monthlyPcQcCnt + monthlyMobileQcCnt)
    print("monthly_cafeCnt : ", monthly_cafeCnt)
    print("cafe_sat : ", cafe_sat)