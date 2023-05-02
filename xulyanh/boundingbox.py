import numpy as np
import cv2
import matplotlib.pyplot as plt
from non_max_supression import non_max_suppression
def contour(img):
    # img = cv2.imread(img)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 50)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
    return img

img= cv2.imread('image/10bich.jpg')
img = cv2.resize(img, dsize=None, fx=0.5, fy=0.5)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Chuyển đổi sang ảnh gray
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 40)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
imgcontour = img.copy()
imgbound = img.copy()
imgboundNMS = img.copy()
imgminbound = img.copy()
img_contour = cv2.drawContours(imgcontour, contours, -1, (0, 255, 0), 2)
# Tìm ra diện tích của toàn bộ các contours
area_cnt = [cv2.contourArea(cnt) for cnt in contours]
area_sort = np.argsort(area_cnt)[::-1]
# Top 5 contour có diện tích lớn nhất
# print(area_sort[2:10])
print(area_sort.size)
# Vẽ bounding box cho contours có diện tích lớn thứ 2
"""ta sẽ xác định tọa độ góc trên bên trái và độ dài cạnh width, height của contour thông qua hàm cv2.boundingRect(). 
Từ đó vẽ bounding box hình chữ nhật đứng lên hình ảnh gốc bằng cách sử dụng hàm cv.rectangle() """
cnt = contours[area_sort[10]]
(x,y),(MA,ma),angle = cv2.fitEllipse(cnt)
print('Angle of Orientation: {}'.format(angle))


boundingBoxes = []
for i in range(3,area_sort.size):
    cnt = contours[area_sort[i]]
    x,y,w,h = cv2.boundingRect(cnt)
    x1, y1, x2, y2 = x, y, x+w, y+h
    boundingBoxes.append((x1, y1, x2, y2))
    # print('centroid: ({}, {}), (width, height): ({}, {})'.format(x, y, w, h))
    img_bound = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    #MIN bounding
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    img_min_bound = cv2.drawContours(imgminbound,[box],0,(100,100,100),2)

boundingBoxes = [box for box in boundingBoxes]
boundingBoxes = np.array(boundingBoxes)
pick = non_max_suppression(boundingBoxes, 0.5)
for (startX, startY, endX, endY) in pick:
    img_bound_NMS = cv2.rectangle(imgboundNMS, (startX, startY), (endX, endY), (0, 255, 0), 2)
# cv2.imshow('test', img)
# cv2.waitKey(0)
plt.figure(figsize=(16, 6))
plt.subplot(141),plt.imshow(img_contour),plt.title('contour')
plt.subplot(142),plt.imshow(img_bound),plt.title('bounding box')
plt.subplot(143),plt.imshow(img_min_bound),plt.title('min boundingbox')
plt.subplot(143),plt.imshow(img_bound_NMS),plt.title('NMS boundingbox')
plt.show()