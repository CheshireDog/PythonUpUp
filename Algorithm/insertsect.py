# coding = utf-8

"""
Author:hjh
Date:07.13
Method:1.最直接的想法，双重循环遍历，并将被查询list的相应元素删除；
       2.哈希表存储较小的list
"""


class Solution:
    def intersect(self, nums1: list, nums2: list) :
        result = []
        for i in nums1:
            if i in nums2:
                result.append(i)
                nums2.remove(i)
        return result

    def intersect2(self, nums1: list, nums2: list) :
        item_dict = {}
        result = []
        if len(nums1) < len(nums2):
            for i in nums1:
                if not i in item_dict:
                    item_dict[i] = 1
                else:
                    item_dict[i] += 1
            for j in nums2:
                if j in item_dict and item_dict[j] >= 1:
                    item_dict[j] -= 1
                # else:
                #     del item_dict[j]
                    result.append(j)

        else:
            for i in nums2:
                if not i in item_dict:
                    item_dict[i] = 1
                else:
                    item_dict[i] += 1
            for j in nums1:
                if j in item_dict and item_dict[j] >= 1:
                    item_dict[j] -= 1
                # else:
                #     del item_dict[j]
                    result.append(j)
        return result


if __name__ == '__main__':
    nums1 = [1,2,2,1]
    nums2 = [2,2,2]
    so = Solution()
    print(so.intersect2(nums1, nums2))