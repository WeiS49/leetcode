#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树

# 迭代 - 从上到下
# 时间复杂度: 执行次数与节点个数有关, O(n)
# 空间复杂度: 占用空间与节点个数相关, O(n)

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if not root: # 特殊情况
            return 
        q = []
        q.append(root)
        while q:
            a = q.pop(0)

            a.left, a.right = a.right, a.left

            if a.left: # 如果节点存在, 就添加
                q.append(a.left)
            if a.right:
                q.append(a.right)

        return root

# @lc code=end

