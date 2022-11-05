#  coding = utf-8 

# @Time : 2022/10/10 16:39
# @Author : HJH
# @File : Closure.py
# @Software: PyCharm


# 闭包 返回值是函数的函数
# 闭包就是外部函数中定义了一个内部函数，当外部函数返回内部函数对象（注意是函数对象）时，程序接收了内部函数的定义（此时并未被执行），当再次执行这个返回值时，这个被返回的函数才能被执行。
# 创建一个闭包必须满足以下几点:
#
# 必须有一个内嵌函数
# 内嵌函数必须引用外部函数中的变量
# 外部函数的返回值必须是内嵌函数

# 闭包和装饰器的区别：闭包传递的是变量，而装饰器传递的是函数，除此之外没有任何区别，或者说装饰器是闭包的一种，它只是传递函数的闭包。

a = 1


def func(b):
    return a + b


print(func(100))

a = 2
a = 3
print(func(100))
print(func(100))