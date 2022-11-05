#  coding = utf-8 

# @Time : 2022/9/10 16:27
# @Author : HJH
# @File : isUgly.py
# @Software: PyCharm

class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        # if n == 1:
        #     return True
        while n % 2 == 0:
            n = n / 2
        while n % 3 == 0:
            n = n / 3
        while n % 5 == 0:
            n = n / 5
        if n == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    so = Solution()
    print(so.isUgly(7))
