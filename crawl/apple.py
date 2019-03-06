import requests
from bs4 import BeautifulSoup
import time
import re
import csv


time.sleep(2)
url="https://tw.appledaily.com/new/realtime"
headers_data={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
response=requests.get(url, headers=headers_data)
soup=BeautifulSoup(response.text,'lxml')
items=soup.select('ul.rtddd li.rtddt')

for item in items:
    time=item.find('time').string
    category=item.find('h2').string
    title=item.find('h1').get_text()
    # link=item.find('a').get('href')
    # test=item.find('h1').get_text()
    match=re.search(r'(?P<title>.+)\((?P<count>\d+)\)',item.find('h1').get_text())
    count=0
    try:
        title=match.group("title")
        count=match.group("count")
    except AttributeError:
        pass

    print(title)
    print(time)
    print(category)