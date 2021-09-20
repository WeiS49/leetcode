#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 参数及返回值: 根节点root; 翻转后的root(再原节点反转)
# 循环进行条件: 有节点没遍历完
# 循环操作: 左右孩子交换, 添加左右孩子节点
# Time: O(n) Space: O(n)
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        queue = []
        if root:
            queue.append(root)
        while queue:
            node = queue.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root




















        # if not root:
        #     return
        # queue = [root]
        # while queue:
        #     node = queue.pop(0)
        #     node.left, node.right = node.right, node.left
        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)
        
        # return root

        # if not root:
        #     return
        # queue = [root]
        # while queue:
        #     node = queue.pop(0)
        #     node.left, node.right = node.right, node.left
        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)
        # return root



# @lc code=end

