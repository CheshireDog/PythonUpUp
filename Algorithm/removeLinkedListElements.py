#  coding = utf-8 

# @Time : 2021/8/17 9:28
# @Author : HJH
# @File : removeLinkedListElements.py
# @Software: PyCharm


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head ,val):
        while head and head.val == val:
            head = head.next
        pre, cur = head, head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next

        return head
