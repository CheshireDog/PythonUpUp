#  coding = utf-8 

# @Time : 2020/8/5 22:06
# @Author : HJH
# @File : MajorityElement.py
# @Software: PyCharm


# 找出出现次数最多的元素（最多者出现频数大于数组长度一半）
class Solution:
    # 字典
    
    def majorityElement(self, nums):
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
                if dic[i] > len(nums)//2:
                    return i
            else:
                dic[i] = 1
        return nums[0]

    # 投票法 题设中主要元素超过了半数，所以每当出现不同元素则major的count减一，为0时就把当前元素赋给major。妙蛙
    def majorityElement2(self, nums):
        major, count = nums[0], 1
        for i in nums[1:]:
            if count == 0:
                major = i
                count = 1
            elif i == major:
                count += 1
            else:
                count -= 1
        return major


if __name__ == '__main__':
    nums = [2,2,1,1,1,2,2]
    so = Solution()
    print(so.majorityElement2(nums))