import requests
from bs4 import BeautifulSoup
import time
import re
import datetime
import json

# cookies = {
#     '_ga': 'GA1.3.1928576083.1551859778',
#     '_gid': 'GA1.3.220778838.1551859778',
#     '_gcl_au': '1.1.2136873236.1551859778',
#     '_fbp': 'fb.2.1551859778447.692233054',
#     'MyCssSkin': 'skin_list',
#     'ASPSESSIONIDAGABQDTA': 'CAMBIBCAEJOKKOCBFMNEEIDO',
# }

# headers = {
#     'Origin': 'https://www.newamazing.com.tw',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
#     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'Accept': '*/*',
#     'Referer': 'https://www.newamazing.com.tw/EW/GO/GroupList.asp',
#     'X-Requested-With': 'XMLHttpRequest',
#     'Connection': 'keep-alive',
#     'DNT': '1',
# }
# page=2
# today=str(datetime.date.today()).replace("-","/")

# data = {
#   'displayType': 'G',
#   'subCd': '',
#   'orderCd': '1',
#   'pageALL': '1',
#   'pageGO': '1',
#   'pagePGO': '1',
#   'waitData': 'false',
#   'waitPage': 'false',
#   'mGrupCd': '',
#   'SrcCls': '',
#   'tabList': '',
#   'regmCd': '',
#   'regsCd': '',
#   'beginDt': today,
#   'endDt': today,
#   'portCd': '',
#   'tdays': '',
#   'bjt': '',
#   'carr': '',
#   'allowJoin': '1',
#   'allowWait': '1',
#   'ikeyword': ''
# }

import requests

cookies = {
    '_ga': 'GA1.3.1928576083.1551859778',
    '_gid': 'GA1.3.220778838.1551859778',
    '_gcl_au': '1.1.2136873236.1551859778',
    '_fbp': 'fb.2.1551859778447.692233054',
    'MyCssSkin': 'skin_module',
    'ASPSESSIONIDAGABQDTA': 'EGDEIBCAHGHNOLDDHGHHCHKK',
    '_gat_UA-24142063-13': '1',
    '_gat': '1',
    '_fbc': 'fb.2.1551945541874.IwAR22TyPmNZvefQkQbT_gJ950GKmXb2pSAjKfSTZzrOTGE8X8r1bJ7xz9MiA',
}

headers = {
    'Origin': 'https://www.newamazing.com.tw',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Referer': 'https://www.newamazing.com.tw/EW/GO/GroupList.asp?fbclid=IwAR22TyPmNZvefQkQbT_gJ950GKmXb2pSAjKfSTZzrOTGE8X8r1bJ7xz9MiA',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'DNT': '1',
}

data = {
  'displayType': 'G',
  'subCd': '',
  'orderCd': '1',
  'pageALL': '4',
  'pageGO': '1',
  'pagePGO': '1',
  'waitData': 'false',
  'waitPage': 'false',
  'mGrupCd': '',
  'SrcCls': '',
  'tabList': '',
  'regmCd': '',
  'regsCd': '',
  'beginDt': '2019/03/07',
  'endDt': '2019/09/07',
  'portCd': '',
  'tdays': '',
  'bjt': '',
  'carr': '',
  'allowJoin': '1',
  'allowWait': '1',
  'ikeyword': ''
}

def monthdelta(date, delta):
    m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
    if not m: m = 12
    d = min(date.day, [31,
        29 if y%4==0 and not y%400==0 else 28,31,30,31,30,31,31,30,31,30,31][m-1])
    return date.replace(day=d,month=m, year=y)

data['beginDt']=str(datetime.date.today()).replace("-","/")
data['endDt']=str(monthdelta(datetime.date.today(), 6)).replace("-","/")

# 頁數設定，現在1-10
for page in range(1,11):
  data['pageALL']=str(page)
  time.sleep(2)
  response = requests.get('https://www.newamazing.com.tw/EW/Services/SearchListData.asp', headers=headers, cookies=cookies, data=data)
  soup=BeautifulSoup(response.text,'lxml')
  target=soup.find('p').get_text().replace("LeavDt","出發日期").replace("GrupSnm","行程名稱").replace("EstmYqt","總團位").replace("SaleYqt","可售位").replace("SaleAm","價錢").replace("GrupLn","天數")
  data=json.loads(target)
  dlist=data['All']

  for n in range(0,len(dlist)):
    print(str(dlist[n]['天數'])+'天')
    print(dlist[n]['行程名稱'])
    print(dlist[n]['出發日期'])
    print(dlist[n]['價錢'])
    print(dlist[n]['可售位'])
    print(dlist[n]['總團位'])