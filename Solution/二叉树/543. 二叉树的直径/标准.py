#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
# 思路和LC104.最大深度类似
# 只是增加了保存当前最大值的中间变量及比较最大值的代码
# Time: O(n) - 节点个数; Space: O(height) - 二叉树高度
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.ans = max(self.ans, left + right + 1)
            return max(left, right) + 1
        depth(root)
        return self.ans - 1



        # self.ans = 0
        # def depth(node):
        #     if not node:
        #         return 0 
        #     l = depth(node.left)
        #     r = depth(node.right)
        #     self.ans = max(self.ans, l + r + 1)
        #     return max(l, r) + 1
        
        # depth(root)
        # return self.ans - 1


# @lc code=end

