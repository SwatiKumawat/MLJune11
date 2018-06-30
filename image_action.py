#!/usr/bin/python2

import cv2

#reading image
img=cv2.imread("dog.jpeg")

#making a line in image
cv2.line(img,(0,0),(50,170),(255,0,0),2)
#making a reactangle in image
cv2.rectangle(img,(15,25),(180,170),(255,0,0),2)
#making circle in image
cv2.circle(img,(100,80),10,(20,40,60),2)

#showing image
cv2.imshow("dog",img)

#saving the image
cv2.imwrite("dogline.jpeg",img)

#holding the window 
cv2.waitKey(0)
cv2.destroyAllWindows()
