# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 01:35:27 2017

@author: Leifei
"""



import cv2
import numpy as np

def get_dist():
    img =  cv2.imread('1.png')
    img = cv2.resize(img, (288, 512), fx=0,  fy =0, interpolation = cv2.INTER_CUBIC)
    img = img[100:450, 20:275]
    img_hsv =  cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    
    ## 用颜色信息找到小人
    purple = [(180,133,138), (86,40,46)]
    lower = np.array(purple[1], dtype = "uint8")
    upper = np.array(purple[0], dtype = "uint8")
    
    mask = cv2.inRange(img_hsv, lower, upper)  
    output = cv2.bitwise_and(img_hsv, img_hsv, mask = mask)  
    
    output_gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    ret, output_bw = cv2.threshold(output_gray,40,255,cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    output_opened = cv2.morphologyEx(output_bw, cv2.MORPH_OPEN, kernel)  
    
    ys = np.zeros((output_opened.shape[0],1))
    for i in range(len(ys)):
        ys[i] = output_opened[i,:].sum()
   
    ys[ ys> 0] = 1
    ys_item = np.argwhere(ys == 1)
    person_y = ys_item[-1][0] - (ys_item[-1][0] - ys_item[0][0])/9
    
    xs = np.zeros((output_opened.shape[1],1))
    for i in range(len(xs)):
        xs[i] = output_opened[:,i].sum()
    
    xs[xs >0 ] = 1
    xs_item = np.argwhere(xs == 1)
    person_x = int((xs_item[0] + xs_item[-1] )[0]/2)
    
    person_cor = (person_x, person_y)  
    
    ##为了防止小人比目的砖块还高，将小人的人头填充成背景颜色
    bg_color = img[person_x, ys_item[0][0] - 100, :]
    img[ ys_item[0][0]: (ys_item[0][0]+30),xs_item[0][0]:xs_item[-1][0]] = bg_color
    
    
    ##通过最高点的位置找到目的砖块
    bg_color_h = img_hsv[0,0,:][0]
    if bg_color_h < 40 or bg_color_h > 156:
        edges = cv2.Canny(img[:,:,0],10,100)
    else:
        edges = cv2.Canny(img[:,:,2],10,100)

    
    cols = np.zeros((edges.shape[0],1))
    for i in range(len(cols)):
       cols[i] = edges[i,:].sum()
    
    cols[cols > 0 ] = 1
    cols_item = np.argwhere( cols == 1)
    clr_y = cols_item[0][0] + 25
    clr_x_items = np.argwhere(edges[cols_item[0][0]] == 255)
    clr_x = int((clr_x_items[0] + clr_x_items[-1])[0] /2)

    dst_cor = (clr_x, clr_y)
    
    dist = np.sqrt( np.square((person_cor[0] - dst_cor[0])) + np.square((person_cor[1] - dst_cor[1])) )
    
    return dist

    
## 两个系数是不同的尝试结果估计得到的
def dist2time(d):
    return 0.005*d + 0.035
    


