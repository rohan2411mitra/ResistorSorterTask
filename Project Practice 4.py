import cv2 as cv
import numpy as np
from datetime import datetime

capture=cv.VideoCapture(0, cv.CAP_DSHOW)

if (capture.isOpened() == False): 
    print("Error reading video file")

def click_event(event,x,y,flags,param):
    if event==cv.EVENT_RBUTTONDOWN:
        if x in range(300,341) and y in range(220,260):
            out.release()
            capture.release()
            cv.destroyAllWindows()
        

fourcc=cv.VideoWriter_fourcc(*"XVID")
out=cv.VideoWriter('output.avi',fourcc,20,(640,480))

record=False
box = False

start= datetime.now().second
while (capture.isOpened()):
    isTrue,frame=capture.read()   

    end=datetime.now().second
    if end==(start+5)%60:
        box=True
    
    if box:
        frame=cv.rectangle(frame,(300,220),(340,260),(0,0,255),-1)
        frame=cv.putText(frame,"Rohan",(300,260),cv.FONT_HERSHEY_COMPLEX,1,(255,0,0),1,cv.LINE_AA)

        cv.setMouseCallback('Video',click_event)

    cv.imshow('Video',frame)

    k=cv.waitKey(1)
    if k%256==114:
        record=True

    if record:
        out.write(frame)

    