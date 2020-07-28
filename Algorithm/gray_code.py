# coding = utf-8

"""
Author:hjh
Date:07.27
Method:找出规律：对于每一个2的倍数，其内的数的规律为，第一个数是2的n-1方加2的n-2方之和（例如第四位为2+4）；
        后面的每一位数规律如下：
        n=3：left :[ 1 -2 -1] 需要加上[6 7 5 4]，以此类推
        left :[ 1  2 -1 -4  1 -2 -1]
        left :[ 1  2 -1  4  1 -2 -1 -8  1  2 -1 -4  1 -2 -1]
"""

import numpy as np


class Solution:
    def grayCode(self, n: int):
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]
        else:
            result_array = [0, 1]
            left = [-1]
            # left = [1, -2, -1]
            for i in range(2, n+1):
                # n = 2
                result_array = np.concatenate((result_array, np.array(self.get_value(i, left))))
                length = len(left)
                left[length//2] *= -1
                right = np.array(left[::-1]) * -1
                change_arr = np.concatenate((left, np.array([2**(i-1)*-1]), right))
                left = change_arr
                print("left :{}".format(left))
            return result_array.tolist()

    def get_value(self, n, arr):
        v = 2**(n-1)+2**(n-2)
        result = list()
        result.append(v)
        for i in arr:
            v += i
            result.append(v)
        return result


if __name__ == '__main__':

    add = [-1]
    so = Solution()
    print(so.grayCode(5))

