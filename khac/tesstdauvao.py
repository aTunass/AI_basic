import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('docs/data_linear.csv', header=None)
print(data)
# print(data.head(5))
print(data[0])
print(data[0:5])
# print(data[float(data[0]) > 60])

data = pd.read_csv('./data_linear.csv')
print(data)
# print(data.head(5))
data1 = data[data['Diện tích'] > 90]
print(data1)
print(data1[data1['Giá'] > 1400])
print(data.values)
print(data.values.T)

# Area = data.values[:,0]
# Cost = data.values[:,1]
# plt.plot(Area, Cost, 'ro')
# plt.axis([20, 110, 400, 1600])
# plt.xlabel('Diện tích (m2)')
# plt.ylabel('Giá (trieu vnd)')
# plt.show()


# Xem chiều dài của df, tương đương shape[0]
# print('Len:', len(data))
# # Xem thông tin dataframe vừa đọc được
# data.info()
# # Xem kích thước của dataframe
# print('Shape:', data.shape)