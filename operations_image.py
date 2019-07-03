import cv2

# Colored Image
img = cv2.imread("penguin.jpg",1)
print(img[0])
# grayscale Image
#img1 = cv2.imread("penguin.jpg",0)
# Resizing image
# Resize take image name ,(columns,rows)
# Resizing the image to half
resized_img1=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
# Now resizing it to double
resized_img2=cv2.resize(img,(int(img.shape[1]*2),int(img.shape[0]*2)))
#Displaying image
cv2.imshow("Penguins",resized_img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
