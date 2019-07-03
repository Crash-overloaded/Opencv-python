#!/usr/bin/python3

import cv2

# Create a CascadeClassifier Object
# Mentioned is the path the XML file which contains face features
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Reading the image as it is

img=cv2.imread("face.jpg")

# Reading the image as grey scale image

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Search the co-ordinates of the image
# Detect multiscale is a method to search for the face rectangle co-ordinates
faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)
# Scale Factor decreases the shape value by 5% until the face is found
# Smaller the value , Greater the accuracy
#print(type(faces))
#print(faces)

# Printing rectangle on face
# (x,y)--> starting co-ordinate
# (x+w,y+h) --> ending co-ordinate
for x,y,w,h in faces:
	img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
resized=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Gray",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
