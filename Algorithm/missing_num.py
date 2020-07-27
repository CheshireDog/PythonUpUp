# coding = utf-8

"""
Author:hjh
Date:07.25
"""

class Solution:
    def missingNumber(self, nums) :
        length = len(nums)
        sums = sum(nums)
        return length*(length+1)/2-sums


if __name__ == '__main__':
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    so = Solution()
    print(so.missingNumber(nums))
