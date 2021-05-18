import cv2
import os
cap = cv2.VideoCapture(0)
# cap.set(3, 500) #长
cap.set(4, 640)#宽
i = 0#相片起始编号
def draw_cicle(event, x, y, flags, param):
    #print(x, y)
    global i
    if event == cv2.EVENT_LBUTTONDBLCLK:
            print(cv2.imwrite("pic/"+str(i)+".jpg", image))
            i += 1
            

while(1):
    return_value, image = cap.read()

    cv2.namedWindow("image", cv2.WINDOW_NORMAL)  # 创建窗口
    cv2.setMouseCallback("image", draw_cicle)  # 鼠标事件的回调函数
    cv2.imshow('image',image)

    if cv2.waitKey(1) & 0xFF == ord('q'):        
        cv2.destroyAllWindows()
        del(cap)
        break
