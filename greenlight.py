import cv2
import numpy as np

cap = cv2.VideoCapture('video/1.mp4')
while True:
    ret,frame = cap.read()
    if ret == False:
        break
    frame = cv2.resize(frame,(1366,768))
    #擷取roi區域
    roiColor = frame[35:80,800:1100]
    #轉換hsv顏色空間
    hsv = cv2.cvtColor(roiColor,cv2.COLOR_BGR2HSV)

    #red
    lower_hsv_red = np.array([157,177,122])
    upper_hsv_red = np.array([179,255,255])
    mask_red = cv2.inRange(hsv,lowerb=lower_hsv_red,upperb=upper_hsv_red)
    #中值濾波
    red_blur = cv2.medianBlur(mask_red, 7)
    #green
    lower_hsv_green = np.array([50,79,137])
    upper_hsv_green = np.array([80,255,255])
    mask_green = cv2.inRange(hsv,lowerb=lower_hsv_green,upperb=upper_hsv_green)
    #中值濾波
    green_blur = cv2.medianBlur(mask_green, 7)

    #因為影象是二值的影象，所以如果影象出現白點，也就是255，那麼就取他的max最大值255
    red_color = np.max(red_blur)
    green_color = np.max(green_blur)
    #在red_color中判斷二值影象如果數值等於255，那麼就判定為red
    if red_color == 255:
        print('red')
                        #。。。這是我經常會混淆的座標。。。 就列舉出來記一下。。。
                        #      y  y+h x  x+w
                        #frame[50:90,950:1100]

                        #     x   y    x+w  y+h
        cv2.rectangle(frame,(1020,50),(1060,90),(0,0,255),2) #按座標畫出矩形框
        cv2.putText(frame, "red", (1020, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255),2)#顯示red文字資訊
    #在green_color中判斷二值影象如果數值等於255，那麼就判定為green
    elif green_color == 255:
        print('green')
        cv2.rectangle(frame,(100,470),(270,570),(0,255,0),2)
        cv2.rectangle(frame,(770,500),(960,600),(0,255,0),2)
        cv2.putText(frame, "green", (1020, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0),2)

    cv2.imshow('frame',frame)
    red_blur = cv2.resize(red_blur,(300,200))
    green_blur = cv2.resize(green_blur,(300,200))
    cv2.imshow('red_window',red_blur)
    cv2.imshow('green_window',green_blur)

    c = cv2.waitKey(10)
    if c==27:
        break