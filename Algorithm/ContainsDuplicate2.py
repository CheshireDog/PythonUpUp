# coding = utf-8 

# @Time : 2020/8/18 20:19
# @Author : 0049003071
# @File : ContainsDuplicate2.py
# @Software: PyCharm


class Solution:
    def containsDuplicate2(self, nums, k) -> bool:
        num_dict = {}
        index = 0
        for i in nums:
            if i not in num_dict:
                num_dict[i] = index
                index += 1
            else:
                if index - num_dict[i] <= k:
                    # print(num_dict[i], index)
                    return True
                else:
                    num_dict[i] = index
                    index += 1
        return False

    def containsDuplicate3(self, nums, k) -> bool:
        num_dict = []
        for i in nums:
            if i in num_dict:
                return True
            num_dict.append(i)
            if len(num_dict) > k:
                num_dict = num_dict[1:]
        return False


if __name__ == '__main__':
    so = Solution()
    nums = [1,2,3,1,2,3]
    k = 2
    print(so.containsDuplicate2(nums, k))