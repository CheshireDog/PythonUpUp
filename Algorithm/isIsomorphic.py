#  coding = utf-8 

# @Time : 2021/2/19 17:07
# @Author : HJH
# @File : isIsomorphic.py
# @Software: PyCharm


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        pear = {}
        pair = {}
        for i in range(len(s)):
            if not s[i] in pear:
                pear[s[i]] = t[i]
                pair[t[i]] = s[i]
                if not len(pear) == len(pair):
                    return False
            if not t[i] == pear[s[i]]:
                return False
        return True


if __name__ == '__main__':
    so = Solution()
    s1 = "paper"
    t1 = "tiwle"
    print(so.isIsomorphic(s1, t1))

