import requests
from bs4 import BeautifulSoup as bs
import tor 

def related_keywords(keyword):
    ## setting tor
    headers = {
        'Referer': 'https://msearch.shopping.naver.com/search/all?where=all&query={}'.format(keyword).encode('utf-8').decode('iso-8859-1'),
    }
    proxies = {
        'http': 'socks5://localhost:9050',
    }
    try:
        response = requests.get('https://msearch.shopping.naver.com/search/all?where=all&query='+keyword , proxies=proxies)
    except requests.ConnectionError as ex:
        tor.renew_tor_ip(9051)
        print("ex = ", ex)
        print()
    else:
        soup = bs(response.text, "html.parser")

        #taglist = soup.select('.taglist')
        taglist = soup.find("div",class_="relatedTag_scroll_area__37Cda")

        related_keywords = taglist.find_all("a",class_="linkAnchor")

        related_keywords_list = []
        for related_keyword in related_keywords:
            related_keywords_list.append(related_keyword.text)

        return related_keywords_list

if __name__ == "__main__" :
    keyword = "마스크"
    related_keywords_list = related_keywords(keyword)

    print(related_keywords_list)