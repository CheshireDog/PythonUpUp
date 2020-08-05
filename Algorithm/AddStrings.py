#  coding = utf-8 

# @Time : 2020/8/5 21:22
# @Author : HJH
# @File : AddStrings.py
# @Software: PyCharm


class Solution:
    def addStrings(self, num1: str, num2: str):
        # 字符串数字相加，不使用Int
        # 最后一位开始遍历，短串遍历完去默认值‘0’，利用ASCII码
        i = len(num1)-1
        j = len(num2)-1
        res = ""
        carry = 0
        while i >= 0 or j >= 0:
            n1 = num1[i] if i >= 0 else '0'
            n2 = num2[j] if j >= 0 else '0'
            temp = ord(n1) + ord(n2) - 2*ord('0') + carry
            cur = temp % 10
            carry = temp//10
            res = chr(cur+48) + res
            i -= 1
            j -= 1
        return '1' + res if carry != 0 else res