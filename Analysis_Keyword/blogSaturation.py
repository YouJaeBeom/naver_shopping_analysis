import volumeSearch_M
import blogCnt
import cafeCnt
import authorization

if __name__ == "__main__" :
    keyword = "나이키"

    Authorization = authorization.authorization()
    monthlyPcQcCnt, monthlyMobileQcCnt = volumeSearch_M.search_volume(keyword,Authorization)
    print("monthlyPcQcCnt : ", monthlyPcQcCnt, "monthlyMobileQcCnt : ", monthlyMobileQcCnt)

    ## 블로그 포화도
    monthly_blogCnt = blogCnt.monthly_blogCnt(keyword)
    blog_sat = monthly_blogCnt / (monthlyPcQcCnt + monthlyMobileQcCnt)
    print("monthly_blogCnt : ", monthly_blogCnt)
    print("blog_sat : ", blog_sat)