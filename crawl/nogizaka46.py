import requests
from bs4 import BeautifulSoup
import time
import re
import json
import urllib.parse as UP
import pymysql

db=pymysql.connect("localhost","root","root",'JPdb')
url="https://www.uta-net.com/artist/12550/"
headers_data={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
time.sleep(2)
response=requests.get(url,headers=headers_data)
soup=BeautifulSoup(response.text,'lxml')
items=soup.select('tbody tr')
for item in items:
    parsed=[]
    gtag=item.find('a').get('href')
    curl='https://www.uta-net.com'+gtag
    time.sleep(2)
    cresponse=requests.get(curl, headers=headers_data)
    csoup=BeautifulSoup(cresponse.text,'lxml')
    citems=csoup.select('div.clearfix div.left')
    for item in citems:
        song_name=item.find('div',class_='title').get_text().replace("\n","").replace("試聴する","")
        lyric=item.find('div',id='kashi_area').get_text().replace("\u3000","")
    c2items=csoup.select('div.clearfix p.youtube_button')
    for item in c2items:
        gtag2=item.find('a').get('href')
        curl2='https://www.uta-net.com'+gtag2
        time.sleep(2)
        cresponse2=requests.get(curl2, headers=headers_data)
        csoup2=BeautifulSoup(cresponse2.text,'lxml')
        c2items=csoup2.select('div#movie_area div#youtube_movie')
        for item in c2items:
            youtube_video=str(item.find('iframe'))
    target=[
        song_name,
        lyric,
        youtube_video,
    ]
    with db.cursor() as cursor:
        sql="""INSERT INTO music(song_name,lyric,youtube_video) values(%s,%s,%s)"""
        cursor.execute(sql,target)
        db.commit()