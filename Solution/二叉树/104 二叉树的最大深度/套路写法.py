#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度

# 类似题目还有543.二叉树的直径
# 标准写法, 不炫技
# Time: O(n) - n为节点个数
# Space: O(height) - height为树的高度

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def check(node):
            if not node:
                return 0
            left = check(node.left)
            right = check(node.right)
            if not left:
                return right + 1
            if not right:
                return left + 1
            return max(left, right) + 1
        return check(root)
        
# @lc code=end

# return 1 + max(map(self.maxDepth, (root.left, root.right)) if root else 0


        # if root == None:
        #     return 0
        # else:
        #     return max(map(self.maxDepth, (root.left, root.right))) + 1

        # return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0