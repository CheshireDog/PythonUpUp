#  coding = utf-8 

# @Time : 2020/8/5 21:56
# @Author : HJH
# @File : RemoveElement.py
# @Software: PyCharm


# 剔除数组中所有的目标值，将所有t个非目标元素置于数组的前t项
class Solution:
    def removeElement(self, nums, val):
        # 遍历数组若元素为目标值，将其与最右侧元素对调，若最右侧元素也为目标值则下标减一
        right = len(nums) - 1
        left = 0
        # if right == left:
        #     if nums[0] == val:
        #         return 0
        #     else:
        #         return 1
        while left <= right:
            if nums[right] == val:
                print(right)
                right -= 1
                continue
            if nums[left] == val:
                print(right, left)
                nums[left] = nums[right]
                right -= 1
            left += 1
        return left


if __name__ == '__main__':
    so = Solution()
    print(so.removeElement([], 3))
