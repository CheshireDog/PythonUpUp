#  coding = utf-8 

# @Time : 2021/11/19 9:59
# @Author : HJH
# @File : sortColors.py
# @Software: PyCharm


class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        ll = len(nums)
        i= 0
        left = 0
        right = ll-1

        while i <= right:
            if nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            elif nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1

            else:
                i += 1

if __name__ == '__main__':
    so = Solution()
    nums = [2,0,2,1,1,0]
    so.sortColors(nums)
    print(nums)
