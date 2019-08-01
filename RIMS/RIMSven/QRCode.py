import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import webbrowser

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
    _, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        data = obj.data
        print("Data", data)
        cv2.putText(frame, str(data), (50, 50), font, 2, (255, 0, 0), 3)
        key = cv2.waitKey(1)
        if(key == 32):
            i = 0
            while(i < 1):
                webbrowser.open_new(data)
                i = i + 1

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
#Reads the QR code and takes you to the website when you click the spacebar
#While loop so it only opens one instance of the website
