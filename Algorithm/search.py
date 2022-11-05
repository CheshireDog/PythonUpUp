#  coding = utf-8 

# @Time : 2022/5/17 10:58
# @Author : HJH
# @File : search.py
# @Software: PyCharm


class Solution:
    def search(self, nums, target) -> int:
        left = 0
        right = len(nums)-1
        # temp = (left + right)//2
        while left < right:
            temp = (left + right)//2
            print(temp)
            if target == nums[temp]:
                return temp
            elif target < nums[temp]:
                right = temp
            else:
                left = temp+1
        if nums[left] == target:
            return  left
        else:
            return -1

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7,8]
    target = 5

    so = Solution()
    print(so.search(nums, target))