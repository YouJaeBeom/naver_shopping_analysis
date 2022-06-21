import json
import requests
import datetime
import time
def getkeywordrand(cid, start, end):
    ranks_list = []
    for page in range(1,26):
        time.sleep(0.1)
        cookies = {
            'NNB': 'DULXWITNGSGGE',
            'nx_ssl': '2',
            'ASID': 'dc957c49000001810000e7bc00000053',
            '_datalab_cid': '50000006',
            'nid_inf': '1631157862',
            'NID_AUT': 'mNO+8XvZHGi+wDfIukaykGursjHL4QHNPkYFKsLDhOgh7+QGMmKkFlp7pQmQzsVL',
            'NID_SES': 'AAABhLdXL1fKA/9pYNDfR8PSP8E1sccNAlS98jb+O1/CXzs1uhXIEX8/N9nZYRCNx//zfPi72op3lwYcy+fv2DsXnd6kHPO4BTp9f8apoA4DZbQlqhhh5EJmNWQPanBeQw7UyoiQ3ux5D6A5T6lLPhD6RZ38V+OhwS9sb0K35Du7yUNdVSoFfrEmGV+M/G/lOl+QulWQMxxjcj3bZ1zMK8xRpUqxqIsmJzGr7AFWezSujNZ9MKK5Zhr3gwL4Iidm4+xZVt1AxTpbaGZM+SIFTyEu3RYr9zFdtatjrp7xM1LjV5tr9kBC+j3UtsHDFYekbFN1pqWvONM2LLnnwRiHa9NoNidBc1UZtH5Y9zfpmuUEx8N6k0Nv2Pe7yauvOKheX7Px2XqDHf9zwuDoaciBB8OhrL16t5TlS4hWZ53tbeDoyb0inBjiWAaTvf5Ut7xbiOkW2Jmw+MdfNcMiGQejMz+hSaQOhtMK0Vdisw0k5SMuWTurawJ/bNPiA92sMKXq2/zxT5pKF9h5x81WqjnmaKjSphg=',
            'NID_JKL': 'LJInBtlDv57Cw5ymKhME3AL6TFoX0rDIhlHPSnitVvQ=',
            'page_uid': 'hqkrGwp0Jy0sscEdtK4ssssst5Z-188792',
            '_naver_usersession_': 'pkqx/d/G/pIpo3hbptWHxA==',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
            'Accept': '*/*',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://datalab.naver.com/shoppingInsight/sCategory.naver',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://datalab.naver.com',
            'Connection': 'keep-alive',
            # Requests sorts cookies= alphabetically
            # 'Cookie': 'NNB=DULXWITNGSGGE; nx_ssl=2; ASID=dc957c49000001810000e7bc00000053; _datalab_cid=50000006; nid_inf=1631157862; NID_AUT=mNO+8XvZHGi+wDfIukaykGursjHL4QHNPkYFKsLDhOgh7+QGMmKkFlp7pQmQzsVL; NID_SES=AAABhLdXL1fKA/9pYNDfR8PSP8E1sccNAlS98jb+O1/CXzs1uhXIEX8/N9nZYRCNx//zfPi72op3lwYcy+fv2DsXnd6kHPO4BTp9f8apoA4DZbQlqhhh5EJmNWQPanBeQw7UyoiQ3ux5D6A5T6lLPhD6RZ38V+OhwS9sb0K35Du7yUNdVSoFfrEmGV+M/G/lOl+QulWQMxxjcj3bZ1zMK8xRpUqxqIsmJzGr7AFWezSujNZ9MKK5Zhr3gwL4Iidm4+xZVt1AxTpbaGZM+SIFTyEu3RYr9zFdtatjrp7xM1LjV5tr9kBC+j3UtsHDFYekbFN1pqWvONM2LLnnwRiHa9NoNidBc1UZtH5Y9zfpmuUEx8N6k0Nv2Pe7yauvOKheX7Px2XqDHf9zwuDoaciBB8OhrL16t5TlS4hWZ53tbeDoyb0inBjiWAaTvf5Ut7xbiOkW2Jmw+MdfNcMiGQejMz+hSaQOhtMK0Vdisw0k5SMuWTurawJ/bNPiA92sMKXq2/zxT5pKF9h5x81WqjnmaKjSphg=; NID_JKL=LJInBtlDv57Cw5ymKhME3AL6TFoX0rDIhlHPSnitVvQ=; page_uid=hqkrGwp0Jy0sscEdtK4ssssst5Z-188792; _naver_usersession_=pkqx/d/G/pIpo3hbptWHxA==',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }

        data = {
            'cid': cid,
            'timeUnit': 'date',
            'startDate': start,
            'endDate': end,
            'age': '',
            'gender': '',
            'device': '',
            'page': str(page),
            'count': '50',
        }

        response = requests.post('https://datalab.naver.com/shoppingInsight/getCategoryKeywordRank.naver', cookies=cookies, headers=headers, data=data)
        print(response.text)
        response_json = json.loads(response.text)
        ranks =  response_json['ranks']
        for rank in ranks:
            ranks_list.append(rank)

    return ranks_list

if __name__ == "__main__":
    ## 기간 설정
    end = datetime.datetime.now().strftime('%Y-%m-%d')
    start = datetime.datetime.now() + datetime.timedelta(days=-31)
    start = start.strftime('%Y-%m-%d')

    ## 카테고리 id 설정
    cid = "50000006"
    ranks_list = getkeywordrand(cid, start, end)
    print("ranks_list : ", ranks_list)