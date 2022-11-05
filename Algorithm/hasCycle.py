#  coding = utf-8 

# @Time : 2021/7/26 22:25
# @Author : HJH
# @File : hasCycle.py  判断链表有环
# @Software: PyCharm


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        sp, fp = head, head
        sign = 0  # 必须先false再true，不然链表长度为1时会报错
        while sp:
            fp = fp.next
            if sign == 1:
                sp = sp.next
                sign = 0
            else:
                sign = 1
            if sp == fp:
                return True
        return False

    def hasCycle2(self, head: ListNode) -> bool:
        sp, fp, si = head, head, False
        while fp:
            if si:
                sp = sp.next
                si = False
            else:
                si = True
            fp = fp.next
            if sp == fp:
                return True
        return False
