import topk_products_avg_price
import topk_products_avg_purCnt

if __name__ == "__main__" :
    keyword="애플워치"
    top_10 = topk_products_avg_price.avg_products_price(keyword,10,1)
    top_10_avg_price = sum(top_10)/len(top_10)
    print("sum(top_10) :", sum(top_10), "len(top_10 : ", len(top_10) , "avg_price : ", top_10_avg_price )

    top_40 = topk_products_avg_price.avg_products_price(keyword,40,1)
    top_40_avg_price = sum(top_40)/len(top_40)
    print("sum(top_40) :", sum(top_10), "len(top_40 : ", len(top_40) , "avg_price : ", top_40_avg_price )

    keyword="애플워치"
    top_10 = topk_products_avg_purCnt.avg_products_purchaseCnt(keyword,10,1)
    top_10_avg_purchaseCnt = sum(top_10)/len(top_10)
    print("sum(top_10) :", sum(top_10), "len(top_10 : ", len(top_10) , "top_10_avg_purchaseCnt : ", top_10_avg_purchaseCnt )

    top_40 = topk_products_avg_purCnt.avg_products_purchaseCnt(keyword,40,1)
    top_40_avg_purchaseCnt = sum(top_40)/len(top_40)
    print("sum(top_40) :", sum(top_10), "len(top_40 : ", len(top_40) , "top_40_avg_purchaseCnt : ", top_40_avg_purchaseCnt )



    top_10_predict = top_10_avg_price * top_10_avg_purchaseCnt
    print( "top_10_predict : ", top_10_predict )

    top_40_predict = top_40_avg_price * top_40_avg_purchaseCnt
    print("top_40_predict : ", top_40_predict )