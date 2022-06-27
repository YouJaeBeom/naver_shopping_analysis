import cafeCnt
import blogCnt

if __name__ == "__main__":
    keyword= "마스크"
    total_cafe_Cnt = cafeCnt.total_cafeCnt(keyword)
    print("total_cafe_Cnt : ",total_cafe_Cnt)

    total_blog_Cnt = blogCnt.total_blogCnt(keyword)
    print("total_blogCnt : ",total_blog_Cnt)

    total_contentCnt = total_cafe_Cnt + total_blog_Cnt
    print("total_contentCnt : ",total_contentCnt)

    ## 카페 비율
    cafeRat = (total_cafe_Cnt/total_contentCnt)*100
    print("cafeRat : ",cafeRat)

    ## 블로그 비율 
    blogRat = (total_blog_Cnt/total_contentCnt)*100
    print("blogRat : ",blogRat)