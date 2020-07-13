# coding = utf-8

"""
Author:hjh
Date:05.23
"""


class Solution(object):
    def four_sum(self, number_list, target):
        length = len(number_list)
        nums = sorted(number_list)
        # nums = number_list
        dict = {}
        result = []
        if length < 4:
            return []
        if length == 4:
            if sum(nums) == target:
                return [nums]
            else:
                return []
        for i in range(length-1):
            for j in range(i+1, length):
                if nums[i]+nums[j] in dict:
                    key = nums[i]+nums[j]
                    dict[key].append((i, j))
                else:
                    key = nums[i]+nums[j]
                    dict[key] = [(i, j)]
        # print(dict)
        for p in range(2, length-1):
            for q in range(p+1, length):
                sub = target-nums[p]-nums[q]
                if sub in dict:
                    for index in dict[sub]:
                        if index[1] < p:
                            result.append((nums[index[0]], nums[index[1]], nums[p], nums[q]))
        return list(set(result))

    def fourSum(self, number_list, target):
        length = len(number_list)
        # nums = sorted(number_list)
        nums = number_list
        dict = {}
        result = []
        if length < 4:
            return []
        if length == 4:
            if sum(nums) == target:
                return [nums]
            else:
                return []
        for i in range(length-1):
            for j in range(i+1, length):
                if nums[i]+nums[j] in dict:
                    key = nums[i]+nums[j]
                    dict[key].append((i, j))
                else:
                    key = nums[i]+nums[j]
                    dict[key] = [(i, j)]
        # print(dict)

        for key in dict:
            if (target-key) in dict.keys():
                if target == 2*key:
                    if len(dict[key]) > 1:
                        for p in range(len(dict[key])-1):
                            for q in range(p+1, len(dict[key])):
                                ind = [dict[key][p][0],dict[key][p][1],dict[key][q][0],dict[key][q][1]]
                                # print(ind)
                                if len(set(ind)) == 4:
                                    # sorted(ind)
                                    ind.sort()
                                    # print(ind)
                                    # print((nums[ind[0]], nums[ind[1]], nums[ind[2]],nums[ind[3]]))
                                    result.append((nums[ind[0]], nums[ind[1]], nums[ind[2]],
                                                   nums[ind[3]]))
                else:
                    for index in dict[key]:
                        for index2 in dict[target-key]:
                            if len({index[0], index[1], index2[0], index2[1]}) == 4:
                                ind = sorted([index[0], index[1], index2[0], index2[1]])
                                # print(ind)
                                result.append((nums[ind[0]], nums[ind[1]], nums[ind[2]], nums[ind[3]],))
        return list(set(result))

if __name__ == '__main__':
    num_list = [1,0,-1,0,-2,2]
    print(num_list)
    target = 0
    so = Solution()
    print(so.four_sum(num_list, target))
    print(so.fourSum(num_list, target))





