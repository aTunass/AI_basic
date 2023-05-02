from __future__ import print_function
# from imutils.object_detection import non_max_suppression
from non_max_supression import non_max_suppression
# from new_nms import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
import matplotlib.pyplot as plt

 
# Khởi tạo một bộ mô tả đặc trưng HOG
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
img = plt.imread('image/dibo.jpg', cv2.IMREAD_UNCHANGED)
# img = img[:1000,:]
# img = cv2.imread('image/foreround.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgcop = img.copy()
print(img.shape)
(rects, weights) = hog.detectMultiScale(img = img, winStride = (8, 8),
                                               padding = (8, 8), scale = 1.02)
# print(rects)
rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
print(type(rects))
# pick = non_max_suppression(rects, probs = None, overlapThresh=0.8)
pick = non_max_suppression(rects, overlapThresh=0.8)
print(pick.shape)
for (startX, startY, endX, endY) in pick:
    img_out = cv2.rectangle(imgcop, (startX, startY), (endX, endY), (0, 255, 0), 2)
plt.imshow(img_out)
plt.show()