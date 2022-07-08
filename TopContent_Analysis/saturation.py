import volumeSearch
import blogCnt
import cafeCnt
import authorization

if __name__ == "__main__" :
    keyword = "나이키"

    monthlyPcQcCnt, monthlyMobileQcCnt = volumeSearch.search_volume(keyword)
    print("monthlyPcQcCnt : ", monthlyPcQcCnt, "monthlyMobileQcCnt : ", monthlyMobileQcCnt)

    ## 블로그 포화도
    monthly_blogCnt = blogCnt.monthly_blogCnt(keyword)
    blog_sat = monthly_blogCnt / (monthlyPcQcCnt + monthlyMobileQcCnt)
    print("monthly_blogCnt : ", monthly_blogCnt)
    print("blog_sat : ", blog_sat)


    ## 카페 포화도
    monthly_cafeCnt = cafeCnt.monthly_cafeCnt(keyword)
    cafe_sat = monthly_cafeCnt / (monthlyPcQcCnt + monthlyMobileQcCnt)
    print("monthly_cafeCnt : ", monthly_cafeCnt)
    print("cafe_sat : ", cafe_sat)