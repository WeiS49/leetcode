#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.ans = -1
        self.rootval = root.val
        self.check(root)
        return self.ans
    def check(self, root):
        if not root:
            return 
        # 当self.ans已被赋值, 且当前root.val更大(一定不是第二小)
        if self.ans != -1 and root.val > self.ans:
            return
        if root.val > self.rootval:
            self.ans = root.val
        if root.left:
            self.check(root.left)
        if root.right:
            self.check(root.right)
    

# @lc code=end

