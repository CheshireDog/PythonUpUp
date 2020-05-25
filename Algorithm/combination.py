# coding = utf-8

"""
Author:hjh
Date:05.25
"""

import numpy as np


class Solution(object):
    def combine(self, n: int, k: int):
        result = []
        start = np.arange(1, k+1)
        result.append(start)
        print(start)


    def combine2(self, n):
        result = []
        for i in range(1,n):
            for j in range(i+1,n+1):
                result.append([i,j])
        return result

    def combine_plus(self, pre_list, n, k):
        if len(pre_list[0]) < k:
            print('ok!')


if __name__ == '__main__':
    n = 4
    k = 2
    so = Solution()
    re = so.combine2(n)
    print(re)