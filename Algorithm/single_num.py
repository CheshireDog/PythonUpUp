# coding = utf-8

"""
Author:hjh
Date:07.09
"""


class Solution(object):
    def single_num(self, number_list):
        dictionary = {}
        result = number_list.copy()
        for i in number_list:
            print("i:"+str(i))
            if i in dictionary:
                print("delete:"+str(i))
                # dictionary[i] += 1
                result.remove(i)
                result.remove(i)
                print(number_list)
            else:
                print(i)
                dictionary[i] = 1
        return result[0]

    def single_num2(self, nums):
        result = sorted(nums)
        print(result)
        for i in range(1, len(result)-1):
            if (result[i-1] != result[i]) and (result[i+1] != result[i]):
                return result[i]
        if result[0] == result[1]:
            return result[-1]
        else:
            return result[0]

    def single_num3(self, nums):
        return sum(set(nums))*2-sum(nums)

    def single_num4(self, nums):
        result = 0
        for v in nums:
            result ^= v
        return result


if __name__ == '__main__':
    numbers = [1,3,1,-1,3]
    so = Solution()
    print(so.single_num4(numbers))


