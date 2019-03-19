import re
import Crawl

# 爬蟲
items=Crawl.crawl('http://www.orangetour.com.tw/EW/GO/GroupList.asp','div.row div.thumbnail')

travelagency=2
# 選取
# 旅遊天數
days=Crawl.ItemFind(items,'div','product_days')
# 出發日期
date=Crawl.ItemFind(items,'div','product_date')
# 價錢
price=Crawl.ItemFind(items,'div','product_price')
# 行程名稱
name=Crawl.ItemFind(items,'div','product_name')
# 總團位
total=Crawl.ItemFind(items,'div','product_total')
# 可售位
available=Crawl.ItemFind(items,'div','product_available')

quan=len(days)
for quan in range(0,quan):
    match=re.search(r'(?P<prodCd>\w*)(?P<TName>.*)',name[quan].replace("\n","").replace(" ","").replace("滿","").replace("超","").replace("值","").replace("PUSH",""))
    prodCd=match.group('prodCd')
    TName=match.group('TName')
    TDays=days[quan].replace("天","")
    TDate=date[quan].replace("/","-")
    TPrice=price[quan].replace("\n","").replace("銷售價$","").replace(",","")
    TTotal=total[quan].replace("機位","").replace(" ","")
    TAvailable=available[quan].replace("可售","").replace(" ","")
    # 爬蟲
    # http://www.orangetour.com.tw/EW/Services/SearchFlight.asp?prodCd=0CNX190309FD&sacctNo=&flightType=1
    items=Crawl.crawl('http://www.orangetour.com.tw/EW/Services/SearchFlight.asp?prodCd='+prodCd+'&sacctNo=&flightType=1','p')[0]
    # Json
    dlist=Crawl.JsonLoad(items,'Flights')
    # 特色
    characteristics=Crawl.Characteristics(dlist)

    # 存入資料庫
    Crawl.DBI(TDays,TName,TDate,TPrice,TAvailable,TTotal,travelagency,characteristics)