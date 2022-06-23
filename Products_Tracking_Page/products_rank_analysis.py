from tkinter.messagebox import NO
import requests
import json
import detail_information_analysis

def ranking_analysis(keyword):
    for pagingIndex in range(1,51):
        params = {
            'sort': 'rel',
            'pagingIndex': '1',
            'pagingSize': '80',
            'viewType': 'list',
            'productSet': 'total',
            'deliveryFee': '',
            'deliveryTypeValue': '',
            'frm': 'NVSHTTL',
            'query': '나이키',
            'origQuery': '나이키',
            'iq': '',
            'eq': '',
            'xq': '',
            'window': '',
        }

        response = requests.get('https://search.shopping.naver.com/api/search/all', params=params)
        response_json = json.loads(response.text)
        data_list =  response_json['shoppingResult']['products']

        for data in data_list:
            
            ## category_n_id 
            category1Id = data['category1Id']
            category2Id = data['category2Id']
            category3Id = data['category3Id']
            category4Id = data['category4Id']

            ## category_n_name 
            category1Name = data['category1Name']
            category2Name = data['category2Name']
            category3Name = data['category3Name']
            category4Name = data['category4Name']

            mallName = data['mallName']
            try:
                mallGrade = data['mallInfoCache']['mallGrade']
            except:
                mallGrade = None
            print("category3Name = {} mallName = {} mallGrade ={}".format(category3Name, mallName, mallGrade))


            rank = data['rank']
            imageUrl = data['imageUrl']
            productName = data['productName']
            price = data['price']
            reviewCount = data['reviewCount']
            purchaseCnt = data['purchaseCnt']
            keepCnt = data['keepCnt']
            mallProductId = data['mallProductId']
            openDate = data['openDate']
            print("rank = {} productName = {} price ={} reviewCount ={} purchaseCnt ={} keepCnt ={} openDate ={}".format(rank, productName, price, reviewCount, purchaseCnt, keepCnt, openDate))


            store_keepCnt, score, qnaCnt, related_tag = detail_information_analysis.getinfo(mallProductId)
            print("store_keepCnt = {} score = {} qnaCnt ={} related_tag ={} \n".format(store_keepCnt, score, qnaCnt, related_tag))

if __name__ == "__main__":
    print(ranking_analysis("마스크"))