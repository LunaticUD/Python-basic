# LunaticUD on Sun Oct  2 10:24:35 2022
# TODO1:
import numpy as np
# Numpy版本
print(np.__version__)
# np? 获取文档
# np.<Tab> 获取所有用法
# TODO2
import array
# 创建同一类型的密集数组
L = [1,2,3,4,5,6,7,8]
A = array.array('i',L)
B = array.array('b',L)
C = array.array('B',L)
print(A,B,C) 
# TODO3
import numpy as np
# 创建数组
print(np.array([1,2,3,4,5]))
print(np.array([1,2,3,4,5]))
print(np.array(['1',2,3,4,5]))
print(np.array([1,2,3,4,'5']))
# 明确设置数组的数据类型
print(np.array([1.0,2,3,4,5],dtype='int'))
# 多维数组
print(np.array([[1,2,3],[4,5,6],[7,8,9]]))
# TODO4
# 从头创建数组
import numpy as np
# 创建一个长度为10的数组，数组的值都是0
print(np.zeros(10,dtype=int))
# 创建一个3*5的浮点型数组，数组的值都是1
print(np.ones((3,5),dtype=int))
# 创建一个3*5的浮点型数组，数组的值都是3.14
print(np.full((3,5),3.14))
print(np.full((3,5),1))
print(np.full((3,5),'2'))
# 创建一个3*5的浮点型数组，数组的值是一个线性序列
# 与range()类似，0-20且2为步长
print(np.arange(0,20,2))
# 创建一个5个元素的数组，数组的值均匀的分配到0-1/0-50
print(np.linspace(0,1,5))
print(np.linspace(0,50,5))
# 创建一个3*3的0-1均匀分布的随机数组
print(np.random.random((3,3)))
print(np.random.random((3,4)))
# 创建一个3*3的均值为0、方差为1的正态分布的随机数数组
print(np.random.normal(0,1,(3,4)))
print(np.random.normal(0,2,(3,4)))
# 创建一个3*3的[0,10)区间的随机整数数组
print(np.random.randint(0,10,(3,3)))
# 创建一个3*3的单位矩阵
print(np.eye(3))
print(np.eye(5))
# 创建一个由3个整型数组的成的未初始化的数组
# 数组的值是内存中任意值
print(np.empty(5))





















