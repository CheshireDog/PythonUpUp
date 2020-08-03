#  coding = utf-8 
# @Time : 2020/8/2 10:13
# @Author : HJH
# @File : BinarySum.py
# @Software: PyCharm


class Solution:
    def addBinary(self, a: str, b: str):
        if len(a) > len(b):
            str_l = len(a)
            str_s = len(b)
            long_str = a[::-1]
            short_str = b[::-1]
        else:
            str_l = len(b)
            str_s = len(a)
            long_str = b[::-1]
            short_str = a[::-1]
        result = ''
        carry = 0
        for i in range(str_s):
            s = int(long_str[i]) + int(short_str[i]) + carry
            if s > 1:
                carry = 1
                result += str(s-2)
            else:
                carry = 0
                result += str(s)
        print(result)
        for j in range(str_s, str_l):
            s = int(long_str[j]) + carry
            if s > 1:
                carry = 1
                result += str(s-2)
            else:
                carry = 0
                result += str(s)
        if carry == 1:
            result += '1'
        return result[::-1]


if __name__ == '__main__':
    a = "1011111"
    b = "1011"
    so = Solution()

    print(so.addBinary(a, b))

