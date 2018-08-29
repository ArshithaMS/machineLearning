#object detection using contours
import cv2

img=cv2.imread("image1.jpg")
cv2.imshow("Original",img)
cv2.waitKey(0)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.waitKey(0)

#Find Canny Edge
edged=cv2.Canny(gray,30,200)
cv2.imshow("Canny edged",edged)
cv2.waitKey(0)

#Finding Contours
_,contours,hierarchy=cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_
CV2.imshow("
