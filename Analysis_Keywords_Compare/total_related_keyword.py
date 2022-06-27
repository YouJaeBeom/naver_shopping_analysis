import top_related_keywords
import ads_related_keywords
import related_keywords


if __name__ == "__main__":
    cid = None
    startDate = None
    endDate = None
    page = None
    
    keyword_list = ["마스크","나이키"]

    for keyword in keyword_list:

        ads_related_keywords_list = ads_related_keywords.ads_related_keywords(keyword)
        print("ads_related_keywords_list : ", ads_related_keywords_list)
        related_keywords_list = related_keywords.related_keywords(keyword)
        print("related_keywords_list :", related_keywords_list)
        top_related_keywords_list = top_related_keywords.top_related_keywords(cid,startDate,endDate,page)
        print("top_related_keywords_list : ", top_related_keywords_list)