#  coding = utf-8 

# @Time : 2022/9/10 16:51
# @Author : HJH
# @File : isUgly2.py
# @Software: PyCharm


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        p2 = p3 = p5 = 1

        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1

        return dp[n]


if __name__ == '__main__':
    so = Solution()
    print(so.nthUglyNumber(100))