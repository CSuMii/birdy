import cv2
import numpy as np

img = cv2.imread('img/3.jpg')
frame = img
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
frame = cv2.resize(frame,(1366,766))


lower_green = np.array([35, 43, 46])
upper_green = np.array([76, 255, 255])
mask = cv2.inRange(hsv, lower_green, upper_green)
res = cv2.bitwise_and(img, img, mask=mask)
cv2.rectangle(res, (310,320), (370,365), (0,255, 0), 2) 

cv2.imshow('Input', img)
cv2.imshow('Result', res)
cv2.waitKey(0)