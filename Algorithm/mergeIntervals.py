#  coding = utf-8 

# @Time : 2021/11/19 10:31
# @Author : HJH
# @File : mergeIntervals.py
# @Software: PyCharm


class Solution:
    def merge(self, intervals):
        intervals.sort(key = lambda ele: ele[0])
        result = []
        queue = []

        for i in intervals:
            print(i)
            print(queue, '\n')
            if not queue:
                queue = i

            if i[0] > queue[1]:
                result.append(queue)
                queue = i
            else:
                queue[1] = max(queue[1],i[1])

        result.append(queue)
        return result

    def merge2(self, intervals):
        aa = sum(intervals,[])
        max_value = max(aa)
        min_value = min(aa)



if __name__ == '__main__':
    so = Solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18], [0,9]]

    print(so.merge(intervals))