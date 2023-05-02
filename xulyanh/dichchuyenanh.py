import numpy as np
import cv2
import matplotlib.pyplot as plt
img= cv2.imread('image/test.jpg')
# cv2.imshow('tesst',img)
# cv2.waitKey(0)
rows, cols = img.shape[:2]
print(img.shape)
# Dịch chuyển hình ảnh xuống góc dưới bên phải
tx, ty = (50, 50)
M1 = np.array([[1, 0, tx], 
              [0, 1, ty]], dtype=np.float32)
tran1 = cv2.warpAffine(img, M1, (cols, rows))

# Dịch chuyển hình ảnh xuống góc dưới bên trái
M2 = np.array([[1, 0, -tx], 
              [0, 1, ty]], dtype=np.float32)
tran2 = cv2.warpAffine(img, M2, (cols, rows))

# Dịch chuyển hình ảnh xuống góc dưới bên trái
M3 = np.array([[1, 0, tx], 
              [0, 1, -ty]], dtype=np.float32)
tran3 = cv2.warpAffine(img, M3, (cols, rows))

# Dịch chuyển hình ảnh xuống góc dưới bên trái
M4 = np.array([[1, 0, -tx], 
              [0, 1, -ty]], dtype=np.float32)
tran4 = cv2.warpAffine(img, M4, (cols, rows))

plt.figure(figsize=(16, 4))
plt.subplot(151),plt.imshow(img),plt.title('Origin Image')
imgplot = plt.imshow(img)
plt.subplot(152),plt.imshow(tran1),plt.title('Translate to Bottom Right')
plt.subplot(153),plt.imshow(tran2),plt.title('Translate to Bottom Left')
plt.subplot(154),plt.imshow(tran3),plt.title('Translate to Up Right')
plt.subplot(155),plt.imshow(tran4),plt.title('Translate to Up Left')
plt.show()