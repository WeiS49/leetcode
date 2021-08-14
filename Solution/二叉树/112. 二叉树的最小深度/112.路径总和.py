#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#
# 使用栈求解, 用到了深度优先遍历的思想
# 时间复杂度: 涉及到单层循环, 时间复杂度为O(n)
# 空间复杂度: 手动维护了一个栈stack, 这个栈保存了树中的所有节点, 所以占用空间与节点个数相关, 空间复杂度为O(n)

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        stack = []
        stack.append((root, root.val))
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right and path == targetSum:
                return True
            if node.left:
                stack.append((node.left, path + node.left.val))
            if node.right:
                stack.append((node.right, path + node.right.val))
        return False
        
# @lc code=end

