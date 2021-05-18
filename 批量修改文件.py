import os.path
import glob
import cv2
import matplotlib.pyplot as plt
def convertjpg(jpgfile,outdir,width=128,height=128):#更改长宽
    
    src = cv2.imread(jpgfile, cv2.IMREAD_ANYCOLOR)#读取文件
    
    src_RGB = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)#更改图像类型
    try:
        print(os.path.join(outdir,os.path.basename(jpgfile)))#路径片段拼接，输出新的放置路径
        print(cv2.imwrite(os.path.join(outdir,os.path.basename(jpgfile)),src_RGB))#写入，输出成功与否
        
    except Exception as e:
        print(e)
        
for jpgfile in glob.glob(r'pic/*.jpg'):#设置遍历pic文件夹中所有jpg文件
    convertjpg(jpgfile,r'pic/1')#设置新的放置路径位置和文件种类
    #默认是从文件运行的文件夹中为相对路径，需要应用在其他地方的话需要修改为绝对路径，或者把这个文件丢那。
    
