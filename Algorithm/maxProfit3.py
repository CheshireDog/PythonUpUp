#  coding = utf-8 

# @Time : 2022/8/26 18:14
# @Author : HJH
# @File : maxProfit3.py
# @Software: PyCharm


class Solution:
    def max_profit(self, prices) -> int:
        buy_1 = buy_2 = float('inf')  # 第一二次买之前的最低价
        pro_1 = pro_2 = 0

        for p in prices:
            buy_1 = min(buy_1, p)
            pro_1 = max(pro_1, p - buy_1)
            buy_2 = min(buy_2, p - pro_1)  # p - pro_1 是用第一次的钱抵消了一部分第二次买的钱
            pro_2 = max(pro_2, p - buy_2)
        return pro_2


if __name__ == '__main__':
    so = Solution()
    pri = [1, 3, 2, 4, 3, 5, 4, 6, 1, 2, 1]
    print(so.max_profit(pri))
