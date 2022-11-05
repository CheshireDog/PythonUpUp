#  coding = utf-8 

# @Time : 2022/5/17 10:00
# @Author : HJH
# @File : fib.py
# @Software: PyCharm

# 斐波那契
class Solution:
    # 暴力递归
    def fib1(self, n: int) -> int:
        if n < 2:
            return n
        else:
            return self.fib1(n-1) + self.fib1(n-2)

    # 动态规划
    def fib2(self, n: int) -> int:
        if n < 2:
            return n
        p, q, r = 0, 0, 1
        for i in range(2, n + 1):
            p, q = q, r
            r = p + q
        return r
