#  coding = utf-8 

# @Time : 2021/7/26 19:47
# @Author : HJH
# @File : reshapeFunc.py
# @Software: PyCharm


class Solution:
    def matrixReshape(self, mat, r: int, c: int) :
        if len(mat) * len(mat[0]) == r * c:
            result = []
            temp = []
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    temp.append(mat[i][j])
                    if len(temp) == c:
                        result.append(temp)
                        temp = []
            return result
        else:
            return mat


if __name__ == '__main__':
    so = Solution()
    nums = [[1, 2],[3, 4]]
    r = 1
    c = 4
    print(so.matrixReshape(nums, r, c))
