#  coding = utf-8 

# @Time : 2021/7/6 20:23
# @Author : HJH
# @File : maxProfit.py
# @Software: PyCharm


class Solution:
    def max_profit(self, prices) -> int:
        min_price = 100001
        max_profit = 0
        for i in prices:
            min_price = min(min_price, i)
            max_profit = max(max_profit, i - min_price)
        return max_profit

    def max_profit_dp(self, prices):
        n = len(prices)
        if n == 0:
            return 0  # 边界条件
        dp = [0] * n
        minprice = prices[0]

        for i in range(1, n):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - minprice)

        return dp[-1]


if __name__ == '__main__':
    so = Solution()
    pri = [7, 1, 5, 3, 6, 4]
    print(so.max_profit(pri))
