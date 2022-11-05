#  coding = utf-8 

# @Time : 2022/10/9 0:30
# @Author : HJH
# @File : coinChange.py
# @Software: PyCharm


class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[-1] if dp[-1] != float('inf') else -1


if __name__ == '__main__':
    so = Solution()
    print(so.coinChange([1,2,5], 11))

