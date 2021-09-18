#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
# 查找最小深度, 需要考虑特殊的二叉树 - 链表
# 因此, 需要遍历整个二叉树, 不能像104题一样省略有子节点的情况
# Time: O(n), 遍历所有节点, n为节点个数
# Space: 平均情况: O(logn) - 二叉树, 最坏情况: O(n) - 链表

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

        if not root.left and not root.right:
            return 1

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if not root.left or not root.right:
            return left + right + 1
        
        return min(left, right) + 1



















        # if not root:
        #     return 0
        
        # if not root.left and not root.right:
        #     return 1

        # # left = self.minDepth(root.left)
        # # right = self.minDepth(root.right)

        # # 此时另一侧为0
        # if not root.left or not root.right: 
        #     return self.minDepth(root.left) + self.minDepth(root.right) + 1

        # return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

        # # length = min(left, right)
        # # return length + 1

        # # return min(self.minDepth(root.left), self.minDepth(root.right)) + 1




# @lc code=end

