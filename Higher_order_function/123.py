#  coding = utf-8 

# @Time : 2022/10/11 23:47
# @Author : HJH
# @File : 123.py
# @Software: PyCharm

import pandas as pd
import numpy as np
from pandas import DataFrame, Series

# obj1 = Series([1, 2, 3, 4])
# print(obj1)
# print(obj1.values)
# print(obj1.index)
#
# obj2 = Series(['1', '2', '3', '4', '5'], index=[1, 2, 3, 4, 5])
#
# # 当做字典
# data = {'a': 100, 'b': 200, 'c': 300}
# obj3 = Series(data)
# print(obj3)
# key = ['a', 'c']
# obj4 = Series(data, index=key)
# print(obj4)
#
# # 缺失值处理
# data = {'a': None, 'b': 200, 'c': 300}
# obj5 = Series(data)
# print(obj5)
# print(pd.isnull(obj5))
#
# #对象命名，索引命名
# data = {'lilei':None,'hanmeimei':18,'tony':12,'Jack':8}
# obj6 = Series(data)
# obj6.name = 'NameAndAge'
# obj6.index.name = 'xingming'
# print(obj6)


# DataFrame


# dates = pd.date_range('20221012', periods=6)
# print(dates)
#
# df = pd.DataFrame(np.random.rand(6, 4), index=dates, columns=list('ABCD'))
# print(df)
#
# print(df.T)
#
# print(df['20221012':'20221014'])  # 左闭右闭
#
# print(df.loc['20221012':'20221014', ['A', 'B']])
#
# print(df.head(2))
#
# print(df.tail(3))
#
# # 重新索引reindex
# obj = Series([4.5, -9.3, 112], index=['a', 'b', 'c'])
# print(obj)
# obj1 = obj.reindex(['a', 'b', 'c', 'd'])
# print(obj1)
# obj2 = obj.reindex(['a', 'b', 'c', 'd'], fill_value=1)
# print(obj2)

# 层次化索引
data = Series(np.random.rand(10),
              index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'], [1, 2, 3, 4, 5, 6, 7, 8, 1, 2]])
print(data)
print(data.index)

#读取文件数据
frame_data = pd.read_csv('data1.csv')

excel_data = pd.read_excel('data2.xlsx',sheet_name='sheet2')
