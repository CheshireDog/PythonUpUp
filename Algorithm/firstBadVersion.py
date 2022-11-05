#  coding = utf-8 

# @Time : 2022/5/17 11:30
# @Author : HJH
# @File : firstBadVersion.py
# @Software: PyCharm

class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n
        temp = 0
        while left < right:
            temp = (left + right)//2
            if not isBadVersion(temp):
                left = temp + 1
            else :
                right = temp
        return right