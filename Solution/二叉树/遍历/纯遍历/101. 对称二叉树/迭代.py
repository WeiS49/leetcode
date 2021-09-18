#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        q = []
        q.append(root)
        q.append(root)

        while q:
            a = q[0]
            b = q[1]
            q = q[2:]

            if not a and not b:
                continue
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            
            q.append(a.left)
            q.append(b.right)
            
            q.append(a.right)
            q.append(b.left)

        return True


# @lc code=end

