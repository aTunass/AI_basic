import cv2
import numpy as np
from non_max_supression import non_max_suppression
import matplotlib.pyplot as plt

img = cv2.imread('image/10bich.jpg')
img = cv2.resize(img, dsize=None, fx=0.5, fy=0.5) #Resize (dài rộng còn nửa )
imgOrigin = img.copy()
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread('image/bich.jpg', 0)
template = cv2.resize(template, dsize=None, fx=0.5, fy=0.5) #Resize (dài rộng còn nửa )
w, h = template.shape[1], template.shape[0]

res = cv2.matchTemplate(img_gray,template, cv2.TM_CCOEFF_NORMED)
THRESHOLD = 0.65
loc = np.where(res >= THRESHOLD)
print(loc)
#Draw boudning box
boundingBoxes = []
for y, x in zip(loc[0], loc[1]):
    cv2.rectangle(img, (x, y), (x + w, y + h), (200,200,20), 1)
    x1, y1, x2, y2 = x, y, x+w, y+h
    boundingBoxes.append((x1, y1, x2, y2))
#print(boundingBoxes)
boundingBoxes = [box for box in boundingBoxes]
boundingBoxes = np.array(boundingBoxes)
pick = non_max_suppression(boundingBoxes, 0.5)
for (startX, startY, endX, endY) in pick:
    imgOrigin = cv2.rectangle(imgOrigin, (startX, startY), (endX, endY), (0, 255, 0), 2)

# cv2.imshow('result', img)
# # cv2.imshow('result2', res)
# cv2.waitKey(0)
plt.figure(figsize=(16, 6))
plt.subplot(141),plt.imshow(img),plt.title('contour')
plt.subplot(142),plt.imshow(imgOrigin),plt.title('bounding box')
plt.show()