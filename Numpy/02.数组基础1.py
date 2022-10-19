# LunaticUD on Sun Oct  2 10:24:35 2022
import numpy as np

# TODO1 数组属性
np.random.seed(0)   # 设置随机种子
x1 = np.random.randint(10,size=6)
x2 = np.random.randint(10,size=(3,4))
x3 = np.random.randint(10,size=(3,4,5))
# 维度
print(x1.ndim)
print(x2.ndim)
print(x3.ndim)
# 维度大小
print(x1.shape)
print(x2.shape)
print(x3.shape)
# 数组的总大小
print(x1.size)
print(x2.size)
print(x3.size)
# 数组的类型
print(x1.dtype)
print(x2.dtype)
print(x3.dtype)
# 每个数组元素字节大小
print(x1.itemsize)
print(x2.itemsize)
print(x3.itemsize)
# 数组总字节大小
print(x1.nbytes)
print(x2.nbytes)
print(x3.nbytes)
# TODO2 数组索引——获取单个元素
# 同列表
# 获取值
np.random.seed(0)
x = np.random.randint(10,size=(3,4))
print("两种方式获取相同：",x[0][0]==x[0,0])
# 修改值
x[0][0] = 12
print(x)
# ✔唯一不同的是列表可以接受不同的类型，但数组只能是同种类型的
x[0][0] = 3.1415926
print(x)    # 3.1415926被自动截断成整型
# TODO3 数组切片
# 一维数组——同列表
np.random.seed(0)
x = np.random.randint(10,size=10)
x1 = [5,0,3,3,7,9,3,5,2,4]
print(x[5::-2])
print(x1[5::-2])
# 多维数组
np.random.seed(0)
x = np.random.randint(10,size=(3,6))
print(x)
print(x[:2,:5])
print(x[::-1,::-1])
# 获取行和列
np.random.seed(0)
x = np.random.randint(10,size=(3,6))
print(x)
print(x[:,0])   # 第一列
print(x[0,:])   # 第一行
print(x[0,:]==x[0])
# 不是副本是视图
np.random.seed(0)
x = np.random.randint(10,size=10)
x1 = [5,0,3,3,7,9,3,5,2,4]
x[::-1]
x1[::-1]
print(x1)
print(x)
# 创建副本
np.random.seed(0)
x = np.random.randint(10,size=10)
x1 = x[::-1]
print(x)
print(x1)




















