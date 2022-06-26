import re
import requests
from bs4 import BeautifulSoup as bs
import json


def getbloginfo(url):

    response = requests.get(url)

    blogId = response.url.split("/")[3]
    logNo = response.url.split("/")[4]

    cookies = {
        'NNB': 'DULXWITNGSGGE',
        'nx_ssl': '2',
        'ASID': 'dc957c49000001810000e7bc00000053',
        '_ga_7VKFYR6RV1': 'GS1.1.1655285848.1.1.1655287263.60',
        '_ga': 'GA1.2.678320805.1655285848',
        'page_uid': 'hq1zAsprvTossvBt604sssssspC-010047',
        'JSESSIONID': 'D1E818F12CF92AB22602A32BEEB1970A.jvm1',
        '_naver_usersession_': 'A96n5QV/hZNCsCY4wJwH4IgG',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': response.url,
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'NNB=DULXWITNGSGGE; nx_ssl=2; ASID=dc957c49000001810000e7bc00000053; _ga_7VKFYR6RV1=GS1.1.1655285848.1.1.1655287263.60; _ga=GA1.2.678320805.1655285848; page_uid=hq1zAsprvTossvBt604sssssspC-010047; JSESSIONID=D1E818F12CF92AB22602A32BEEB1970A.jvm1; _naver_usersession_=A96n5QV/hZNCsCY4wJwH4IgG',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'iframe',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        'blogId': blogId,
        'logNo': logNo,
        'redirect': 'Dlog',
        'widgetTypeCall': 'true',
        'directAccess': 'false',
    }

    response = requests.get('https://blog.naver.com/PostView.naver', params=params, cookies=cookies, headers=headers)
    soup = bs(response.text, "html.parser")
    
    try:
        writeDate = soup.find('span', class_='se_publishDate').text
    except:
        try:
            # date fil5 pcol2 _postAddDate
            writeDate = soup.find('p', class_='date fil5 pcol2 _postAddDate').text
        except :
            print("writeDate None")
            writeDate = None
        

    return writeDate
    

if __name__ == "__main__":
    getbloginfo("https://adcr.naver.com/adcr?x=+a8+h/1z6Yp04ApqeNQQJv///w==kIQqEAieZsaNP0Ta/FtKK9yHfY4Ajl9MLi/JaviN2Vz49w5rV6jsEJKC4ZS/0hj3BeqbON3pt9Ykii4H08tUWtXxjvIbKBbB3Ooi4eVET0RJ4YniEMH4f75vfwtmnE4KpxWrqgYUugo/QGBmoyLuhoPfF5UG24aoDAu4THFeEXKInq/5eNcDebFalChhsGyiYX6AzwmP8dRt0EidROFXScGBnSdU8q718mFPWqabeV7+O9XtMdE5CUqI1xeDmED7AG+h+5pFhTuaQ1d1YyRTQHfQELsSRD5P0YsFFSEw3PDpjs0DV16/l8ZlFG9Jr1AzmfpxKOgMs46MAeAXJgxMZpOTQ/rRIX+FTRSsHQoBAdVixyVaY/hCiC4O9UdtyxcmQxzQbpWWAaN45gZDSFMTSgmdWphrGxlsX9IgVofqR/uDhdFAzwTW2EkbMF9jFJS5UbKCDRcnu+7gSf8fTBWMFnGmIBakcf8hpTYJsZL+NTWovR1USceD+zTw8uDcGj9q4zLqRKq6VYP4NWOKiLnpqys8C/i2T3JPOo5EtZvU2vR6gl4XjEYs2txeIhbJRfod+TpuS8qn10JdHLtNme3caoxbzAVrnKF0DR2KQ0lVe3vhcAng+s9GExKymZAtucgVRIgyNzMjsYPzVC+tt4HH/BcAzjIm6EONSRCEFmBW2itBcIRZsJGJE08NhJhBCJb8a")
    #getbloginfo("https://blog.naver.com/mallangear/222625624076")