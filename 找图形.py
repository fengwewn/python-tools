#用640p的相机，识别范围为5m，测试对象，绿色的巴掌大三角形，测试背景，杂色宣传海报上。
#1080p相机，识别范围为7m，测试情况如上。
#问题还是距离越远，对相机随机噪点，背景光线和测试背景混色的情况处理的越差。


import numpy as np
import cv2
img = cv2.imread("HSV1.jpg")#
#可以改成real time
v = img[:,:,0]
#kernel = np.ones((3, 3), np.uint8)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))

# closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
#显示腐蚀后的图像
#cv2.imshow("Eroded Image",eroded);
#这里使用的是绿色图像，所以需要进行hsv的绿色图像参数切割，这里参数经过实际相机情况微调过。
#建议配合上古opencv进行使用，因为那出来的画面可以鼠标移到图像上就能显示三维值，新版没有了。
#可以使用另外的辅助程序去找三维值。
#红蓝色建议换成lab格式切割。
ret,thresh = cv2.threshold(v,70,255,3)
ret1,thresh1 = cv2.threshold(thresh,77,255,4)
#二值化
ret1,thresh2 = cv2.threshold(thresh1,0,255,0)
#膨胀腐蚀，用来消除噪点
closing = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel)
#用来微调的显示图像，可以都注释掉
cv2.imshow('th',thresh)
cv2.imshow('th1',thresh1)
cv2.imshow('th2',thresh2)
cv2.imshow('clos',closing)
#找线段的点数量
img,contours,h = cv2.findContours(closing,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    # .03 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt,.02 * cv2.arcLength(cnt, True), True)#线段的点再过滤
    #print (len(approx))
    if len(approx)==3:#三角形
        print ("triangle")
        #continue
        area = cv2.contourArea(approx)#求面积
        if(area >100):
            cv2.drawContours(img,[approx],0,(122,212,78),1)#画上去
        print(area)
#     elif len(approx)==4:
#         #print ("square")
#         x , y, w, h=cv2.boundingRect(approx)
#         if((h < 600)and(w<400)):
#             #cv2.drawContours(img,[cnt],0,(94,234,255),2)
#             continue
#     elif len(approx)==8:
#         area = cv2.contourArea(cnt)
#         (cx, cy), radius = cv2.minEnclosingCircle(cnt)
#         circleArea = radius * radius * np.pi
#         #print ('circleArea'+str(circleArea))
#         #print ('area'+str(area))
#         #if (circleArea == area):
#         #cv2.drawContours(img, [approx], 0, (220, 152, 91), 1)
#         #print('ppp')
            
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
