
import volumeSearch_D
import authorization
import getCategoryAgeRate
import getCategoryGenderRate
import datetime

if __name__ == "__main__":
    keyword_list = ["마스크","나이키"]
    ## 기간 설정
    import datetime
    end = datetime.datetime.now().strftime('%Y-%m-%d')
    start = datetime.datetime.now() + datetime.timedelta(days=-31)
    start = start.strftime('%Y-%m-%d')

    ## 카테고리 id 설정
    cid = "50000000"
    
    ## device 별
    device = "pc,mo"

    ## Gener 
    gender = "f,m" 

    ## 나이별 "10,20,30,40,50,60"
    age = "20,30,40"

    for keyword in keyword_list:
        search_volume = volumeSearch_D.search_volume(cid, start, end, device, gender, age, keyword)

        print(keyword, "total_volume : ", search_volume)
