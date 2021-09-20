#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# [110] 平衡二叉树

# 参数及返回值: 根节点root; 是否是平衡二叉树isBalanced(bool)
# 终止条件: 节点为空
# 单层递归逻辑: 判断高度差, 若>1, 则返回结果(只需要判断一次, 可以使用辅助变量)

# Time: O(n) Space: O(n)
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.bool = True
        self.check(root)
        return self.bool

    def check(self, root):
        if not root:
            return 0
        left = self.check(root.left)
        right = self.check(root.right)

        ans = abs(left - right)
        if ans > 1:
            self.bool = False
        # 每层递归要有返回值
        return max(left, right) + 1



























        # def depth(node):
        #     if not node:
        #         return 0
        #     # 获取左右节点
        #     left = depth(node.left)
        #     right = depth(node.right)
        #     ans = abs(left - right)
        #     if ans > 1:
        #         return -1
        #     # 只要找到之后, 就不需要再继续递归了
        #     # 可以和上面的if写在一起
        #     if left == -1 or right == -1:
        #         return -1
        #     return 1 + max(left, right) # 最大深度的标准写法

        # return depth(root) != -1
# @lc code=end

# [1,2,2,3,null,null,3,4,null,null,4]