import re
import Crawl
import datetime
import json

data={
  'displayType': 'G',
  'subCd': '',
  'orderCd': '1',
  'pageALL': '',
  'pageGO': '1',
  'pagePGO': '1',
  'waitData': 'false',
  'waitPage': 'false',
  'mGrupCd': '',
  'SrcCls': '',
  'tabList': '',
  'regmCd': '',
  'regsCd': '',
  'beginDt': '',
  'endDt': '',
  'portCd': '',
  'tdays': '',
  'bjt': '',
  'carr': '',
  'allowJoin': '1',
  'allowWait': '1',
  'ikeyword': ''
}
# 月份+6
def monthdelta(date, delta):
    m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
    if not m: m = 12
    d = min(date.day, [31,
        29 if y%4==0 and not y%400==0 else 28,31,30,31,30,31,31,30,31,30,31][m-1])
    return date.replace(day=d,month=m, year=y)

data['beginDt']=str(datetime.date.today()).replace('-','/')
data['endDt']=str(monthdelta(datetime.date.today(), 6)).replace('-','/')

travelagency=1
# 頁數設定
for page in range(1,3):
  data['pageALL']=str(page)
  items=Crawl.crawl('https://www.newamazing.com.tw/EW/Services/SearchListData.asp','p',data=data)[0]
  # Json
  dlist=Crawl.JsonLoad(items,'All')

  for n in range(0,len(dlist)):
    # 行程名稱
    TName=dlist[n]['GrupSnm'].replace('\n','').replace(' ','').replace('滿','').replace('促銷','')
    # 天數
    TDays=dlist[n]['GrupLn']
    # 出發日期
    TDate=dlist[n]['LeavDt'].replace("/","-")
    # 價錢
    TPrice=dlist[n]['SaleAm']
    # 總團位
    TTotal=dlist[n]['EstmYqt']
    # 可售位
    TAvailable=dlist[n]['SaleYqt']
    # 行程編號
    prodCd=dlist[n]['GrupCd']
    # 爬蟲
    # https://www.newamazing.com.tw/EW/Services/SearchFlight.asp?prodCd=BKK06190308C&sacctNo=&flightType=1
    items=Crawl.crawl('https://www.newamazing.com.tw/EW/Services/SearchFlight.asp?prodCd='+prodCd+'&sacctNo=&flightType=1','p')[0]  
    # Json
    dlist2=Crawl.JsonLoad(items,'Flights')
    # 特色
    characteristics=Crawl.Characteristics(dlist2)

    if TDays=='天數' or TDate=='出發日期' or TPrice=='售價' or TName=='':
        pass
    else:
      # print(TDays)
      # print(TName)
      # print(TDate)
      # print(TPrice)
      # print(TAvailable)
      # print(TTotal)
      # print(characteristics)
      
      # 存入資料庫
      Crawl.DBI(TDays,TName,TDate,TPrice,TAvailable,TTotal,travelagency,characteristics)