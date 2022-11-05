#  coding = utf-8 

# @Time : 2022/10/10 17:18
# @Author : HJH
# @File : Decorator.py
# @Software: PyCharm


import time


# 装饰器 （语法糖，注解）

def run_time(func):
    def get_time(*args, **kwargs):
        print(time.time())
        func(*args, **kwargs)

    return get_time


@run_time
def student_run(i):
    print('student run'+str(i))

@run_time
def student_run2(i,j):
    print('student run'+str(i*j))

@run_time
def student_run3():
    print('student run'+' null')

@run_time
def student_run4(*args, **kwargs):
    print('student run'+str(*args)+str(**kwargs))


student_run(1)
student_run2(1,2)
