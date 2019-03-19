import cv2
import numpy as np

n=0
a=199
new=0

def rotate(image, angle, center=None, scale=1.0):
    # 圖像尺寸
    (h, w)=image.shape[:2]
    # 指定中心
    if center is None:
        center=(w / 2, h / 2)
    # 旋轉
    M=cv2.getRotationMatrix2D(center,angle,scale)
    rotated=cv2.warpAffine(image,M,(w, h))
    # 返回旋转后的图像
    return rotated

while n<=a:
    print(n)
    img=cv2.imread('p\\bus\\'+str(n)+'.jpg')
    img=cv2.resize(img,(100,100))
    for r in range(-10,15,5):
        # 正左轉
        rotated=rotate(img,r)
        cv2.imwrite('new\\'+str(new)+'.jpg',rotated)
        new=new+1
    # 翻轉
    img=cv2.flip(img,1)
    for r in range(-10,15,5):
        rotated=rotate(img,r)
        cv2.imwrite('new\\'+str(new)+'.jpg',rotated)
        new=new+1
    n=n+1