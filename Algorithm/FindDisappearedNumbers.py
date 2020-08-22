#  coding = utf-8 

# @Time : 2020/8/9 16:28
# @Author : HJH
# @File : FindDisappearedNumbers.py
# @Software: PyCharm


class Solution(object):
    # 遍历数组，对于出现的每一个元素，将其对应的下标的元素的值取反，没出现过的元素的下标对应的值是正数。妙蛙！
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            new_index = abs(nums[i]) - 1
            if nums[new_index] > 0:
                nums[new_index] *= -1
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        return result


if __name__ == '__main__':
    so = Solution()
    nums = [4,3,2,7,8,2,3,1]
    print(so.findDisappearedNumbers(nums))
