#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        def check(node):
            if not node:
                return 0
            left = check(node.left)
            right = check(node.right)
            # 通过添加条件判断, 舍弃掉没有节点的分支
            # 否则遇到特殊二叉树 - 链表时会出错
            # 因为链表只有一条分支, 另一条为0, 总是更小, 导致错误
            # 除非根据"没有node" "没有node左右"分别进行判断
            if not left:
                return right + 1
            if not right:
                return left + 1
            return min(left, right) + 1
        return check(root)

# @lc code=end

