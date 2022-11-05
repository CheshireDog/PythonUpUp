#  coding = utf-8 

# @Time : 2021/7/26 21:00
# @Author : HJH
# @File : firstUniqChar.py
# @Software: PyCharm


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        length = len(s)
        for i in range(length):
            if s[i] not in d:
                d[s[i]] = i
            else:
                d[s[i]] = length + 1
        print(d.values())
        ret = min(d.values())
        return -1 if ret > length else ret


if __name__ == '__main__':
    so = Solution()
    print(so.firstUniqChar("loveleetcode"))
