#  coding = utf-8 

# @Time : 2022/10/5 11:49
# @Author : HJH
# @File : minCoin.py
# @Software: PyCharm


class Solution:
    def minCount(self, coins):
        sums = 0
        for i in coins:
            sums += i // 2 + i % 2
        return sums


if __name__ == '__main__':
    coins = [4, 6, 1]
    so = Solution()
    print(so.minCount(coins))
