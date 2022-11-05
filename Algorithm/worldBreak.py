#  coding = utf-8 

# @Time : 2022/8/29 15:14
# @Author : HJH
# @File : worldBreak.py
# @Software: PyCharm

class Solution:
    def wordBreak(self, s: str, word_dict) -> bool:
        s_len = len(s)
        while s_len > 0:
            for word in word_dict:
                cur_len = len(word)
                if s[:cur_len] == word:
                    s = s[cur_len:]
                    # print(s)
            if s_len == len(s):
                return False
            else:
                s_len = len(s)
        return True

    def wordBreak2(self, s: str, wordDict) -> bool:
        n = len(s)
        dp = [False] * n
        for i in range(n):
            for word in wordDict:
                m = len(word)
                if word == s[i - m + 1:i + 1] and (dp[i - m] or i - m + 1 == 0):
                    dp[i] = True
        # print(dp)
        return dp[-1]


if __name__ == '__main__':
    so = Solution()
    ss = "cars"
    w_dict = ["car", "ca", "rs"]
    print(so.wordBreak2(ss, w_dict))
