import cv2
import numpy as np

device=cv2.VideoCapture(0) # huse if give comple blue130-180,after that mix is called saturation,value is intensity of that color
while True:
    #Take each frame
    ret,frame=device.read()

    #cvt BGR to hsv
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #Define range of blue color
    lower_range=np.array([110,50,50])
    upper_range = np.array([130, 255, 255])
    #
    lower_range_red=np.array([150,70,30])
    upper_range_red=np.array([180,255,150])

    #Threshold the HSV image to get only blue color
    mask1=cv2.inRange(hsv,lower_range,upper_range)
    mask2=cv2.inRange(hsv,lower_range_red,upper_range_red)

    #bitwise_and mask and orignal image
    res=cv2.bitwise_and(frame,frame,mask=mask1)
    res1=cv2.bitwise_and(frame,frame,mask=mask2)

    #cv2.imshow('show',mask)
    cv2.imshow('show1',frame)
    cv2.imshow('Res',res)
    cv2.imshow('res1',res1)
    if cv2.waitKey(1)==13: #
        break
device.release()
cv2.destroyAllWindows()
