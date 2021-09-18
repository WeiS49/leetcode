#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 利用二叉搜索树的特性: root.left.val < root.val < root.right.val
# 因此中序遍历时结果按从小到大排序
# Space: O(n) n为二叉树中节点个数
# Time: O(1)
# 优化操作: 在check中添加判断: 当self.res非空时, return

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 设定一个计数器k用来保存当前搜索到的节点数
        self.k = k
        self.res = None
        self.check(root)
        return self.res

    def check(self, root):
        if self.res:
            return 

        if root:
            self.check(root.left)
            # 节点操作: k--
            self.k -= 1
            # k == 0, 说明当前节点为第k小的元素, 赋值
            if self.k == 0:
                self.res = root.val
            self.check(root.right)




# @lc code=end

