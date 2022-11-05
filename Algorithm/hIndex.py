#  coding = utf-8 

# @Time : 2022/9/10 9:44
# @Author : HJH
# @File : hIndex.py
# @Software: PyCharm


class Solution:
    def hIndex(self, citations) -> int:
        citations_sorted = sorted(citations)
        length = len(citations)
        h_index = 0
        for i in range(len(citations_sorted)):
            if length - i <= citations_sorted[i]:
                h_index = length - i
                break
        return h_index


if __name__ == '__main__':
    so = Solution()
    ci = [3, 0, 6, 1, 5]
    print(so.hIndex(ci))
