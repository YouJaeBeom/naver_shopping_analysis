import requests
import json
import authorization
import time
import random
import requests

def search_volume(keyword, Authorization):
    

    cookies = {
    'NNB': 'DULXWITNGSGGE',
    'nx_ssl': '2',
    'ASID': 'dc957c49000001810000e7bc00000053',
    '066c80626d06ffa5b32035f35cabe88d': 'j%C2%C3%F4F%26Bn%C1%D7KUBX%99%11%15wB%DB%D1%29K%E0%99%97g%8B%EBz%9C%FEu%40%F9%D4%9D%25b%E6%CA%19%05%BCD%C5%C0%FD%92Z%8B%BF%24%B5%60%13HnL%8B%99%C3%8E2%91%92%AC%14%F0%A7M%0C%A6%82%1B%ED%9D%5B6%FFb%D7C%80%86%F9N%F14f%22%89i%F4%09%00%96%3D%18F%FD%C2%EC%92%A8%C0%E3%EB%3A2t%9B%B4%82%CB%9A%1C%27%06%D4%BBa%8A%16i%90%2B%D2%A0%F4%D0%7E%C5%B7%2A%BE',
    '1a5b69166387515780349607c54875af': '%C1%F9%27nc%D2%A4%82',
    '1b25d439ceac51f5d414df7689017f6c': '%AE%E2%BFK%3D%9B%07K%FD%15%0B%15%DC%97%95%C4%A3%B8%DD%E9%D6%3F%12a%3B%D6%CDj%DA%11%DCB%BB%2B%19%3B%C37%C1%CA%14%7D%7C%11%B9%15%25%83%13%EF%83%24%C1%CB%5C%3E%C7%A4%8DDz%92%C3%0F%82%AA%C8%DC%81%AA%ABq%B0%E7e%3D%E3%A5%A9%A3kD%A6%E8%AC%AD%CF%ED%F8%14tz%5B%F2J%EBya%B8%1D%E4%C0%C9%23%87%8F%1Am%FA%7B%E3%B4%5C6%CC%C9%D4%5D%F2F7A%E3%090K%EA%DC%FA%12%E3%F9%11%25%C0%B1%E0%EA7%8D%E5%E9%21%5E%5B%A1%93%B4%2A%27M%F2g%1D%3A%0D%F9%FD%C6Fd%9B%A5%F4%A6A%F8%EA%B1%F3%2AK%A8%7E%F4%CC%2F%E6%BDv%97%5BH%ACV%C6%1E%B3%F5%B1%B6%BE%7B%8A%BD%CAv%AE%01%ED%18%EE%10%0ARB%A7%C3%27%5Bv%14%97%83S1%7C%B4%BD%84%06%9D%91%BD%26j%B0%18%00%7D%18%8F%0F%F4%0F%1B%DF%CCW%FA%0BcM%89qA%AB%5C%E5%D1%8DD%C9%A6%E5u0%F3%FC3%7Cr%9D%EB%18%26%EB%D4%EF%AF%EF%FF%CC%3C%BF%91%0D%CDC%C3%85%5EC%BE%3E%90%89%BC%8CD%E35%25LC%E7m%CE%5B%FC%1Cj%EFn%27E%5BB%10%81+%93K%FARcJ%82%1E%EA%D3%8D%BD%A6%3B%05%E5%3D%0F%F4%0F%1B%DF%CCW%FA%0BcM%89qA%AB%5C%E5%D1%8DD%C9%A6%E5uD%FE%91e%F8%2A%F3r%EEo.%27%D6%2BXl%29K%E2%98%95p%2F%CD%C1%25%A4%8D%D7%5E%F4T%BAX%29FA%D9%12%87%DCQrO%FA%E9%EE%C7%95.A%25%88%3B%B9G%1Bw%E2U%EAV%D7%EA%27S%15%F31%83%CB%87%A6c%247%F1%88%28X%0F%FC%D7%3F%93%7DT%E6%D5%0D%CB%24%06%17%82%05f%C2%12%EE%ED%A0%BA%13%AE%BE%87%CDL%BC%0C%139%C4%251E%E0%E4%175%F0%3C%81s%17%F0.%19%EDx%BFn%9A%F8%C5%CD%97E%A1%BF%BE%AE%12%9B%CA%83%15%F2l%91%9E%A6%99%B3b%19P%B2%8ENd%22%DDpAH%DE%92%DA%C2%AC%0F%5D%E94%FC%88%82LN%F5%24J%A1E%A6%2A%24%9Dr%04%A2T%C0%EAz%2BO%3C%89%88%A0q%CB0L%15%CFy%2Cbv%CF2%DC',
    'elicjyl': 'true',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Accept': 'application/json, text/plain, */*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Authorization': (Authorization),
        'Connection': 'keep-alive',
        'Referer': 'https://manage.searchad.naver.com/customers/2565665/tool/keyword-planner',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'NNB=DULXWITNGSGGE; nx_ssl=2; ASID=dc957c49000001810000e7bc00000053; 066c80626d06ffa5b32035f35cabe88d=j%C2%C3%F4F%26Bn%C1%D7KUBX%99%11%15wB%DB%D1%29K%E0%99%97g%8B%EBz%9C%FEu%40%F9%D4%9D%25b%E6%CA%19%05%BCD%C5%C0%FD%92Z%8B%BF%24%B5%60%13HnL%8B%99%C3%8E2%91%92%AC%14%F0%A7M%0C%A6%82%1B%ED%9D%5B6%FFb%D7C%80%86%F9N%F14f%22%89i%F4%09%00%96%3D%18F%FD%C2%EC%92%A8%C0%E3%EB%3A2t%9B%B4%82%CB%9A%1C%27%06%D4%BBa%8A%16i%90%2B%D2%A0%F4%D0%7E%C5%B7%2A%BE; 1a5b69166387515780349607c54875af=%C1%F9%27nc%D2%A4%82; 1b25d439ceac51f5d414df7689017f6c=%AE%E2%BFK%3D%9B%07K%FD%15%0B%15%DC%97%95%C4%A3%B8%DD%E9%D6%3F%12a%3B%D6%CDj%DA%11%DCB%BB%2B%19%3B%C37%C1%CA%14%7D%7C%11%B9%15%25%83%13%EF%83%24%C1%CB%5C%3E%C7%A4%8DDz%92%C3%0F%82%AA%C8%DC%81%AA%ABq%B0%E7e%3D%E3%A5%A9%A3kD%A6%E8%AC%AD%CF%ED%F8%14tz%5B%F2J%EBya%B8%1D%E4%C0%C9%23%87%8F%1Am%FA%7B%E3%B4%5C6%CC%C9%D4%5D%F2F7A%E3%090K%EA%DC%FA%12%E3%F9%11%25%C0%B1%E0%EA7%8D%E5%E9%21%5E%5B%A1%93%B4%2A%27M%F2g%1D%3A%0D%F9%FD%C6Fd%9B%A5%F4%A6A%F8%EA%B1%F3%2AK%A8%7E%F4%CC%2F%E6%BDv%97%5BH%ACV%C6%1E%B3%F5%B1%B6%BE%7B%8A%BD%CAv%AE%01%ED%18%EE%10%0ARB%A7%C3%27%5Bv%14%97%83S1%7C%B4%BD%84%06%9D%91%BD%26j%B0%18%00%7D%18%8F%0F%F4%0F%1B%DF%CCW%FA%0BcM%89qA%AB%5C%E5%D1%8DD%C9%A6%E5u0%F3%FC3%7Cr%9D%EB%18%26%EB%D4%EF%AF%EF%FF%CC%3C%BF%91%0D%CDC%C3%85%5EC%BE%3E%90%89%BC%8CD%E35%25LC%E7m%CE%5B%FC%1Cj%EFn%27E%5BB%10%81+%93K%FARcJ%82%1E%EA%D3%8D%BD%A6%3B%05%E5%3D%0F%F4%0F%1B%DF%CCW%FA%0BcM%89qA%AB%5C%E5%D1%8DD%C9%A6%E5uD%FE%91e%F8%2A%F3r%EEo.%27%D6%2BXl%29K%E2%98%95p%2F%CD%C1%25%A4%8D%D7%5E%F4T%BAX%29FA%D9%12%87%DCQrO%FA%E9%EE%C7%95.A%25%88%3B%B9G%1Bw%E2U%EAV%D7%EA%27S%15%F31%83%CB%87%A6c%247%F1%88%28X%0F%FC%D7%3F%93%7DT%E6%D5%0D%CB%24%06%17%82%05f%C2%12%EE%ED%A0%BA%13%AE%BE%87%CDL%BC%0C%139%C4%251E%E0%E4%175%F0%3C%81s%17%F0.%19%EDx%BFn%9A%F8%C5%CD%97E%A1%BF%BE%AE%12%9B%CA%83%15%F2l%91%9E%A6%99%B3b%19P%B2%8ENd%22%DDpAH%DE%92%DA%C2%AC%0F%5D%E94%FC%88%82LN%F5%24J%A1E%A6%2A%24%9Dr%04%A2T%C0%EAz%2BO%3C%89%88%A0q%CB0L%15%CFy%2Cbv%CF2%DC; elicjyl=true',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        'format': 'json',
        'hintKeywords': keyword,
        'siteId': '',
        'month': '',
        'biztpId': '',
        'event': '',
        'includeHintKeywords': '0',
        'showDetail': '1',
        'keyword': '',
    }

    response = requests.get('https://manage.searchad.naver.com/keywordstool', params=params, cookies=cookies, headers=headers)

    response_json = json.loads(response.text)
    monthlyPcQcCnt =  response_json['keywordList'][0]['monthlyPcQcCnt']
    monthlyMobileQcCnt =  response_json['keywordList'][0]['monthlyMobileQcCnt']

    return monthlyPcQcCnt, monthlyMobileQcCnt



if __name__ == "__main__":
    keyword = "마스크"
    Authorization = authorization.authorization()
    monthlyPcQcCnt, monthlyMobileQcCnt = search_volume(keyword, Authorization)
