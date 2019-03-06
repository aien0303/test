import numpy as np
import cv2

frame=cv2.imread("0.jpg")
hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
frame_data=np.asarray(hsv)
# print(frame_data.shape)
row,col,channels=frame.shape

H=hsv[:,:,0]
# print(H[0].shape)
# print(H.shape)
S=hsv[:,:,1]
V=hsv[:,:,2]

lower_red = np.array([170,100,250])
upper_red = np.array([180,255,255])

for y in range(row):
    for x in range(col):
        if frame[y,x,0]<=180 and frame[y,x,1]<=255 and frame[y,x,2]<=255 and frame[y,x,0]>=180 and frame[y,x,1]>=100 and frame[y,x,2]>=250:
            frame.itemset((y,x,0),255)
            frame.itemset((y,x,1),255)
            frame.itemset((y,x,2),255)
        else:
            frame.itemset((y,x,0),0)
            frame.itemset((y,x,1),0)
            frame.itemset((y,x,2),0)

for i in range(row):
    for j in range(col):
        if frame[i,j,0]==255 and frame[i,j,1]==255 and frame[i,j,2]==255:
            # frame=cv2.imread("0.jpg")
            crop_frame=frame[x-20:x+80,y-20:y+80]
            cv2.imshow("crop_frame",crop_frame)
            cv2.waitKey(0)