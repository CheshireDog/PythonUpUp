#  coding = utf-8 

# @Time : 2021/8/17 9:58
# @Author : HJH
# @File : reverseLinkedList.py
# @Software: PyCharm


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        if not (head or head.next):
            return head
        cur, new = head, None
        while cur:
            nnode = cur.next
            cur.next = new
            new = cur
            cur = nnode

        return new
