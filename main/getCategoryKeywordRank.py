
import json
import requests

def getkeywordrand():
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
        'cid': '50000006',
        'timeUnit': 'date',
        'startDate': '2022-05-12',
        'endDate': '2022-06-12',
        'age': '',
        'gender': '',
        'device': '',
        'page': '25',
        'count': '20',
    }

    response = requests.post('https://datalab.naver.com/shoppingInsight/getCategoryKeywordRank.naver', cookies=cookies, headers=headers, data=data)

    response_json = json.loads(response.text)
    data =  response_json['ranks']
    print(data)

    return response.text