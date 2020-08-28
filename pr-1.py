#!/usr/bin/python3

import pytesseract
import pyttsx3
import cv2
#import os
#espeak from import espeak
#import sys

# reading image
img = cv2.imread("test4.png")
#img1 = cv2.multiply(img, 1.2)
bw = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
'''
#cleaning white image
ret,thresh = cv2.threshold(bw,145,255,cv2.THRESH_BINARY)
#adapt_thresh = cv2.adaptiveThreshold(bw,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
'''
#cleaning black image 
th,dst = cv2.threshold(bw,50,255,cv2.THRESH_BINARY_INV) 

#cv2.imshow("adaptive",adapt_thresh)
cv2.imshow("thresholded",dst)
#cv2.imshow("original",img)
#cv2.imshow("b/w",bw)

cv2.waitKey(0)
cv2.destroyAllWindows()

config = ('-l eng --oem 1 --psm 3')
#converting image text to string
text = pytesseract.image_to_string(dst, config=config)
#printing the extracted text
print (text)


'''
#say the text from image
engine=pyttsx3.init()
engine.say(text)
engine.runAndWait()
'''
'''
a=text.decode('utf-8')
#a = text.split(' ')
espeak.synth(a)
li = text.split(' ')
#print type(li)
for i in li:
	#print li
	#print i
	#print i.decode('utf-8')
	espeak.synth(i)
'''
