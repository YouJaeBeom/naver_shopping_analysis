import related_keyword_ad
import related_keyword_shopping
import related_keyword_top


if __name__ == "__main__":
    cid = "50000006"
    ## 기간 설정
    import datetime
    end = datetime.datetime.now().strftime('%Y-%m-%d')
    start = datetime.datetime.now() + datetime.timedelta(days=-31)
    start = start.strftime('%Y-%m-%d')
    
    keyword_list = ["마스크","나이키"]

    for keyword in keyword_list:

        related_keyword_ad_list = related_keyword_ad.ads_related_keywords(keyword)
        print("related_keyword_ad_list : ", related_keyword_ad_list)
        related_keyword_shopping_list = related_keyword_shopping.related_keywords(keyword)
        print("related_keyword_shopping_list :", related_keyword_shopping_list)
        related_keyword_tops_list = related_keyword_top.top_related_keywords(cid,start,end)
        print("related_keyword_tops_list : ", related_keyword_tops_list)