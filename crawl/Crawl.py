import requests
from bs4 import BeautifulSoup
import time
import pymysql
import json

# 爬蟲
def crawl(Url,Select,data=''):
    time.sleep(2)
    headers_data={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    if data!='':
        response=requests.get(Url,headers=headers_data,data=data)
    else:
        response=requests.get(Url,headers=headers_data)
    soup=BeautifulSoup(response.text,'lxml')
    items=soup.select(Select)
    return items

# 選取
def ItemFind(Items,Tag,ClassName):
    targetList=[]
    for item in Items:
        target=item.find(Tag,ClassName).get_text()
        targetList.append(target)
    return targetList

# Json
def JsonLoad(items,ObName):
    items=str(items)[3:-4]
    data=json.loads(items)
    dlist=data[ObName]
    return dlist

# 特色
def Characteristics(dlist):
    # 擷取
    global ArrTm,DepTm,characteristics
    if dlist==[]:
        pass
    else:
        if dlist[0]['ArrTm']=='':
            pass
        else:
            ArrTm=int(dlist[0]['ArrTm'].replace(':',''))
        if dlist[0]['DepTm']=='':
            pass
        else:
            DepTm=int(dlist[-1]['DepTm'].replace(':',''))
            
        # 判斷0000-1159早回早去 1600-2359晚回晚去
        characteristics=''
        if len(dlist)<2:
            if len(dlist)==2:
                characteristics+='、直飛'
        if ArrTm!='':
            if ArrTm<1159:
                characteristics+='、早去'
            elif ArrTm>1600:
                characteristics+='、晚去'
        if DepTm!='':
            if DepTm<1159:
                characteristics+='、早回'
            elif DepTm>1600:
                characteristics+='、晚回'
        if characteristics!='':
            characteristics=characteristics[1:]
    return characteristics

# 存入資料庫
def DBI(days,name,date,price,available,total,travelagency,characteristics):
    db=pymysql.connect("localhost","root","root",'test')
    target=[
        days,
        name,
        date,
        price,
        available,
        total,
        travelagency,
        characteristics,
    ]
    with db.cursor() as cursor:
        sql="""INSERT IGNORE INTO products(days,name,date,price,available,total,travelagency,characteristics) values("""+'%s'+',%s'*(len(target)-1)+""")"""
        cursor.execute(sql,target)
        db.commit()
    return print('存入資料庫')