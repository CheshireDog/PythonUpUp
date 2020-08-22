#  coding = utf-8 

# @Time : 2020/8/16 19:42
# @Author : HJH
# @File : AverageSalary.py
# @Software: PyCharm


class Solution:
    def average(self, salary) -> float:
        min = salary[0]
        max = salary[0]
        sum = 0
        for i in salary:
            sum += i
            if min > i:
                min = i
                continue
            if max < i:
                max = i
                continue
        return (sum-min-max)/(len(salary)-2)


if __name__ == '__main__':
    so = Solution()
    salary = [6000, 5000, 4000, 3000, 2000, 1000]
    print(so.average(salary))