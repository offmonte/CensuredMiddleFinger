import cv2
from cvzone.HandTrackingModule import HandDetector

video = cv2.VideoCapture(0)

video.set(3,1280)
video.set(4,720)

detector = HandDetector()
cont = 0
while True:
    _,img = video.read()
    hands,img = detector.findHands(img)
    #bbox = hands['bbox']


    if hands:
        estado = detector.fingersUp(hands[0])
        #print(estado)

        if estado == [0,0,1,0,0] or estado == [1,0,1,0,0]:
            print('Middle Finger Up')
            
            print(cont)
            cont +=1
            #ix, iy, fx, fy = bbox[0],bbox[1],bbox[2],bbox[3]
            #cv2.circle(img,(ix, iy, fx, fy),15,(0,0,0),cv2.FILLED)

            

    cv2.imshow('img',cv2.resize(img,(640,420)))
    if cv2.waitKey(1)==27: #Fecha o programa ao apertar ESC
        break