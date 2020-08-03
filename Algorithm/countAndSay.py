# coding = utf-8

"""
Author:hjh
Date:08.03
Method:描述前一迭代字符串有几个几...
"""


class Solution:
    def countAndSay(self, n: int):
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        status = "11"
        for i in range(1, n-1):
            print("Circle :{}".format(i))
            count = 1
            cmp = status[0]
            say = ""
            for j in status[1:]:
                if j == cmp:
                    count += 1
                else:
                    say += str(count)
                    say += str(cmp)
                    count = 1
                cmp = j
            if count > 1:
                say += str(count)
                say += str(cmp)
            else:
                say += "1"
                say += str(cmp)
            print(say)
            status = say
        result = status
        return result


if __name__ == '__main__':
    so = Solution()
    n = 5
    print(so.countAndSay(n))







