#  coding = utf-8 
# @Time : 2020/8/2 20:24
# @Author : HJH
# @File : TwoSumSorted.py
# @Software: PyCharm


class Solution:
    def twoSum(self, numbers, target: int):
        bound = len(numbers) - 1
        for i in range(len(numbers)):
            if numbers[i] > target:
                bound = i
                break
        left = 0
        right = bound
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left+1, right+1]
        return []


if __name__ == '__main__':
    so = Solution()
    nn = [2, 4, 6, 7, 11, 15]
    tt = 13
    print(so.twoSum(nn, tt))