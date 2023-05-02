import numpy as np

#khai bao 2 vecto
a = np.array([1, 2 ,3])
b = np.array([4, 5 ,6])
print('nhan hai vecto:', np.dot(a,b))

#MA TRAN
A = np.array([[1, 2, 3],[5, 1, 1],[3, 2, 1],[1, 1, 1]])
B = np.array([[4, 2, 1, 4],[5, 5, 1, 7],[1, 2, 1, 4]])
C = np.array([[4, 1, 4],[5, 1, 7],[2, 1, 4]])
print('tich hai ma tran A va B: \n', np.dot(A,B))
print('ma tran chuyen vi cua A: \n', np.transpose(A))
print('ma tran chuyen vi cua B: \n', B.T)
print('Dinh thuc ma tran C: ', np.linalg.det(C))
print('hang cua ma tran A: ',np.linalg.matrix_rank(A))

# He phuong trinh

X = np.array([[2,2,3], [4,5,6], [7,8,9]])
Y = np.array([14,32,50])
print('nghiem he phuong trinh la: ', np.linalg.solve(X, Y))