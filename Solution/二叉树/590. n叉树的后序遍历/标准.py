#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N 叉树的后序遍历
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
    def postorder(self, root: 'Node') -> List[int]:

        output = []
        self.dfs(root, output)
        return output

    def dfs(self, root, output):
        if not root:
            return

        for child in root.children:
            self.dfs(child, output)
        output.append(root.val)


# @lc code=end

