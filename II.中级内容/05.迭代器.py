# 迭代器
# 序列包括列表、元组、集合、字典和字符串
# 列表、元组、字符串都可以通过索引的形式进行循环
# 集合、字典则不可以通过索引的形式进行循环
# dir()函数查看某些数据类型可以执行哪些操作
# print(dir(str))         # 存在'__iter__'
# print(dir(list))        # 存在'__iter__'
# print(dir(dict))        # 存在'__iter__'
# print(dir(int))         # 不存在'__iter__'
# print(dir(bool))        # 不存在'__iter__'

# # __iter__是可迭代的含义，iterable可迭代对象
# lit = ["你好","好不好"]
# it = lit.__iter__()
# # print(dir(it))                 # 通过__iter__获得iterator迭代器 存在__next__函数
# # 而可迭代对象中的每一个函数由__next__函数来访问，并且只能向下，不会倒退。
# its = it.__next__()
# print(its)
# its = it.__next__()
# print(its)
# its = it.__next__()
# print(its)                      # 没有了对象便会返回StopIteration错误。
# # 使用步骤
# # 1.序列通过__iter__函数获得迭代器
# # 2.迭代器通过__next__函数返回序列中的对象
# # 3.反复的执行第二步，直到报错StopIteration
# a = {"你好","你不好"}
# it = a.__iter__()
# print(it.__next__())
# print(it.__next__())
# it = a.__iter__()               # 🈲此时要想再次获取数据，必须重新获得迭代器，否则会报错StopIteration
# print(it.__next__())
# print(it.__next__())

# print(a.__iter__().__next__())
# print(a.__iter__().__next__())  # 🈲it与a__iter___的关系并不等与数学上的等价，所获得都是第一个值

# it = iter(a)
# print(next(it))                 # 此时的iter=__iter__
# print(next(it))                 # 此时的next=__next__

# 列表不是迭代器
# 迭代器本身是一个可迭代的对象，可以进行for循环

# # for循环的工作机制
# lit = ["a","s","d"]
# # for 的正常工作方式
# # for i in lit:
# #     print(i)            
# # for 的内部工作机制
# it = lit.__iter__()             # 获取迭代器
# while True:                     # 进行死循环，不断的尝试获取到序列中的值直到捕捉到StopIteration 错误，停止循环
#     try:
#         obj = it.__next__()
#         print(obj)
#     except StopIteration:
#         break

# 迭代器的特点
# 节省内存
# 存在惰性机制
# 不能反复只能向下执行
