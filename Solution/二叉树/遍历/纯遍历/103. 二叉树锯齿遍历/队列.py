#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        res = []
        queue = [root]

        while queue:
            current = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if not node:
                    continue
                current.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if len(res) % 2 == 1:
                res.append(current[::-1])
            else:
                res.append(current)

        return res




# @lc code=end

