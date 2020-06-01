# coding = utf-8

"""
Author:hjh
Date:05.25
Method：先得出选择两个的所有结果R2，对于长度加一的情形只需将R2各结果的每项加一再在开头添加1，过滤掉最大值溢出的情形。
        优化：因为排列组合C(5,2)=C(5,3)，故将k>n/2的情形转化为n-k即可。
"""

import copy

class Solution(object):
    def combine(self, n: int, k: int):
        result = []
        if k == 0:
            return result
        if k == 1:
            for i in range(n):
                result.append([i+1])
            return result
        if k == 2:
            return self.combine2(n)
        if k == n:
            temp = []
            for i in range(n):
                temp.append(i+1)
            result.append(temp)
            return result
        if k >= round(n/2):
            temp = []
            full_list = [x+1 for x in range(n)]
            # print(full_list)
            if n-k == 1:
                temp = []
                for i in range(n):
                    temp.append([i+1])
            elif n-k == 2:
                temp = self.combine2(n)
            else:
                temp = self.combine_left(n, n-k)
            # print(temp)
            for i in temp:
                result.append(list(set(full_list)-set(i)))
            return result
        else:
            return self.combine_left(n, k)

    def combine_left(self, n: int, k: int):
        start = self.combine2(n)
        if k >2:
            result = start
            for iter in range(k-2):
                result = copy.copy(self.combine_plus(result, n, k))
                # print(result)
            return result

    def combine2(self, n):
        result = []
        for i in range(1, n):
            for j in range(i+1, n+1):
                result.append([i, j])
        return result

    def combine_plus(self, pre_list, n, k):
        result = []
        for j in range(1, n-k+2):
            # print("***************")
            # print(pre_list)
            for i in range(len(pre_list)):
                pre_list[i] = [x+1 for x in pre_list[i]]
                if max(pre_list[i]) <= n:
                    inserted = copy.copy(pre_list[i])
                    inserted.insert(0, j)
                    result.append(inserted)
        return result

if __name__ == '__main__':
    n = 10
    k = 7
    so = Solution()
    print(so.combine(n, k))

