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
        self.ans = 0
        def depth(node):
            if not node:
                return 0
            l = depth(node.left)
            r = depth(node.right)
            self.ans = max(l, r) + 1
            return max(l, r) + 1
        depth(root)
        return self.ans

        
# @lc code=end

# return 1 + max(map(self.maxDepth, (root.left, root.right)) if root else 0


        # if root == None:
        #     return 0
        # else:
        #     return max(map(self.maxDepth, (root.left, root.right))) + 1

        # return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0