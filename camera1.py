import cv2
import numpy as np
lower = np.array([35,43,46])
upper = np.array([77,255,255])

lower_green = np.array([50, 43, 46])
upper_green = np.array([80, 255, 255])

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img,(1366,768))
    output = cv2.inRange(img, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
    output = cv2.dilate(output, kernel)
    output = cv2.erode(output, kernel)
    contours, hierarchy = cv2.findContours(output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

    for contour in contours:
        area = cv2.contourArea(contour)
        color = (0,255,0)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)

    blue_output = cv2.inRange(img, lower_green, upper_green)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
    blue_output = cv2.dilate(blue_output, kernel)
    blue_output = cv2.erode(blue_output, kernel)
    contours, hierarchy = cv2.findContours(blue_output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        color = (0,255,0)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)

    cv2.imshow('oxxostudio', img)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()