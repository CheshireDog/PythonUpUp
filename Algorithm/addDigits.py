#  coding = utf-8 

# @Time : 2022/9/10 16:54
# @Author : HJH
# @File : addDigits.py
# @Software: PyCharm


class Solution:
    def addDigits(self, num: int) -> int:
        sums = 0
        if num < 10:
            return num
        current = num
        while current >= 10:
            print('当前数据：', current)
            for i in str(current):
                sums += int(i)
            current = sums
            sums = 0

        return current


if __name__ == '__main__':
    so = Solution()
    print(so.addDigits(1987))
