#  coding = utf-8 
# @Time : 2020/8/2 19:46
# @Author : HJH
# @File : LengthOfLastWord.py
# @Software: PyCharm


class Solution:
    def lengthOfLastWord(self, s: str):
        if s == ' ':
            return 0
        else:
            return len(s.split(' ')[-1]) if ' ' in s else len(s)

    def lengthOfLastWord2(self, s: str):
        if ' ' in s:
            return len(s.split(' ')[-1])
        elif s == '':
            return 0
        else:
            return len(s)


if __name__ == '__main__':
    so = Solution()
    ss = "a"
    print(so.lengthOfLastWord2(ss))
