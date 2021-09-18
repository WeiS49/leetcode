#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 相当于层序遍历只添加最后一个值
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        queue = [root]
        res = []
        while queue:
            current = []
            # node = queue.pop(0)
            for node in queue:
                current.append(node)
            res.append(current[-1].val)

            current = []
            for node in queue:
                if node.left:
                    current.append(node.left)
                if node.right:
                    current.append(node.right)

            queue = current

        return res




# @lc code=end

