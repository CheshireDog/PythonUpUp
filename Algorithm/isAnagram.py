#  coding = utf-8 

# @Time : 2021/2/19 17:43
# @Author : HJH
# @File : isAnagram.py
# @Software: PyCharm
import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        stat1 = {}
        stat2 = {}
        for i in range(len(s)):
            if not s[i] in stat1:
                stat1[s[i]] = 1
            else:
                stat1[s[i]] += 1
            if not t[i] in stat2:
                stat2[t[i]] = 1
            else:
                stat2[t[i]] += 1
        return stat1 == stat2

    def isAnagram2(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)



if __name__ == '__main__':
    so = Solution()
    print(so.isAnagram("anagram", "nagaram"))