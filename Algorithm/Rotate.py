#  coding = utf-8 

# @Time : 2020/8/5 21:27
# @Author : HJH
# @File : Rotate.py
# @Software: PyCharm


class Solution:
    # 数组翻转
    def rotate(self, nums, k: int):
        # 暴力双重循环，每次整体右移一位，会超时
        for i in range(k):
            temp = nums[-1]
            for j in range(len(nums)-1, 0, -1):
                nums[j] = nums[j-1]
            nums[0] = temp

    def rotate2(self, nums, k):
        # 每次将第一个元素添加到数组末端，并在原位将其删除
        # k % len(nums)用于解决k大于数组长度的情况
        for i in range(len(nums)-k % len(nums)):
            nums.append(nums[0])
            del nums[0]

    def rotate3(self, nums, k):
        # Python 数组切片
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        print(nums)

    def rotate4(self, nums, k):
        # 三次翻转
        k %= len(nums)
        self.swap(0, len(nums)-1)
        self.swap(0, k-1)
        self.swap(k, len(nums)-1)

    def swap(self, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    so = Solution()
    so.rotate4(nums, k)
