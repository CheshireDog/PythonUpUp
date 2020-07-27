# coding = utf-8

"""
Author:hjh
Date:05.31
Method：
"""


class Solution(object):
    def merge(self, nums1, m: int, nums2, n: int):
        i, j = 0, 0
        if n == 0:
            pass
        else:
            while i < m or j < n:
                try:
                    if nums1[i] > nums2[j]:
                        nums1.insert(i + j, nums2[j])
                        j += 1
                        nums1.pop()
                        # print(nums1)
                    elif nums1[i] > 0:
                        i += 1
                    else:
                        nums1[i] = nums2[j]
                        i += 1
                        j += 1
                except:
                    break

            #     # result.append(nums1[i])
            #     i += 1
            #     print(i,j)
            #     print(nums1)
            # elif nums1[i] > 0:
            #     nums1.insert(i + j, nums2[j])
            #     nums1.pop()
            #     i += 1
            #     j += 1
            #     print(i, j)
            #     print(nums1)
            # else:
            #     nums1.insert(i + j, nums2[j])
            #     nums1.pop()
            #     j += 1

        print(nums1)
        # return result


if __name__ == '__main__':
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    so = Solution()
    print(so.merge(nums1, m, nums2, n))