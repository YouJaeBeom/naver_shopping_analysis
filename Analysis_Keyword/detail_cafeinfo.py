import re
import requests
from bs4 import BeautifulSoup as bs
import json
import datetime

def getcafeid(url):
    response = requests.get(url)
    """with open("TextFile.txt", "w") as file:
        file.write(response.text)"""
    #print(response.text)
    cafeid = re.findall(r'g_sClubId = .*;', response.text)
    cafeid = cafeid[0].replace('g_sClubId = ', '').replace('"','').replace(';','').strip()

    return cafeid

def getcafeinfo(url):

    cafeid = getcafeid(url)

    art = re.findall(r'art=.*', url)
    art = art[0].replace('art=', '').replace('"','').replace(';','').strip()

    pageid = re.findall(r'/.*\?', url)
    pageid = pageid[0].replace('?','').split("/")[4]
     

    cookies = {
        'NNB': 'DULXWITNGSGGE',
        'nx_ssl': '2',
        'ASID': 'dc957c49000001810000e7bc00000053',
        '_ga_7VKFYR6RV1': 'GS1.1.1655285848.1.1.1655287263.60',
        '_ga': 'GA1.2.678320805.1655285848',
        'page_uid': 'hqwT+sprvhGssdiWr8Nsssssto4-179682',
        'nid_inf': '1635002861',
        'NID_AUT': '56gqxDwQU3QG6cgQjGGG7esG7fzM2Ceq/atZNnrjqXVzf7MvjGLHWO1AWKnpzTzX',
        'NID_SES': 'AAABgaLCzZ7TKkqH+h/VQ4rzcd9HfCeW5R8W7fiKSr0TBidnd21Qy53H7J/w6Yi3IuJbXu/150ry4nqkYDDz3z4xpH2w+JRNCAV/EjqrTgMik1t4wgaK8uCvGThTqh4KPzv7FGhCDIUar52C2vT5oWCp7O/oWAE7afzYro9T7doxvu7byNxBzN/eKyRku9g2nPAsOfs+hj6V6nP2e6WR8ob5EfNN+k4YBSO6M3yg7qbviq5+mN74eM7FZNUqvkuJfCUQLMFdRA/kqgGHL9SKGtPXVHYwp3LNaBl7Nnh7lfgaqj+tlQrFax7YJpmZ9vhOpoTbeC7iapodXnNtX4XLwW5Y9exebH+aWNnfhRKW7M4H6/cF9YYdc7r0FLzosxv0voHqCPkFq/IxtKdCcQ1GBIAYlUyL74SUmuJX6M1ujWSYks3CRZEzdFPE0rcyW6ZPgmzPt/NrHZPhmS4xDPCt8Ipz1tQ1t4JHmqDPXjd2z86ztKkprZqvRqmmnKpcNamsVKh6vHyHWGbpbPajjfi8jzqxHnw=',
        'NID_JKL': 'AiAUnyw/Xv3SlM/Do39bDu9XcrhP7ysAdNccZ0J4xT4=',
        'JSESSIONID': '38B5A5D78B35F1007D7F93701CD0342D',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Accept': 'application/json, text/plain, */*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        #'Referer': 'https://cafe.naver.com/ca-fe/cafes/'+cafeid+'/articles/'+pageid+'?art=ZXh0ZXJuYWwtc2VydmljZS1uYXZlci1zZWFyY2gtY2FmZS1wcg.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjYWZlVHlwZSI6IkNBRkVfVVJMIiwiY2FmZVVybCI6Imltc2FuYnUiLCJhcnRpY2xlSWQiOjYxMzI1NjQxLCJpc3N1ZWRBdCI6MTY1NTQ0NTIxMTg5Nn0.dEUKsLrzhqvI_Xn-b4OKmBVMi-vO85stcWGkF4jwNyU&query=%EB%A7%88%EC%8A%A4%ED%81%AC&where=search&tc=naver_search&oldPath=%2FArticleRead.nhn%3Farticleid%3D61325641%26art%3DZXh0ZXJuYWwtc2VydmljZS1uYXZlci1zZWFyY2gtY2FmZS1wcg.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjYWZlVHlwZSI6IkNBRkVfVVJMIiwiY2FmZVVybCI6Imltc2FuYnUiLCJhcnRpY2xlSWQiOjYxMzI1NjQxLCJpc3N1ZWRBdCI6MTY1NTQ0NTIxMTg5Nn0.dEUKsLrzhqvI_Xn-b4OKmBVMi-vO85stcWGkF4jwNyU%26query%3D%25EB%25A7%2588%25EC%258A%25A4%25ED%2581%25AC%26where%3Dsearch%26clubid%3D10094499%26tc%3Dnaver_search',
        'X-Cafe-Product': 'pc',
        'Origin': 'https://cafe.naver.com',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'NNB=DULXWITNGSGGE; nx_ssl=2; ASID=dc957c49000001810000e7bc00000053; _ga_7VKFYR6RV1=GS1.1.1655285848.1.1.1655287263.60; _ga=GA1.2.678320805.1655285848; page_uid=hqwT+sprvhGssdiWr8Nsssssto4-179682; nid_inf=1635002861; NID_AUT=56gqxDwQU3QG6cgQjGGG7esG7fzM2Ceq/atZNnrjqXVzf7MvjGLHWO1AWKnpzTzX; NID_SES=AAABgaLCzZ7TKkqH+h/VQ4rzcd9HfCeW5R8W7fiKSr0TBidnd21Qy53H7J/w6Yi3IuJbXu/150ry4nqkYDDz3z4xpH2w+JRNCAV/EjqrTgMik1t4wgaK8uCvGThTqh4KPzv7FGhCDIUar52C2vT5oWCp7O/oWAE7afzYro9T7doxvu7byNxBzN/eKyRku9g2nPAsOfs+hj6V6nP2e6WR8ob5EfNN+k4YBSO6M3yg7qbviq5+mN74eM7FZNUqvkuJfCUQLMFdRA/kqgGHL9SKGtPXVHYwp3LNaBl7Nnh7lfgaqj+tlQrFax7YJpmZ9vhOpoTbeC7iapodXnNtX4XLwW5Y9exebH+aWNnfhRKW7M4H6/cF9YYdc7r0FLzosxv0voHqCPkFq/IxtKdCcQ1GBIAYlUyL74SUmuJX6M1ujWSYks3CRZEzdFPE0rcyW6ZPgmzPt/NrHZPhmS4xDPCt8Ipz1tQ1t4JHmqDPXjd2z86ztKkprZqvRqmmnKpcNamsVKh6vHyHWGbpbPajjfi8jzqxHnw=; NID_JKL=AiAUnyw/Xv3SlM/Do39bDu9XcrhP7ysAdNccZ0J4xT4=; JSESSIONID=38B5A5D78B35F1007D7F93701CD0342D',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        'requestFrom': 'A',
        'orderBy': 'asc',
        'art': art,
    }

    response = requests.get('https://apis.naver.com/cafe-web/cafe-articleapi/v2/cafes/'+cafeid+'/articles/'+pageid+'/comments/pages/1', params=params, cookies=cookies, headers=headers)
    response_json = json.loads(response.text)
    readCount = response_json['result']['article']['readCount']
    writeDate = response_json['result']['article']['writeDate']
    writeDate = datetime.datetime.fromtimestamp(writeDate/1000.0)


    return readCount, writeDate

if __name__ == "__main__":
    getcafeinfo("https://cafe.naver.com/imsanbu/61325641?art=ZXh0ZXJuYWwtc2VydmljZS1uYXZlci1zZWFyY2gtY2FmZS1wcg.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjYWZlVHlwZSI6IkNBRkVfVVJMIiwiY2FmZVVybCI6Imltc2FuYnUiLCJhcnRpY2xlSWQiOjYxMzI1NjQxLCJpc3N1ZWRBdCI6MTY1NTUzNDQ3MzEzMH0.2BBMBQJuIIb8AkXd8iRCSLZASgvG1pcLt88DbP2AC7E")
    
    #ex()