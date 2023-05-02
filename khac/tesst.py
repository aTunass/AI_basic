import numpy as np  
import cv2
a = np.array([[[2, 4, 6], [3, 5, 7]], [[12, 14, 16], [13, 15, 17]], [[22, 24, 26], [23, 25, 27]]])  
print('a: ',a)
b=np.mean(a,axis=0, keepdims=False)  
c=np.mean(a,axis=1, keepdims=False)
d=np.mean(a,axis=2, keepdims=False)
print('b: ', b)
print('c: ', c)
print('d: ', d)
img = cv2.imread('foreround.png')
img = cv2.resize(img, (560, 280))
cv2.imwrite('foreground.jpg', img)