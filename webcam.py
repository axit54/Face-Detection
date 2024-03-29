import cv2
import matplotlib.pyplot as plt
import numpy as np

cam = cv2.VideoCapture(0)
  
while True:
    ret_val, img = cam.read()
    # cv2.imshow('Webcam', img)
    haar_face_cascade = cv2.CascadeClassifier('/haarcascade_frontalface_alt.xml')
        grey=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #finding the faces
        faces = haar_face_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=5);  
        print('Faces found: ', len(faces))
        for (x, y, w, h) in faces:     
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2) 
            #roi_gray = gray[y:y+h, x:x+w]
            #roi_color = img[y:y+h, x:x+w]
        cv2.imshow('Webcam',img)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
  cv2.destroyAllWindows()