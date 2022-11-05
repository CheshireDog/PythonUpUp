#  coding = utf-8 

# @Time : 2021/7/27 20:08
# @Author : HJH
# @File : mergeTwoLists.py
# @Software: PyCharm


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = head = ListNode()
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    l3.next = l1
                    l3 = l3.next
                    l1 = l1.next
                else:
                    l3.next = l2
                    l3 = l3.next
                    l2 = l2.next
            elif l1:
                l3.next = l1
                l3 = l3.next
                l1 = l1.next
            else:
                l3.next = l2
                l3 = l3.next
                l2 = l2.next
        return head.next


    def mergeTwoLists2(self, l1, l2):
        ret = head = ListNode()

        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    ret.next = l1
                    ret = ret.next
                    l1 = l1.next
                else:
                    ret.next = l2
                    ret = ret.next
                    l2 = l2.next
            elif l1:
                ret.next = l1
                ret = ret.next
                l1 = l1.next
            elif l2:
                ret.next = l2
                ret = ret.next
                l2 = l2.next
        return head.next



if __name__ == '__main__':
    so = Solution()
