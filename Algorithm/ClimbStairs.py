# coding = utf-8

"""
Author:hjh
Date:06.01
"""

class Solution:
    def climbStairs(self, n: int):
        if n < 3:
            return n
        num_list = []
        num_list.append(1)
        num_list.append(2)
        for i in range(2, n):
            num_list.append(num_list[i-1]+num_list[i-2])
        return num_list[-1]

    def fib(self, n):
        if n ==1:
            return 1
        if n == 2:
            return 2
        if n >2:
            return self.fib(n-1)+self.fib(n-2)
        else:
            return 0

if __name__ == '__main__':
    n = 5
    so = Solution()
    print(so.climbStairs(38))
