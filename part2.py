# a)爬蟲，沒時間
import requests
from bs4 import BeautifulSoup
import time
import re
import csv


time.sleep(2)
url="https://www.ptt.cc/bbs/LoL/index.html"
headers_data={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
response=requests.get(url, headers=headers_data)
soup=BeautifulSoup(response.text,'lxml')
items=soup.select('div div.r-list-container')

for item in items:
    date=item.find('div',class_='date').get_text()
    title=item.find('div',class_='title').get_text()
    author=item.find('div',class_='author').get_text()
#     # category=item.find('h2').string
#     # title=item.find('h1').get_text()
#     # link=item.find('a').get('href')
        
    print(date)
    print(title)
    print(author)
# b)現做一個網站，爬蟲，隨機選取