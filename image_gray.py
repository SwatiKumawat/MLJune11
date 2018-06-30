#!/usr/bin/python2

import cv2
#taking original image
img=cv2.imread("dog.jpeg")

#cnverting to black and white
img1=cv2.imread("dog.jpeg",0)

#converting to transparent
img2=cv2.imread("dog.jpeg",-1)

#converting to gray
img3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#showing all the images
cv2.imshow("original",img)
cv2.imshow("b/w",img1)
cv2.imshow("transparent",img2)
cv2.imshow("bgr2gray",img3)

#holding the image window
cv2.waitKey(0)
cv2.destroyAllWindows
