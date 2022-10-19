# LunaticUD on Sun Oct  2 10:24:35 2022
import numpy as np

# TODO4 数组的变形
# 将1-9放入3x3的矩阵中
grid = np.arange(1,10).reshape((3,3))
print(grid)
# grid1 = np.arange(1,10).reshape((3,4))
# print(grid1)    # 报错
# 获取行
x = np.arange(1,10)
print(x[np.newaxis,:])
print(x.reshape(1,9))
# 获取列
print(x[:,np.newaxis])
print(x.reshape(9,1))
print(x.reshape(9,1).ndim)
# TODO5 数组拼接和分裂
# 数组拼接
x = np.arange(1,4)
y = np.arange(4,7)
print(np.concatenate([x,y]))
x1 = [[1,2,3],[4,5,6]]
y1 = [[4,5,6],[7,8,9]]
# 第一轴
print('concatenate',np.concatenate([x1,y1]))
print('vstack',np.vstack([x1,y1]))
# 第二轴
print('concatenate',np.concatenate([x1,y1],axis=1))
print('hstack',np.hstack([x1,y1]))
# np.dstack()用于第三个维度划分
# 数组分裂
x = np.arange(1,16).reshape(3,5)
y = [0,1,2,3,4,5,6,7,8,9]
print(np.split(y,[2,6]))
print(np.split(x,[1,2]))
print(np.hsplit(x,[1]))
print(np.vsplit(x,[1]))
# np.dsplit()用于第三个维度划分



















