#  coding = utf-8 

# @Time : 2022/9/8 22:14
# @Author : HJH
# @File : maxArea.py
# @Software: PyCharm

class Solution:

    def maxArea(self, height) -> int:
        l = len(height)
        left = 0
        right = l - 1
        area = 0
        while left < right:
            cur_area = min(height[left], height[right]) * (right - left)
            area = max(area, cur_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area


if __name__ == '__main__':
    so = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(so.maxArea(height))
