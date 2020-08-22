#  coding = utf-8 

# @Time : 2020/8/9 15:48
# @Author : HJH
# @File : FindMaxConsecutiveOnes.py
# @Software: PyCharm


class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        max_len = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                if count > max_len:
                    max_len = count
                count = 0
        return max_len if count < max_len else count


if __name__ == '__main__':
    so = Solution()
    nums = [1,1,0,0,1,1,1]
    print(so.findMaxConsecutiveOnes(nums))