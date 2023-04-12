import cv2
import numpy as np

cap = cv2.VideoCapture('video/6.mp4')
#cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
  
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_green = np.array([35, 50, 151])
    upper_green = np.array([125, 255, 255])

   
    mask = cv2.inRange(hsv, lower_green, upper_green)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:
            cv2.drawContours(frame, [cnt], 0, (0, 255, 0), 2)

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #臉
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            if len(faces) > 0:
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(frame, 'PERSON', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # 綠色的東西
    cv2.imshow('GREEN', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
