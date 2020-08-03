# coding = utf-8

"""
Author:hjh
Date:07.27
Method:杨辉三角
"""


class Solution:
    def generate(self, numRows):
        result1 = [1]
        result2 = [1, 1]
        if numRows == 0:
            return []
        if numRows == 1:
            return [result1]
        if numRows == 2:
            return [result1, result2]
        result = [result1, result2]
        temp = [1, 1]
        for i in range(2, numRows):
            l = [1]
            for j in range(len(temp)-1):
                l.append(temp[j]+temp[j+1])
            l.append(1)
            temp = l
            result.append(temp)
        return result

    def generate2(self, rowIndex):
        result = [1]
        if rowIndex == 0:
            return [1]
        temp = [1]
        while rowIndex > 0:
            for i in range(0, len(result)-1):
                temp.append(result[i] + result[i+1])
            temp.append(1)
            result = temp
            temp = [1]
            rowIndex -= 1
        return result


if __name__ == '__main__':
    so = Solution()
    print(so.generate2(3))