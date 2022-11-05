#  coding = utf-8 

# @Time : 2021/7/2 16:43
# @Author : HJH
# @File : maxSubArray.py
# @Software: PyCharm



class Solution:
    def maxSubArray(self, nums):
        backup = []
        temp = 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1], nums[0] + nums[1])
        for i in range(len(nums)):
            if nums[i] > 0:
                temp += nums[i]
            else:
                backup.append(temp)  # 出现负数先压栈
                if temp + nums[i] <= 0:  # 出现大负数，之前的结果抛弃
                    temp = 0
                else:
                    temp += nums[i]  # 小负数可以接受，累加当前结果
            backup.append(temp)
            print(temp)
        if max(backup) == 0:  # 防止全部为负
            return max(nums)
        else:
            return max(backup)


if __name__ == '__main__':
    so = Solution()
    print(so.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
