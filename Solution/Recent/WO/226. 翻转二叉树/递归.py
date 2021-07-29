#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树

# 递归 - 从上到下和从下到上
# 时间复杂度: 执行次数与节点个数有关, O(n)
# 空间复杂度: 占用空间与树的高度相关, O(n)

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: # 终止条件
            return 

        # 写法1: 从上到下 - 先执行条件, 后递归函数
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        # 写法2: 从下到上 - 先递归函数, 后执行条件
        # left = self.invertTree(root.left) # 递归函数
        # right = self.invertTree(root.right)
        # root.left, root.right = right, left # 执行条件
        
        return root



# @lc code=end

