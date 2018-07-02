#!/usr/bin/python2

import cv2

# start the web camera
capture = cv2.VideoCapture(0)

#if camera is working print
if capture.isOpened() :
	print "camera is ready to take pic"

# if not print this
else :
	print  "check your camera drivers"

#current camera data after frame take status
status,frame = capture.read()
cv2.imshow("frame1",frame)

#hold the image  window 
cv2.waitKey(0)
capture.release()


