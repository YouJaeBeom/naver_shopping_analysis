import requests
import json
from bs4 import BeautifulSoup as bs


def getQnA(mallProductId):
    cookies = {
        'NNB': 'DULXWITNGSGGE',
        'nx_ssl': '2',
        'ASID': 'dc957c49000001810000e7bc00000053',
        'nid_inf': '1631157862',
        'NID_AUT': 'mNO+8XvZHGi+wDfIukaykGursjHL4QHNPkYFKsLDhOgh7+QGMmKkFlp7pQmQzsVL',
        'NID_SES': 'AAABimuiecTfiZAYgmt6qSrlPtHiwp7hP3adedT08vgJqIy2rJMyAvLngsMlXZDAOLWjJKRco1x86zlQeqY4eufijPV+35/OJbyXpxkiQdbYQY4jFpgFo6e+BGWBU7Wnq2t6yPhFwlc8N4SZL29Acn/XJhyA9viIpyhspTGykQ+aiA21Na9SHcEJZQD5kyuOyt+8qbwD4KdbrYsXqFXE0++UWtxG/bmjQZXxQZhgxKJB2VarX74PyOUmuzTH1+J1BqMVE2TPnnvY5PBpP8cczkHNQvBE/Y+ASiPobVHYWJfCulaz1063TdztljBmauBI9mKwQ/OklB5OEEKH7WJi8iEfKaQelobGRPKonaFD1MtXYEVr9m+RRpXIUNtBn3+QaQ3GWlXfF71jiOWTWUCJMQ779wh9r+gxEEUypht80m3QkV79X7SIjhkUXpXwm93tirPdK5umlc8ZrU5ld8wfA8DuStEqWfb0Yi/o1UM91kqZytGE0w0nicZjUu5vNGII30LAgHuNx7l8m+4GuCRwsErzk9M=',
        'NID_JKL': 'LJInBtlDv57Cw5ymKhME3AL6TFoX0rDIhlHPSnitVvQ=',
        'page_uid': 'hqkXgwp0JXVssl+A4O4sssssses-212213',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Accept': 'application/json, text/plain, */*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        # 'Referer': 'https://smartstore.naver.com/cityhall/products/6234837639?NaPm=ct%3Dl4cgxwfc%7Cci%3D99b8b411d996f00c02cadf8f0c01afe82db38c31%7Ctr%3Dslsl%7Csn%3D840287%7Chk%3Df80f090f75072d5bd52a1ca1afa34f8e855d601b',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'NNB=DULXWITNGSGGE; nx_ssl=2; ASID=dc957c49000001810000e7bc00000053; nid_inf=1631157862; NID_AUT=mNO+8XvZHGi+wDfIukaykGursjHL4QHNPkYFKsLDhOgh7+QGMmKkFlp7pQmQzsVL; NID_SES=AAABimuiecTfiZAYgmt6qSrlPtHiwp7hP3adedT08vgJqIy2rJMyAvLngsMlXZDAOLWjJKRco1x86zlQeqY4eufijPV+35/OJbyXpxkiQdbYQY4jFpgFo6e+BGWBU7Wnq2t6yPhFwlc8N4SZL29Acn/XJhyA9viIpyhspTGykQ+aiA21Na9SHcEJZQD5kyuOyt+8qbwD4KdbrYsXqFXE0++UWtxG/bmjQZXxQZhgxKJB2VarX74PyOUmuzTH1+J1BqMVE2TPnnvY5PBpP8cczkHNQvBE/Y+ASiPobVHYWJfCulaz1063TdztljBmauBI9mKwQ/OklB5OEEKH7WJi8iEfKaQelobGRPKonaFD1MtXYEVr9m+RRpXIUNtBn3+QaQ3GWlXfF71jiOWTWUCJMQ779wh9r+gxEEUypht80m3QkV79X7SIjhkUXpXwm93tirPdK5umlc8ZrU5ld8wfA8DuStEqWfb0Yi/o1UM91kqZytGE0w0nicZjUu5vNGII30LAgHuNx7l8m+4GuCRwsErzk9M=; NID_JKL=LJInBtlDv57Cw5ymKhME3AL6TFoX0rDIhlHPSnitVvQ=; page_uid=hqkXgwp0JXVssl+A4O4sssssses-212213',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        'filterMyComment': 'false',
        'page': '1',
        'size': '10',
    }

    response = requests.get('https://smartstore.naver.com/i/v1/comments/PRODUCTINQUIRY/'+mallProductId, params=params, cookies=cookies, headers=headers)


    response_json = json.loads(response.text)
    qnaCnt =  response_json['totalElements']

    #print(qnaCnt)
    return qnaCnt 

def getinfo(mallProductId):
    cookies = {
        'NA_CO': 'ct%3Dl4cgxwfc%7Cci%3D99b8b411d996f00c02cadf8f0c01afe82db38c31%7Ctr%3Dslsl%7Chk%3Df80f090f75072d5bd52a1ca1afa34f8e855d601b%7Ctrx%3Dundefined',
        'wcs_bt': 's_b8805abdaa43:1655109015|d496c0f5ccbdc8:1655109015',
        'NNB': 'DULXWITNGSGGE',
        'nx_ssl': '2',
        'ASID': 'dc957c49000001810000e7bc00000053',
        'nid_inf': '1631157862',
        'NID_AUT': 'mNO+8XvZHGi+wDfIukaykGursjHL4QHNPkYFKsLDhOgh7+QGMmKkFlp7pQmQzsVL',
        'NID_SES': 'AAABimuiecTfiZAYgmt6qSrlPtHiwp7hP3adedT08vgJqIy2rJMyAvLngsMlXZDAOLWjJKRco1x86zlQeqY4eufijPV+35/OJbyXpxkiQdbYQY4jFpgFo6e+BGWBU7Wnq2t6yPhFwlc8N4SZL29Acn/XJhyA9viIpyhspTGykQ+aiA21Na9SHcEJZQD5kyuOyt+8qbwD4KdbrYsXqFXE0++UWtxG/bmjQZXxQZhgxKJB2VarX74PyOUmuzTH1+J1BqMVE2TPnnvY5PBpP8cczkHNQvBE/Y+ASiPobVHYWJfCulaz1063TdztljBmauBI9mKwQ/OklB5OEEKH7WJi8iEfKaQelobGRPKonaFD1MtXYEVr9m+RRpXIUNtBn3+QaQ3GWlXfF71jiOWTWUCJMQ779wh9r+gxEEUypht80m3QkV79X7SIjhkUXpXwm93tirPdK5umlc8ZrU5ld8wfA8DuStEqWfb0Yi/o1UM91kqZytGE0w0nicZjUu5vNGII30LAgHuNx7l8m+4GuCRwsErzk9M=',
        'NID_JKL': 'LJInBtlDv57Cw5ymKhME3AL6TFoX0rDIhlHPSnitVvQ=',
        'page_uid': 'hqkXgwp0JXVssl+A4O4sssssses-212213',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'NA_CO=ct%3Dl4cgxwfc%7Cci%3D99b8b411d996f00c02cadf8f0c01afe82db38c31%7Ctr%3Dslsl%7Chk%3Df80f090f75072d5bd52a1ca1afa34f8e855d601b%7Ctrx%3Dundefined; wcs_bt=s_b8805abdaa43:1655109015|d496c0f5ccbdc8:1655109015; NNB=DULXWITNGSGGE; nx_ssl=2; ASID=dc957c49000001810000e7bc00000053; nid_inf=1631157862; NID_AUT=mNO+8XvZHGi+wDfIukaykGursjHL4QHNPkYFKsLDhOgh7+QGMmKkFlp7pQmQzsVL; NID_SES=AAABimuiecTfiZAYgmt6qSrlPtHiwp7hP3adedT08vgJqIy2rJMyAvLngsMlXZDAOLWjJKRco1x86zlQeqY4eufijPV+35/OJbyXpxkiQdbYQY4jFpgFo6e+BGWBU7Wnq2t6yPhFwlc8N4SZL29Acn/XJhyA9viIpyhspTGykQ+aiA21Na9SHcEJZQD5kyuOyt+8qbwD4KdbrYsXqFXE0++UWtxG/bmjQZXxQZhgxKJB2VarX74PyOUmuzTH1+J1BqMVE2TPnnvY5PBpP8cczkHNQvBE/Y+ASiPobVHYWJfCulaz1063TdztljBmauBI9mKwQ/OklB5OEEKH7WJi8iEfKaQelobGRPKonaFD1MtXYEVr9m+RRpXIUNtBn3+QaQ3GWlXfF71jiOWTWUCJMQ779wh9r+gxEEUypht80m3QkV79X7SIjhkUXpXwm93tirPdK5umlc8ZrU5ld8wfA8DuStEqWfb0Yi/o1UM91kqZytGE0w0nicZjUu5vNGII30LAgHuNx7l8m+4GuCRwsErzk9M=; NID_JKL=LJInBtlDv57Cw5ymKhME3AL6TFoX0rDIhlHPSnitVvQ=; page_uid=hqkXgwp0JXVssl+A4O4sssssses-212213',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
    }

    params = {
        'NaPm': 'ct=l4cgxwfc|ci=99b8b411d996f00c02cadf8f0c01afe82db38c31|tr=slsl|sn=840287|hk=f80f090f75072d5bd52a1ca1afa34f8e855d601b',
    }

    response = requests.get('https://smartstore.naver.com/main/products/'+mallProductId, params=params, cookies=cookies, headers=headers)
    soup = bs(response.text, "html.parser")

    try:
        store_keepCnt = soup.select('.number')[0].text
        score = soup.select('strong._2pgHN-ntx6:nth-child(2)')[0].text
        qnaCnt = getQnA(mallProductId)
        #related_tag = soup.select('._3Vox1DKZiA')
    except :
        store_keepCnt = None
        score = None
        qnaCnt = None
        #related_tag = None

    return store_keepCnt, score, qnaCnt