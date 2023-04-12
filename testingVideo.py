import cv2
import numpy as np

# 讀取影片檔案
cap = cv2.VideoCapture('video/6.mp4')

# 定義HSV中綠色的範圍
lower_green = np.array([35, 25, 151])
upper_green = np.array([124, 255, 255])


while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # 轉換顏色空間為HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 取出綠色範圍內的部分
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    res_green = cv2.bitwise_and(frame, frame, mask=mask_green)
    # 檢測是否有綠燈
    if cv2.countNonZero(mask_green) > 0 :
        print('green light is detected and person is present')

    cv2.imshow('frame', frame)
    cv2.imshow('GREEN', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()