import re

# 第一題
urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png",
]

# 取
urlsLen=len(urls)
aList=[]
for a in range(0,urlsLen):
    # print(urls[a])
    # 字串
    match=re.search(r'(?P<other>.+)/(?P<target>.{5})',urls[a])
    
    # 直接抓5個字元
    aList.extend([match.group('target')])
aList.remove('haha.')
print(aList)
# if判斷存在+1不存在=1



# 第二題
def anonymous(x): 
     return x**2 + 1 
 
def integrate(fun, start, end): 
    step = 0.1
    intercept = start
    area = 0
    while intercept < end:
        intercept += step

        # 只加這行，好像是積分，之前有看過類似
        area=area+fun(intercept)*step

    return area 

print(integrate(anonymous, 0, 10))

# 第三題
sum=0
# 1~1000
for x in range(1,1001):
    # 3或5餘數0
    if x%3==0 or x%5==0:
      sum=sum+x
print(sum)