#  coding = utf-8 

# @Time : 2022/10/10 9:47
# @Author : HJH
# @File : lambda.py
# @Software: PyCharm


# 匿名函数
# 格式 lambda 参数列表：表达式

add_lambda = lambda x, y: x + y

# 三元运算符

condition = False
print(1 if condition else 2)

# map函数应用

list1 = [1, 2, 3, 4, 5]
print(list(map(lambda x: x + x, list1)))

print(list(map(lambda x, y: x * x + y, [1, 2, 3], [4, 5, 6])))


# filter 过滤器
def is_not_none(s):
    return s and len(s.strip()) > 0


print(list(filter(is_not_none, [' ', '', 'hello'])))

# reduce 对参数序列中元素进行累积
# 先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
from functools import reduce

f = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 10)

print(f)

# 三大推导式

# 列表推导式
list1 = [1, 2, 3, 4, 5]
list2 = [i + i for i in list1]
print(list1, '\n', list2)
list3 = [i + i for i in list1 if i > 2]
print(list3)

# 集合推导式
#  [] 变{}


# 字典推导式
d = {'zs': 20, 'ls': 25, 'ww': 30}

s_key = [key + 'aaa' for key, value in d.items()]
print(s_key)

d1 = {value: key for key, value in d.items()}
print(d1)

d2 = {key: value for key, value in d.items() if value > 22}
print(d2)
