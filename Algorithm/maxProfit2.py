#  coding = utf-8 

# @Time : 2022/8/26 15:51
# @Author : HJH
# @File : maxProfit2.py
# @Software: PyCharm


class Solution:
    def max_profit(self, prices) -> int:
        if len(prices) < 2:
            return 0
        sum_profit = 0
        # buy_price = prices[0]
        sold_price = prices[1]
        if prices[1] > prices[0]:
            sign = 1
            buy_price = prices[0]
        else:
            sign = 0
            buy_price = prices[1]
        if len(prices) == 2:
            return sold_price - buy_price
        for i in range(2, len(prices)):
            # print('当前股价为'+str(prices[i]))
            if prices[i] > prices[i - 1]:
                # print('涨')
                sold_price = prices[i]
                sign = 1
                # print('止跌，买入价格为'+str(buy_price))
            else:
                # print('跌')
                if sign:
                    # print('跳水,卖出价为'+str(sold_price))
                    sign = 0
                    sum_profit += sold_price - buy_price
                    # print(sum_profit)
                    # sold_price = 0
                    # print('观望')
                buy_price = prices[i]
        if sign:
            # print('收尾')
            sum_profit += sold_price - buy_price
        return sum_profit

    def max_profit2(self, prices) -> int:
        n = len(prices)
        ans = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                ans += prices[i] - prices[i - 1]
        return ans


if __name__ == '__main__':
    so = Solution()
    pri = [3, 2, 6, 5, 0, 3]
    print(so.max_profit(pri))
