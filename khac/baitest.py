import pandas as pd
import matplotlib.pyplot as plt
import cv2
import numpy as np

data = pd.read_csv('docs/data_linear.csv')
Area = data.values[:,0]
Cost = data.values[:,1]
plt.plot(Area, Cost, 'ro')
plt.axis([20, 110, 400, 1600])
plt.xlabel('Diện tích (m2)')
plt.ylabel('Giá (trieu vnd)')
plt.show()

img = cv2.imread('image/image.png')
mask = np.ones(img.shape[:2], np.uint8)*255
mask[0:272, 320:640] = 0
img_crop = cv2.bitwise_and(img, img, mask=mask)
img_crop = img[0:int(img.shape[0]/2), int(img.shape[1]/2):img.shape[1], :]
img_resize = cv2.resize(img, (320,272))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img, (5,5), sigmaX=5, sigmaY=1)
img_blur1 = cv2.GaussianBlur(img, (5,5), sigmaX=100, sigmaY=100)
img_canny = cv2.Canny(img_blur, 50, 100)

# cv2.imshow('img', img)
# cv2.imshow('img_crop', img_crop)
# cv2.imshow('img_resize', img_resize)
cv2.imshow('img_blur', img_blur)
cv2.imshow('img_blur1', img_blur1)

# cv2.imshow('img_canny', img_canny)
cv2.waitKey(0)