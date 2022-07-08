import requests
from bs4 import BeautifulSoup as bs

def related_keywords(keyword):
    response = requests.get('https://search.shopping.naver.com/search/all?where=all&frm=NVSCTAB&query='+keyword)

    soup = bs(response.text, "html.parser")

    related_keywords = soup.select('.relatedTags_relation_srh__1CleC > ul:nth-child(2) > li')

    related_keywords_list = []
    for related_keyword in related_keywords:
        related_keywords_list.append(related_keyword.text)

    return related_keywords_list

if __name__ == "__main__" :
    keyword = "마스크"
    related_keywords_list = related_keywords(keyword)

    print(related_keywords_list)