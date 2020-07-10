import cv2
import math

path ='test.jpg'
img=cv2.imread(path)

pointsList=[]

def mousePoints(event,x,y,flags,params):
    if(event == cv2.EVENT_LBUTTONDOWN):
        cv2.circle(img,(x,y),5,(0,0,255),cv2.FILLED)
        pointsList.append([x,y])
        print(pointsList)

while True:
    cv2.imshow('image',img)
    cv2.setMouseCallback('image',mousePoints)
    if(cv2.waitKey(1) and 0xFF ==ord('q')):
        pointsList=[]
        img=cv2.imread(path)