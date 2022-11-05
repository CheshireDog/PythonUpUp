#  coding = utf-8 

# @Time : 2021/9/25 19:08
# @Author : HJH
# @File : orderTraversal.py
# @Software: PyCharm


# 二叉树遍历
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode):
        