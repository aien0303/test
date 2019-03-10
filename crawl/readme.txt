products1.py=newamazing
products2.py=orangetour
Crawl.py=function
test.sql=MySQL


SQL:
DB=test
# 兩個table

table=product
# Pid PK
# days int '天'改''(乾淨)
# name 改成非Uni
# date date格式 '/'改'-'(格式需求)
# price int ','改''
# available int(乾淨)
# total int
# travelagency int
# characteristics

table=travelagency
# TAid PK
# TAname Uni


加分項目:
資料的正確性以及乾淨程度
# 更改

抓取兩家旅行社兩頁以上的商品資料
# 成功，products1.py

多抓取步驟3. 以外，而有出現在Tripesso網站上的內容
# 成功，航班特色

使用requests
# 成功

程式碼的維護性及可擴充性
# 三次更改