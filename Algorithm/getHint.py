#  coding = utf-8 

# @Time : 2022/9/10 1:03
# @Author : HJH
# @File : getHint.py
# @Software: PyCharm

from _collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0
        s_count = Counter(secret)
        g_count = Counter(guess)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
        for key in s_count:
            if key in g_count:
                cow += min(s_count[key], g_count[key])
        return f'{bull}A{cow}B'
