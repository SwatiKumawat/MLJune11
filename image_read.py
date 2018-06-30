#!/usr/bin/python

import cv2

#reading the image
img=cv2.imread("dog.jpeg")

#shows the height and width of image
print img.shape

#shows the image
cv2.imshow("dogg",img)

#holding the image
cv2.waitKey(0)

#waitkey will be destroyed using q 
cv2.destroyAllWindows()

