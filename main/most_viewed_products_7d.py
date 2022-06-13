
from bs4 import BeautifulSoup
import requests
import json

cookies = {
    'autocomplete': 'use',
    'NNB': 'DULXWITNGSGGE',
    'AD_SHP_BID': '14',
    'nx_ssl': '2',
    'ASID': 'dc957c49000001810000e7bc00000053',
    'spage_uid': 'hqjkmwprvxZssnWiWKossssssiZ-021170',
    'nid_inf': '1631157862',
    'NID_AUT': 'mNO+8XvZHGi+wDfIukaykGursjHL4QHNPkYFKsLDhOgh7+QGMmKkFlp7pQmQzsVL',
    'NID_SES': 'AAABgE/pjxCLRf8HON0CSUdabFgnvWeUkQQ7CsWL+NQwMhefOTqHXcYgdt1hFRWdeRdBuC1lK8J18bZw0F2G9gR7oIhsD+Wae5sRCmkZE0dLajByswStQAS8UlJGm71i5fQ13dqt3IH4T8EMyVFth/V/CtwsmLOZSV2bZz6TgdEfN1ilMH9KwNsX6qYxul7TVrrK3d7h0dJ7ZR3UEa7STUqKbO1z0+vlGNDkFAlLBKug2uHbAil1K05T+khzJVekOjAq/NLIyHv8Ifq1NXI6miEE/4rESmAExNzKlUX11qlslGBQba/dE82FodMZx7HMUKrNY0AwCjUiyIqya5V0VL6RXN1blr5sq2FreiNCPY9JczuKDy2GOxve+eLBLW3U7BJp0I2CzgJKBC1DIJGYI6TSyoEoKSk6gVV1gtCncE8SZ3sWwpmS1e5JOA8tnCJ/t8ljzc8v78m6eMcR3Qdyb5W3g3lJ42eR+50LEnwFMezWO0nqd0zY3AQvstbJJoR5Frf3yw==',
    'NID_JKL': 'LJInBtlDv57Cw5ymKhME3AL6TFoX0rDIhlHPSnitVvQ=',
    'ncpa': '4858315|l4c1twbk|927c5e8482564b12efddb8c575f00f5681a192cf|s_13896d3b7eb40|80d374f4447f0553390bd4a7a2222ba0bef775e5:24|l4c223ug|16b3d132050c58936acc83d407694a7f82eb0e7f|s_419afe53a6bb|216ef0a30e6d34008cf0f68fe952a9cce5495d89:17703|l4c2566o|b24d363fd3e9061389bd93ce70695d674b6ac017|s_1f0b6dd345b2|c562e5d711af772c2575bbc0de754568bf7bfd61:95694|l4c6438w|e2dd271a1f76c70407bb2aca54d87405d35dcd8b|null|6616f5118b0e16be4b405a2e6498994a689f5051',
    'page_uid': 'hqjkmwprvxZssnWiWKossssssiZ-021170',
    'sus_val': 'z1yThr2dCQikMTrA4cOfBJWD',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://search.shopping.naver.com/best/category/keyword?categoryCategoryId=ALL&categoryChildCategoryId=&categoryDemo=M04&categoryMidCategoryId=&categoryRootCategoryId=ALL&chartRank=1&period=P1D',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'autocomplete=use; NNB=DULXWITNGSGGE; AD_SHP_BID=14; nx_ssl=2; ASID=dc957c49000001810000e7bc00000053; spage_uid=hqjkmwprvxZssnWiWKossssssiZ-021170; nid_inf=1631157862; NID_AUT=mNO+8XvZHGi+wDfIukaykGursjHL4QHNPkYFKsLDhOgh7+QGMmKkFlp7pQmQzsVL; NID_SES=AAABgE/pjxCLRf8HON0CSUdabFgnvWeUkQQ7CsWL+NQwMhefOTqHXcYgdt1hFRWdeRdBuC1lK8J18bZw0F2G9gR7oIhsD+Wae5sRCmkZE0dLajByswStQAS8UlJGm71i5fQ13dqt3IH4T8EMyVFth/V/CtwsmLOZSV2bZz6TgdEfN1ilMH9KwNsX6qYxul7TVrrK3d7h0dJ7ZR3UEa7STUqKbO1z0+vlGNDkFAlLBKug2uHbAil1K05T+khzJVekOjAq/NLIyHv8Ifq1NXI6miEE/4rESmAExNzKlUX11qlslGBQba/dE82FodMZx7HMUKrNY0AwCjUiyIqya5V0VL6RXN1blr5sq2FreiNCPY9JczuKDy2GOxve+eLBLW3U7BJp0I2CzgJKBC1DIJGYI6TSyoEoKSk6gVV1gtCncE8SZ3sWwpmS1e5JOA8tnCJ/t8ljzc8v78m6eMcR3Qdyb5W3g3lJ42eR+50LEnwFMezWO0nqd0zY3AQvstbJJoR5Frf3yw==; NID_JKL=LJInBtlDv57Cw5ymKhME3AL6TFoX0rDIhlHPSnitVvQ=; ncpa=4858315|l4c1twbk|927c5e8482564b12efddb8c575f00f5681a192cf|s_13896d3b7eb40|80d374f4447f0553390bd4a7a2222ba0bef775e5:24|l4c223ug|16b3d132050c58936acc83d407694a7f82eb0e7f|s_419afe53a6bb|216ef0a30e6d34008cf0f68fe952a9cce5495d89:17703|l4c2566o|b24d363fd3e9061389bd93ce70695d674b6ac017|s_1f0b6dd345b2|c562e5d711af772c2575bbc0de754568bf7bfd61:95694|l4c6438w|e2dd271a1f76c70407bb2aca54d87405d35dcd8b|null|6616f5118b0e16be4b405a2e6498994a689f5051; page_uid=hqjkmwprvxZssnWiWKossssssiZ-021170; sus_val=z1yThr2dCQikMTrA4cOfBJWD',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'categoryCategoryId': 'ALL',
    'categoryChildCategoryId': '',
    'categoryDemo': 'M04',
    'categoryMidCategoryId': '',
    'categoryRootCategoryId': 'ALL',
    'period': 'P7D',
}

response = requests.get('https://search.shopping.naver.com/best/_next/data/NurwgmMcJVwLajFklX6sM/category/click.json', params=params, cookies=cookies, headers=headers)
response_json = json.loads(response.text)
products =  response_json['pageProps']['dehydratedState']['queries'][2]['state']['data']['products']


print(products[94])
print(len(products))


