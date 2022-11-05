#  coding = utf-8 

# @Time : 2022/9/9 11:01
# @Author : HJH
# @File : wordPattern.py
# @Software: PyCharm


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = {}
        s_list = s.split(' ')
        if not len(pattern) == len(s_list):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in words:
                if s_list[i] not in words.values():
                    words[pattern[i]] = s_list[i]
                else:
                    return False
            elif not words[pattern[i]] == s_list[i]:
                return False

        return True


if __name__ == '__main__':
    so = Solution()
    pattern = "aaa"
    s = "dog dog dog dog"
    print(so.wordPattern(pattern, s))
