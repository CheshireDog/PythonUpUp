#  coding = utf-8 

# @Time : 2021/7/2 16:19
# @Author : HJH
# @File : RectangleArea.py
# @Software: PyCharm


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        s = (C-A)*(D-B)+(H-F)*(G-E)
        x = sorted([A, C, E, G])
        y = sorted([B, D, F, H])
        sy = (x[2] - x[1]) * (y[2] - y[1])
        if A > G or B > H or C < E or D < F:
            return s
        else:
            return s - sy



if __name__ == '__main__':
    so = Solution()
    print(so.computeArea(1,2,3,4,5,6,7,8))

