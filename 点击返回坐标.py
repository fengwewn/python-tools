#是找图形.py的补充，由于新版opencv没有了移动鼠标到图形上显示rgb的功能，所以用这个程序代替
import cv2
img = cv2.imread('pic/2/jiaozheng.jpg')
height, width = img.shape[:2]

def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy =str(img[y,x]) #"%d,%d" %(x,y)##"%d,%d" %(x,y)#
        print(xy)
        print('x, y = {}, {}'.format(x, y))
        cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)
        cv2.putText(img,xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
        1.0, (0, 0, 0), thickness=1)
        cv2.imshow("image",img)

cv2.namedWindow("image", 0)
cv2.resizeWindow("image",width ,height);
loc = cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#更好的参考，显示更多东西）
#   # -*- coding:utf-8 -*-
#   import cv2
  
#   img = cv2.imread('11_13/120002.jpg')
#   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#   hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  
#   def mouse_click(event, x, y, flags, para):
#     if event == cv2.EVENT_LBUTTONDOWN: # 左边鼠标点击
#       print('PIX:', x, y)
#       print("BGR:", img[y, x])
#       print("GRAY:", gray[y, x])
#       print("HSV:", hsv[y, x])
  
#   if __name__ == '__main__':
#     cv2.namedWindow("img")
#     cv2.setMouseCallback("img", mouse_click)
#     while True:
#       cv2.imshow('img', img)
#       if cv2.waitKey() == ord('q'):
#         break
#     cv2.destroyAllWindows()
#https://cloud.tencent.com/developer/article/1737231
