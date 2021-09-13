#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N 叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:

    def preorder(self, root: 'Node') -> List[int]:
        res = []
        self.check(root, res)
        return res
        

    def check(self, root, res):
        if root:
            res.append(root.val)
            for child in root.children:
                self.check(child, res)

# @lc code=end

