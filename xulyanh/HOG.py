import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage import feature
# img = plt.imread('image/foreround.png', cv2.IMREAD_UNCHANGED)
img = plt.imread('image/dibo.jpg', cv2.IMREAD_UNCHANGED)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print('image shape:', img.shape)
print('gray shape: ', gray.shape)

# Calculate gradient gx, gy
gx = cv2.Sobel(gray, cv2.CV_32F, dx=0, dy=1, ksize=3)
gy = cv2.Sobel(gray, cv2.CV_32F, dx=1, dy=0, ksize=3)

print('gray shape: {}'.format(gray.shape))
print('gx shape: {}'.format(gx.shape))
print('gy shape: {}'.format(gy.shape))

g, theta = cv2.cartToPolar(gx, gy, angleInDegrees=True) #g la do lon gradient, theta la phuong gradient
print('gradient format: {}'.format(g.shape))
print('theta format: {}'.format(theta.shape))


plt.figure(figsize = (16, 8))
plt.subplot(1, 6, 1)
plt.imshow(img)
plt.title('Original Image')
plt.subplot(1, 6, 2)
plt.imshow(gray)
plt.title('Gray Image')

plt.subplot(1, 6, 3)
plt.title('gradient of x')
plt.imshow(gx)

plt.subplot(1, 6, 4)
plt.title('gradient of y')
plt.imshow(gy)

plt.subplot(1, 6, 5)
plt.title('Magnitute of gradient')
plt.imshow(g)

plt.subplot(1, 6, 6)
plt.title('Direction of gradient')
plt.imshow(theta)
plt.show()
