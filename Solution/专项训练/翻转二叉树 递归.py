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

# 参数及返回值: 根节点root; 返回后的结果root
# 递归终止条件: 当前节点不存在
# 单层递归逻辑: 遍历左右节点, 交换左右孩子

# 这道题不能用中序遍历, 要么是先遍历, 再交换; 或者先交换, 再遍历
# 如果是遍历 - 交换 - 遍历, 就有可能出现多交换一次的情况, 出现问题
# Time: O(n)  Space: O(n)

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.reverse(root)
        return root

    def reverse(self, root):

        if not root:
            return 
        if root.left:
            self.reverse(root.left)
        if root.right:
            self.reverse(root.right)
        root.left, root.right = root.right, root.left





















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

