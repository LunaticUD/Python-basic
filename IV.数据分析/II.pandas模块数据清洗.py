# Pandas清除空值
# dropna()语法
# DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
# axis：默认为 0，表示逢空值剔除整行，如果设置参数 axis＝1 表示逢空值去掉整列。
# how：默认为 'any' 如果一行（或一列）里任何一个数据有出现 NA 就去掉整行，如果设置 how='all' 一行（或列）都是 NA 才去掉这整行。
# thresh：设置需要多少非空值的数据才可以保留下来的。
# subset：设置想要检查的列。如果是多个列，可以使用列名的 list 作为参数。
# inplace：如果设置 True，将计算得到的值直接覆盖之前的值并返回 None，修改的是源数据。

# isnull() 判断各个单元格是否为空
import pandas as pd

# df = pd.read_csv("5.csv")
# print(df["Value"])
# print(df["Value"].isnull())
# 如果你要修改源数据 DataFrame, 可以使用 inplace = True 参数
# new_df = df.dropna()
# print(new_df.to_string())
# df.dropna(inplace=True)
# print(df.to_string())
# 移除 ST_NUM 列中字段值为空的行
# df = pd.read_csv("1.csv")
# df.dropna(subset=["Value"],inplace=True)
# print(df.to_string())
# 可以 fillna() 方法来替换一些空字段
# 使用 12345 替换空字段
# df = pd.read_csv("5.csv")
# df.fillna(12345,inplace=True)
# df["PID"].fillna(124,inplace=True)
# print(df.to_string())

# # mean()、median() 和 mode() 方法计算列的均值（所有值加起来的平均值）、中位数值（排序后排在中间的数）和众数（出现频率最高的数）
# miss_value = ["<0.1",""]
# df = pd.read_csv("1.csv",na_values=miss_value)
# df.dropna(subset=["Value"],inplace=True)
# average1 = df["Value"].mean()
# median2 = df["Value"].median()
# mode3 = df["Value"].mode()
# print(average1,"\n", median2, "\n", mode3)

# # Pandas 清洗格式错误数据
# # 第三个日期格式错误
# data = {
#   "Date": ['2020/12/01', '2020/12/02' , '20201226'],
#   "duration": [50, 40, 45]
# }
# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# df['Date'] = pd.to_datetime(df['Date'])
# print(df.to_string())

# # Pandas 清洗错误数据
# person = {
#   "name": ['Google', 'Runoob' , 'Taobao'],
#   "age": [50, 40, 12345]    # 12345 年龄数据是错误的
# }
# df = pd.DataFrame(person)
# df.loc[2, 'age'] = 30 # 修改数据
# print(df.to_string())
# person = {
#     "name": ['Google', 'Runoob', 'Taobao'],
#     "age": [50, 40, 12345]  # 12345 年龄数据是错误的
# }
# df = pd.DataFrame(person)
# for x in df.index:
#     if df.loc[x, "age"] > 120:
#         # 添加条件修改
#         # df.loc[x, "age"] = 60
#         # 添加条件删除一行
#         df.drop(x,inplace=True)
# print(df.to_string())

# # Pandas 清洗重复数据
# # 可以使用 duplicated() 和 drop_duplicates() 方法。
# # 对应的数据是重复的，duplicated() 会返回 True，否则返回 False。
# person = {
#   "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
#   "age": [50, 40, 40, 23]
# }
# df = pd.DataFrame(person)
# print(df.duplicated())
# df.drop_duplicates(inplace=True)
# print(df)