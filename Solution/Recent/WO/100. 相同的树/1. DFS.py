#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS: 判断非空树的节点是否相等
# 某一树先为空时, 直接返回结果, 不需要继续执行
# 时间复杂度: O(n), n为给定树的最小节点个数
# 空间复杂度: O(n), 同理

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        # 递归的终止条件(判断当前节点是否为空)
        if not p and not q:
            return True
        elif not p or not q:
            return False

        # 取反, 递归的执行条件(对比值是否相等)
        elif p.val != q.val:
            return False
        
        # 返回递归函数(使用and来判断左右节点是否一致)
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# @lc code=end

