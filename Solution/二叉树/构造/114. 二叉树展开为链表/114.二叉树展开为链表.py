#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None # 用来保存遍历过的头节点

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return None

        self.flatten(root.right)
        self.flatten(root.left)

        root.left = None
        root.right = self.prev
        self.prev = root













        # if not root:
        #     return None

        # if root.right:
        #     self.flatten(root.right)
        # if root.left:
        #     self.flatten(root.left)

        # root.left = None
        # root.right = self.prev
        
        # self.prev = root

# @lc code=end

