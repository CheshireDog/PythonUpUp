#  coding = utf-8 

# @Time : 2021/1/6 13:56
# @Author : HJH
# @File : isHappy.py
# @Software: PyCharm


class Solution:
    def isHappy(self, n: int):


        return 0





    def intSplit(self, num: int):
        result = 0
        while num // 10 > 0:
            v = num % 10
            result += v * v
            num = num // 10

        return result


if __name__ == '__main__':
    a = 1
    print(a//10)