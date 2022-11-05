#  coding = utf-8 

# @Time : 2021/7/26 20:35
# @Author : HJH
# @File : setZeros.py
# @Software: PyCharm


class Solution:
    def setZeroes(self, matrix) -> None:
        x = []
        y = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    x.append(i)
                    y.append(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in x or j in y:
                    matrix[i][j] = 0


if __name__ == '__main__':
    so = Solution()
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    so.setZeroes(matrix)
    print(matrix)
