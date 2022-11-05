# coding = utf-8 

# @Time : 2020/8/18 19:44
# @Author : 0049003071
# @File : ContainsDuplicate.py
# @Software: PyCharm


class Solution:
    def containsDuplicate(self, nums) -> bool:
        num_dict = {}
        for i in nums:
            if i not in num_dict:
                num_dict[i] = 0
            else:
                return True
        return False


if __name__ == '__main__':
    so = Solution()
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(so.containsDuplicate(nums))
