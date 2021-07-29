#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#
# 深度优先遍历, 类似栈, 递归
# 时间复杂度: 最坏情况需要遍历树中所有节点, O(n)
# 空间复杂度: 最坏情况需要储存n个节点, O(n)

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return # 添加进None的情况
        if root == p or root == q: return root # 只有找到了, 才返回root
        left = self.lowestCommonAncestor(root.left, p, q) # 将左节点添加进递归池, 即使为None
        right = self.lowestCommonAncestor(root.right, p, q) # 将右节点添加进递归池
        if not right and not left: return # 左右节点都没有的情况
        if not left: return right # 只找到右节点的情况
        if not right: return left # 只找到左节点的情况
        return root # 只有左右都找到, 才会执行























        # if not root: return # 如果节点为空 返回Null
        # if root == q or root == p: return root # 如果找到左右节点, 则返回节点值
        # left = self.lowestCommonAncestor(root.left, p, q) # 只有找到了才会被赋值, 否则就返回Null
        # right = self.lowestCommonAncestor(root.right, p, q)
        # if not left and not right: return # 找不到左右节点, 返回空
        # if not left: return right # 无左节点, 返回右节点
        # if not right: return left # 无右节点, 返回左节点
        # return root # 两侧均有节点, 
# @lc code=end

