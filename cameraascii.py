import numpy
import cv2
import sys


cap = cv2.VideoCapture(0)
display = ''

if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    #cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break


    for i in range(48):
        for j in range(64):
            if(frame[i*5][j*5][1]>220):
                display += '##'
            elif(frame[i*5][j*5][1]>200):
                display += '++'
            elif(frame[i*5][j*5][1]>150):
                display += '..'
            elif(frame[i*5][j*5][1]>100):
                display += ' .'
                
            else:
                display += '  '
        display += '\n'
    print(display)
    display = ''

cap.release()
cv2.destroyAllWindows()