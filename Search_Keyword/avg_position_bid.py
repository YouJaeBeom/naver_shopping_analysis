import time
import random
import requests

import signaturehelper

BASE_URL = 'https://api.naver.com'
API_KEY = '0100000000a004fa620fc668bae9f873f38e5ec778766d6fbafd9cda1742bf91f5abf27b84'
SECRET_KEY = 'AQAAAACgBPpiD8Zouun4c/OOXsd4IOK7TUOWilUJFAZxe/vfNw=='
CUSTOMER_ID = '2565665'

def get_header(method, uri, api_key, secret_key, customer_id):
    timestamp = str(round(time.time() * 1000))
    signature = signaturehelper.Signature.generate(timestamp, method, uri, SECRET_KEY)
    return {'Content-Type': 'application/json; charset=UTF-8', 
            'X-Timestamp': timestamp, 'X-API-KEY': API_KEY, 
            'X-Customer': str(CUSTOMER_ID), 'X-Signature': signature}

def avg_position_bid():
    uri = '/estimate/average-position-bid/keyword'
    method = 'POST'
    r = requests.post(BASE_URL + uri, json={'device': 'PC', 'items': [{'key': '제주여행', 'position': 1}, {'key': '게스트하우스', 'position': 2}, {'key': '자전거여행', 'position': 3}]}, headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))

    print("#response status_code = {}".format(r.status_code))
    print("#response body = {}".format(r.json()))

if __name__ == "__main__" :
    avg_position_bid()
