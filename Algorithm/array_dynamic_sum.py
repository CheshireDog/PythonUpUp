# coding = utf-8

"""
Author:hjh
Date:07.09
"""

class Solution(object):
    def array_sum(self, number_list):
        array_sums = [0]
        # array_sums.append(0)
        for i in range(len(number_list)):
            array_sums.append(number_list[i]+array_sums[i])
        return array_sums[1:]

if __name__ == '__main__':
    numbers = [1,1,1,11,1]
    so = Solution()
    print(so.array_sum(numbers))

