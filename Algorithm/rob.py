#  coding = utf-8 
# @Time : 2020/8/2 21:26
# @Author : HJH
# @File : rob.py
# @Software: PyCharm


class Solution:
    def rob(self, nums):
        pa = 0
        pb = 0
        for i in range(len(nums)):
            if i%2 == 0:
                pa += nums[i]
            else:
                pb += nums[i]
        if pa >= pb:
            return pa
        else:
            return pb


if __name__ == '__main__':
    so = Solution()
    print(so.rob([1,2,3,1]))

