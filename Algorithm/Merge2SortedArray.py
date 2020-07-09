# coding = utf-8

"""
Author:hjh
Date:05.31
"""


class Solution:
    def merge(self, nums1, m: int, nums2, n: int):
        i,j = 0,0
        edge = m
        if not nums2 == []:
            while j < n and i < edge:
                if nums1[i] > nums2[j]:
                    nums1.insert(i, nums2[j])
                    nums1.pop()
                    # print(nums1)
                    i += 1
                    edge += 1
                    j += 1
                else:
                    i += 1
            if j < n:
                # print(j)
                offset = 0
                for p in range(j, n):
                    nums1.pop()
                    nums1.insert(m+j+offset, nums2[p])
                    offset += 1
            print(nums1)

if __name__ == '__main__':
    so = Solution()
    # nums1 = [4,0,0,0,0,0]
    # nums2 = [1,2,3,5,6]
    nums1 = [2,0]
    nums2 = [1]
    m = 2
    n = 1
    so.merge(nums1, m, nums2, n)


