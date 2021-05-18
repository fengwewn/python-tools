#是找图形.py的补充，realtime版本

import cv2
from matplotlib import pyplot as plt
import numpy as np  
import math 

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.75)#0.75打开，0.25关闭
cap.set(3, 1920)#长
cap.set(4, 1080)#宽
#cam.set(cv2.CAP_PROP_SETTINGS, 1)
cap.set(11,50)#对比度 40
cap.set(12, 50)#饱和度 50
cap.set(13, 50)#色调 50

#capture.set(CV_CAP_PROP_EXPOSURE, 50);   


kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))

def fidd(contours,img):
    for cnt in contours:
        # .03 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt,.03 * cv2.arcLength(cnt, True), True)
        #print (len(approx))
        if len(approx)==3:
            print ("triangle")
            #continue
            area = cv2.contourArea(approx)
            if(area >100):
                cv2.drawContours(img,[approx],0,(122,212,78),1)
            print(area)
    return img

while(1):

    ret,frame = cap.read()
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #图像RGB 转HSV，因为在低污染的时候HSV还是挺好用的，针对蓝红颜色还是建议LAB
    cv2.imshow('hsv',hsv) 
    gray = hsv[:,:,0]#灰度图
                
    ret,thresh = cv2.threshold(gray,65,255,3)
    ret1,thresh1 = cv2.threshold(thresh,86,255,4)
    #这里用的是绿色的范围为测试样本，上下切一下，只保留范围内
    #用cv2.threshold是个人习惯
    ret1,thresh2 = cv2.threshold(thresh1,0,255,0)
    #二值化
    erosion =cv2.erode(thresh2,kernel,2)
    #过滤一下
    #
#     closing = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
#     closing1 = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
    
#     edges_w = cv2.Canny(closing, 40, 140, apertureSize = 3)
    img,contours,h = cv2.findContours(erosion,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
    img=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    img = fidd(contours,img)
    cv2.imshow('img',img)
    cv2.imshow('or',frame)
    cv2.imshow('th',thresh)
    cv2.imshow('th1',thresh1)
    cv2.imshow('th2',thresh2)
    cv2.imshow('erosion',erosion)
#     cv2.imshow('clos',closing)
#     cv2.imshow('clos1',closing1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break 
