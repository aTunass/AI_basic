import cv2
import numpy as np

# read input image
img = cv2.imread('lane.jpg')
img = cv2.GaussianBlur(img, (3,3), cv2.BORDER_DEFAULT)
img = img[190:,:]
# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_yellow = np.array([15,50,180])
upper_yellow = np.array([40,255,255])

lower_green = np.array([128, 128, 128], dtype="uint8")
upper_green = np.array([200, 200, 200], dtype="uint8")

lower_white = np.array([200, 200, 200], dtype="uint8")
upper_white = np.array([255, 255, 255], dtype="uint8")

# Create a mask. Threshold the HSV image to get only yellow colors

# mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
mask = cv2.inRange(img, lower_green, upper_green)
# mask = cv2.inRange(img, lower_white, upper_white)
# Bitwise-AND mask and original image
result = cv2.bitwise_and(img,img, mask= mask)
img_canny = cv2.Canny(result, 50, 100)

# display the mask and masked image
cv2.imshow('Mask',hsv)
cv2.imshow('Masked Image',result)
cv2.imshow('Canny',img_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()