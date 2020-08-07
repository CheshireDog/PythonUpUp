# coding = utf-8 

# @Time : 2020/8/6 13:42
# @Author : 0049003071
# @File : MinSubArrayLen.py
# @Software: PyCharm


class Solution:
    # 里层暴力循环，外层二分查找，会超时555
    def minSubArrayLen(self, s: int, nums):
        result = 0
        left = 1
        right = len(nums)
        while left <= right:
            print(left, right)
            ind = (left + right) // 2
            if self.find_max_combine(ind, nums) >= s:
                result = ind
                right = ind - 1
            else:
                left = ind + 1
        return result

    def find_max_combine(self, length, nums):
        max = 0
        for i in range(len(nums)-length+1):
            if sum(nums[i: i+length]) > max:
                max = sum(nums[i: i+length])
        return max

    # 双指针法
    def minSubArrayLen2(self, s: int, nums) -> int:
        if len(nums) == 0:
            return 0
        res = len(nums) + 1
        num_add = nums[0]
        a, b = 0, 0
        while a < len(nums) and b < len(nums):
            if num_add < s:
                    b += 1
                    if b < len(nums):
                        if nums[b] >= s:
                            return 1
                        else:
                            num_add += nums[b]
            if num_add >= s:
                res = min(b-a+1, res)
                num_add -= nums[a]
                a += 1
        return res if res != len(nums)+1 else 0


if __name__ == '__main__':
    value = 15
    nums = [1,2,3,4,5]
    so = Solution()
    print(so.minSubArrayLen2(value, nums))
