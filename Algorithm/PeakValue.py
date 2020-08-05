#  coding = utf-8 

# @Time : 2020/8/5 22:01
# @Author : HJH
# @File : PeakValue.py
# @Software: PyCharm


# 找出大于左右值长度元素（任意一个），下标-1与+无穷的值为无穷小
class Solution:
    def findPeakElement(self, nums):
        # 暴力比较
        if len(nums) < 2:
            return 0
        # if len(nums) == 2:
        #     return 0 if nums[0] > nums[1] else 1
        if nums[0] > nums[1]:
            return 0
        if nums[len(nums)-2] < nums[len(nums)-1]:
            return len(nums)-1
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] and nums[i+1] > nums[i+2]:
                return i+1

    def findPeakElemt2(self, nums):
        # 若数组单调减，则第一个元素符合；若递增或峰值在中间则找出右侧小于该元素的下标即可，妙蛙
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return i
        return len(nums)-1


if __name__ == '__main__':
    nums = [1,2,1,3,5,6,4]
    so = Solution()
    print(so.findPeakElement(nums))