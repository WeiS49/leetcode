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
# 递归解法
# 时间复杂度: O(n) - 遍历整棵树, 线性复杂度
# 空间复杂度: O(n) - 递归层数最大为树的层数
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.check(root, root) # 

    def check(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False

        # 写法1 判断值相等和返回函数分开写
        if p.val != q.val:
            return False
        return self.check(p.left, q.right) and self.check(p.right, q.left)

        # 写法2 判断值相等的代码写在return中
        # return p.val == q.val and self.check(p.left, q.right) and self.check(p.right, q.left)


# @lc code=end

