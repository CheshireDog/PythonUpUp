#  coding = utf-8 

# @Time : 2021/7/26 21:12
# @Author : HJH
# @File : canConstruct.py 赎金信
# @Software: PyCharm


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i,'',1)

            else:
                return False
        return True


if __name__ == '__main__':
    so = Solution()
    ransomNote = "aaa"
    magazine = "ab"
    print(so.canConstruct(ransomNote, magazine))
