import requests
import re
def getpostinfo(url):

    response = requests.get(url)


    volumeNo = re.findall(r'volumeNo=.*\&memberNo', response.url)
    volumeNo = volumeNo[0].replace('volumeNo=', '').replace('"','').replace('&','').replace("memberNo","").strip()

    try: 
        memberNo = re.findall(r'memberNo=.*\&vType=VERTICAL', response.url)
        memberNo = memberNo[0].replace('memberNo=', '').replace('"','').replace('&','').replace("vType=VERTICAL","").strip()
    except:
        memberNo = re.findall(r'memberNo=.*', response.url)
        memberNo = memberNo[0].replace('memberNo=', '').replace('"','').replace(';','').strip()
    
    cookies = {
        'NNB': 'DULXWITNGSGGE',
        'nx_ssl': '2',
        'ASID': 'dc957c49000001810000e7bc00000053',
        '_ga_7VKFYR6RV1': 'GS1.1.1655538255.2.0.1655538255.60',
        '_ga': 'GA1.2.678320805.1655285848',
        'page_uid': 'hq2cAwprvTossvBu7tsssssssVo-278803',
        '_gid': 'GA1.2.464269409.1655538256',
        'BMR': '',
        '_naver_usersession_': 'sSvDrrTSrUkovy8vlIK2ed4Z',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'NNB=DULXWITNGSGGE; nx_ssl=2; ASID=dc957c49000001810000e7bc00000053; _ga_7VKFYR6RV1=GS1.1.1655538255.2.0.1655538255.60; _ga=GA1.2.678320805.1655285848; page_uid=hq2cAwprvTossvBu7tsssssssVo-278803; _gid=GA1.2.464269409.1655538256; BMR=; _naver_usersession_=sSvDrrTSrUkovy8vlIK2ed4Z',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
    }

    params = {
        'volumeNo': volumeNo,
        'memberNo': memberNo,
    }

    response = requests.get('https://post.naver.com/viewer/postView.naver', params=params, cookies=cookies, headers=headers)

    # <meta property="og:createdate" content="2022.06.17. 13:58:17" >
    try:
        writeDate = re.findall(r'"og:createdate" content=".*"', response.text)
        writeDate = writeDate[0].replace('"og:createdate" content=', '').replace('"','').replace(';','').strip()
    except:
        print("volumeNo : ",volumeNo, "memberNo : ", memberNo, url)

    return writeDate

if __name__ == "__main__":
    getpostinfo("https://adcr.naver.com/adcr?x=m0nsujmWJiF7JmZEl+sBWP///w==k8cpGnoenWJXcBQs3AIF4tH7wGYTcrhPNFhTSWtiempX1c+RJA4CtB/jqEA8oR4gpeOU09PxEVlJlKs6wWkKZArD3I7TU7C5Yl2hdpLWZFJCC/SL/p16P7729ol9YO97al1WHI/6vaeON61hmk+ZhoosGDxknOADQnR7OdXsDfIScePJyRxFtsMaKm0ntkSupId36NMC2po3IYr60r6ZWvdxDxnKWHU1LCYt/KqqXcyRjJgPRQWELftVINkhe0Xu5rsmH5moKv0/JGqPWQC4VVlhcm8QW6Pzw1L5W89QMIdMy+epnPcSqm6R2fmik07eS4WzFe4TZbxDSzMmKssMs0guv86sxi6UsZm9xbsPDdK1u3+hvlbAvqQ6NfQJwiPSqldSTarTphptsSVaEYuQhSWHj67AGvp4bg0xYkTGG4KZRQEpkwLTWicj6/ufZgM8SndgxR/Tyi17yliP91RqtZZiUJwBg5OqftseVqofkonDivfojEvCpL+rTL7kQq4Vp7/BkmIgQGv2CXXv4cJko6Rdvyu6dOu6l338uu5zXCXabvoJEcO/PWSGrpfuwbIbyTc/JDOogCm2L/mH1qGXAQPy0TMoBXTa3JBHzb2PF0SHaoI6KbZ1SqQpKTUIl9iZ46zguIZrmCiLt7H0bA5PR/A==")