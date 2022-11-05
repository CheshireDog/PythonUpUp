# coding = utf-8

"""
Author:hjh
Date:05.31
Method：88
"""


class Solution(object):
    def merge(self, nums1, m: int, nums2, n: int):
        i, j = 0, 0
        if n == 0:
            pass
        else:
            while i < m or j < n:
                try:
                    if nums1[i] >= nums2[j]:
                        nums1.insert(i, nums2[j])
                        j += 1
                        nums1.pop()
                    elif nums1[i] == nums2[j]:
                        nums1.insert(i, nums2[j])
                        i += 1
                        j += 1
                        nums1.pop()
                    else:

                        i += 1
                except:
                    break
            if j < n:
                nums1[m + j:m + n] = nums2[j:n]


if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    so = Solution()
    so.merge(nums1, m, nums2, n)
    print(nums1)