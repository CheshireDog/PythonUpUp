#  coding = utf-8 

# @Time : 2022/5/17 10:16
# @Author : HJH
# @File : tribonacci.py
# @Software: PyCharm

class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        elif n == 2:
            return 1
        else:
            b = 1
            c = 1
            d = 2
            for i in range(3, n+1):
                a = b
                b = c
                c = d
                d = a+b+c
            return c