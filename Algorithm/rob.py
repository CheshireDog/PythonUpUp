#  coding = utf-8 
# @Time : 2020/8/2 21:26
# @Author : HJH
# @File : rob.py
# @Software: PyCharm


class Solution:
    def rob1(self, nums):
        robed = 0
        nums += [0, 0]
        while len(nums) > 2:
            if nums[0] >= nums[1]:
                robed += nums[0]
                nums = nums[2:]
                print(nums)
            elif nums[1] >= nums[0] + nums[2]:
                robed += nums[1]
                nums = nums[3:]
                print(nums)
            else:
                nums[2] += nums[0]
                nums = nums[1:]
                print(nums)
        return robed

    def rob2(self, nums):
        robed = 0
        length = len(nums)
        nums += [0, 0]
        for i in range(length):
            if nums[i] >= nums[i + 1]:
                robed += nums[i]
                nums[i + 1] = 0
            elif nums[i + 1] >= nums[i] + nums[i + 2]:
                robed += nums[i + 1]
                nums[i + 1] = nums[i + 2] = 0
            else:
                nums[i + 2] += nums[i]
        return robed

    def rob_dy(self, nums):  # 动态规划
        prev = 0
        curr = 0

        # 每次循环，计算“偷到当前房子为止的最大金额”
        for i in nums:
            # 循环开始时，curr 表示 dp[k-1]，prev 表示 dp[k-2]
            # dp[k] = max{ dp[k-1], dp[k-2] + i }
            prev, curr = curr, max(curr, prev + i)

        return curr


if __name__ == '__main__':
    so = Solution()
    print(so.rob_dy([2, 7, 9, 3, 1]))
