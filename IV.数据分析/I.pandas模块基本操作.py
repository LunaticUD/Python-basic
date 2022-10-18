import json

import pandas as pd

#
# # Pandas数据结构 - Series 类似表格中的一列，一维数组，可以保存任何类型
# # 语法
# # pandas.Series(Data,index,dtype,name,copy)
# # data一组数据
# # index 索引
# # dtype 数据类型
# # name 设置名称
# # copy 拷贝数据
# a = [7,8,9,10]
# mypandas1 = pd.Series(a)
# print(mypandas1)
# # 据索引进行取值
# print(mypandas1[3])
# # 指定索引和其他
# mypandas2 = pd.Series(a,index=["x","y","z","k"],dtype="int",name="mypandas")
# print(mypandas2["x"])
# # data为字典时key为索引，value为data
# mypandas3 = {1:"x",2:"y",3:"z"}
# print(pd.Series(mypandas3))
# # 转换为字典后需要那部分数据用索引获取
# print(pd.Series(mypandas3)[1])

# Pandas数据结构 - DataFrame相当于一个表格，是一个二维数据
# 语法
# pandas.DataFrame( data, index, columns, dtype, copy)
# data 数据
# index 行标签
# columns 列标签
# dtype 数据类型
# copy 拷贝数据
# # ▣列表创建
# mydataset1 = [["apple","10"],["bear","20"]]
# myvalue1 = pd.DataFrame(mydataset1,index=["x","y"],columns=["first","value"])
# print(myvalue1)
# #  ▣ndarrays创建
# mydataset2 = {
#   'sites': ["Google", "Runoob", "Wiki"],
#   'number': [1, 2, 3]
# }
# myvalue3 = pd.DataFrame(mydataset2)
# print(myvalue3)
# # ▣字典创建
# mydataset3 = [{"a": 1, "b": 2, "c": 3}, {"a": "x", "b": "y", "c": "z"}]
# myvalue3 = pd.DataFrame(mydataset3,index=["m","n"])     # 指定index的值
# myvalue4 = pd.DataFrame(mydataset3,index=["m","n"],columns=["v","b","s"])   # 指定columns值无法获取到数据
# print(myvalue3)
# print(myvalue4)
# # ▣用字典创建
# s = {
#     "col1":{"row1":1,"row2":2,"row3":3},
#     "col2":{"row1":"x","row2":"y","row3":"z"}
# }
# my = pd.DataFrame(s)
# print(my)
# # 用loc属性获取指定行数据
# print(myvalue3.loc["n"])    # 返回的是Series数据
# print(myvalue3.loc[["m","n"]])  # 返回的是DataFrame数据

# Pandas对CSV文件格式的处理
# # # 语法
# # df1 = pd.read_csv('nba.csv')    # 使用read_csv进行读取csv文件格式
# # print(df1.to_string())          # 使用to——string()输出DataFrame格式，不用输出前5行，后5行
# df1 = pd.read_csv("1.csv")
# print(df1)
# print(df1.to_string())
# # 使用to_csv()将DataFrame储存为csv文件
# mydataset = [{"a": 1, "b": 2, "c": 3}, {"a": "x", "b": "y", "c": "z"}]
# myvalue = pd.DataFrame(mydataset,index=["m","n"])
# print(myvalue)
# myvalue.to_csv("2.csv")
# 用head()属性读取头部几行，默认为5行
# myvalue = pd.read_csv("1.csv")
# # print(myvalue.head())
# # print(myvalue.head(12))
# # 用tail()属性读取尾部几行，默认为5行
# # print(myvalue.tail())
# # print(myvalue.tail(12))
# # 用info()属性打印出数据信息
# # print(myvalue.info())

# # Pandas对JSON文件格式的处理
# # 语法
# mydataset2 = pd.read_json("A.json")
# print(mydataset2.to_string())
# # 读取URL的json数据
# mydataset3 = pd.read_json("https://static.runoob.com/download/sites.json")
# print(mydataset3.to_string())

# df = pd.read_json("3.json")
# with open("3.json","r") as f1:
#     data = json.loads(f1.read())
# # json_normalize()方法解析内嵌json数据
# # record_path参数解析要解析的一列，meta参数显示要显示的一列
# data2 = pd.json_normalize(data,record_path="students",meta=["school_name","class"])
# print(data2)

# # 复杂实例
# # 使用 Python JSON 模块载入数据
# with open('4.json', 'r') as f:
#     data = json.loads(f.read())
#
# df = pd.json_normalize(
#     data,
#     record_path=['students'],
#     meta=[
#         'class',
#         ['info', 'president'],
#         ['info', 'contacts', 'tel']
#     ]
# )
#
# print(df)

# 对于复杂的套嵌要使用from glom import glom来获取
