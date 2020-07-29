# coding = utf-8

"""
Author:hjh
Date:07.25
"""

class Solution:
    def removeDuplicates(self, nums):
        count = 0
        sum = 0
        for i in range(2, len(nums)):
            if nums[i] == nums[i-2-count]:
                nums[i] += 90000000000
                count += 1
                sum += 1
            else:
                count = 0
        nums.sort()
        print(nums)
        return nums[:len(nums)-sum]

    def removeDuplicates2(self, nums):
        s = 1
        f = 2
        while f < len(nums):
            if nums[s-1] == nums[f]:
                f += 1
            else:
                nums[s+1] = nums[f]
                s += 1
                f += 1
        return s+1


if __name__ == '__main__':
    nums = [-2147483648,-2147483648,-2147483648,1,1,1,2]
    so = Solution()
    print(so.removeDuplicates(nums))