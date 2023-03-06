import cv2
import numpy as np
from numpy import array, uint8

def Sobel_edge_detection(f):
    cv2.threshold(img,dst=img,*(89,255,0))

    grad_x = cv2.Sobel(f, cv2.CV_32F, 1, 0, ksize = 3)
    grad_y = cv2.Sobel(f, cv2.CV_32F, 0, 1, ksize = 3)
    magnitude = abs(grad_x) + abs(grad_y)
    g = np.uint8(np.clip(magnitude, 0, 255))
    ret, g = cv2.threshold(g, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return img

if __name__ == '__main__' :

    img = cv2.imread("img/BalaenicepsRex/2.jpg",-1)
    cv2.imshow("original", img)
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img2 = Sobel_edge_detection(img1)
    cv2.imshow("grey", img1)
    cv2.imshow("After", img2)
    cv2.waitKey()
    cv2.destroyAllWindows()

    cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    cv2.waitKey(0)
    cv2.destroyAllWindows()