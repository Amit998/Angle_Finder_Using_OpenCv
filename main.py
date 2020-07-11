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


def gradient(p1,p2):
    return ((p2[1]-p1[1])/(p2[0]-p1[0]))



def getAngel(pointsList):
    point1,point2,point3=  pointsList[-3:]
    m1=gradient(point1,point2)
    m2=gradient(point1,point3)
    angel=math.atan((m2-m1)/(1+m1*m2))
    print(round(math.degrees(angel)))


while True:

    if(len(pointsList) % 3 == 0 and len(pointsList) !=0):
        getAngel(pointsList)
    cv2.imshow('image',img)
    cv2.setMouseCallback('image',mousePoints)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        pointsList=[]
        img=cv2.imread(path)