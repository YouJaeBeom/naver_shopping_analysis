import requests
import json
import pymysql

db_name = "test"

def getCategoryID(cid,dept):
    cookies = {
        'NNB': 'DULXWITNGSGGE',
        'ASID': 'dc957c49000001810000e7bc00000053',
        '_datalab_cid': '50000000',
        '_ga_7VKFYR6RV1': 'GS1.1.1655549940.3.0.1655549940.60',
        '_ga': 'GA1.2.678320805.1655285848',
        'NFS': '2',
        'MM_NEW': '1',
        'nx_ssl': '2',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': '*/*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://datalab.naver.com/shoppingInsight/sCategory.naver',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'NNB=DULXWITNGSGGE; ASID=dc957c49000001810000e7bc00000053; _datalab_cid=50000000; _ga_7VKFYR6RV1=GS1.1.1655549940.3.0.1655549940.60; _ga=GA1.2.678320805.1655285848; NFS=2; MM_NEW=1; nx_ssl=2',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        'cid': cid , 
    }

    response = requests.get('https://datalab.naver.com/shoppingInsight/getCategory.naver', params=params, cookies=cookies, headers=headers)

    response_json = json.loads(response.text)
    ranks =  response_json['childList']
    dept = dept + 1
    tab = "\t" * dept
    for rank_2dept in ranks:
        cid = rank_2dept['cid']
        name = rank_2dept['name']
        connection = pymysql.connect(
            host='localhost', 
            user='rnrsqaure', 
            password='', 
            db=db_name,
            use_unicode=True, charset="utf8"
        )
        try:
            with connection.cursor() as curs:
                try: 
                    sql = "INSERT INTO `CategoryID` (`cid`,`name`,`dept`) VALUES (%s,%s,%s)"
                    curs.execute(sql,(
                        int(cid),
                        name,
                        dept
                    ))
                    print(tab,"CategoryID insert!!!!!", name,cid,dept)
                except Exception as ex:
                    print(tab,"XXXX CategoryID insert!!!!!", name,cid,dept, ex)
            connection.commit()
        finally:
            connection.close()
        ranks = getCategoryID(cid,dept)



if __name__ == "__main__":
    dept = 1 
    cidList = {
        "패션의류" : '50000000', # 패션의루
        "패션잡화" : '50000001', # 패션잡화 
        "화장품/미용" : '50000002', # 화장품/미용
        "디지털/가전" : '50000003', # 디지털/가전
        "가구/인테러이" : '50000004', # 가구/인테러이
        "출산/육아" : '50000005', # 출산/육아
        "식품" : '50000006', # 식품
        "스포츠/레저" : '50000007', # 스포츠/레저
        "생활/건강" : '50000008', # 생활/건강
        "여가/생활편의" : '50000009', # 여가/생활편의
        "면세점" : '50000010', # 면세점
        "도서 " : '50005542', # 도서   
    }
    for name, cid in cidList.items():
        connection = pymysql.connect(
            host='localhost', 
            user='rnrsqaure', 
            password='', 
            db=db_name,
            use_unicode=True, charset="utf8"
        )
        try:
            with connection.cursor() as curs:
                try: 
                    sql = "INSERT INTO `CategoryID` (`cid`,`name`,`dept`) VALUES (%s,%s,%s)"
                    curs.execute(sql,(
                        int(cid),
                        name,
                        dept
                    ))
                    print("CategoryID insert!!!!!", name,cid,dept)
                except Exception as ex:
                    print(ex, "XXXX CategoryID insert!!!!!", name,cid,dept)
            connection.commit()
        finally:
            connection.close()
        ranks = getCategoryID(cid,dept)
        
