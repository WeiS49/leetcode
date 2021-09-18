#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if not root:
            return []

        queue = [root]
        res = []

        while queue:
            level = []
            n = len(queue)
            for _ in range(n):
                node = queue.pop(0)
                level.append(node.val)
                # if node.left:
                #     queue.append(node.left)
                # if node.right:
                #     queue.append(node.right)
                # for child in node.children:
                #     queue.append(child)
                queue.extend(node.children)
            res.append(level)

        return res
        
# @lc code=end

