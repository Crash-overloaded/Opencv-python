#!/usr/bin/python3

import cv2
import time

# '0' is used to specify the use of built-in camera
# We can also give path to the video file instead of '0'
video = cv2.VideoCapture(0)
a=1
# check returns True if camera captures a image or vice-versa
# Whereas frame is a numpy array which represents the first image that video captures
while True:
	a+=1
	check , frame = video.read()
#print(check)
	print(frame)
# capturing video
	# Converting video frame to gray
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow('GrayVideo',gray)
	cv2.imshow('Normal',frame)
	# After every millisecond frame will change
	key=cv2.waitKey(1)
	if key == ord('q'):
		break

# releasing the camera in some milliseconds
print(a) # Printing no of frames
video.release()

cv2.destroyAllWindows()
