#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 使用递归很难直接判断左右节点是否到底, 
# 递归更适合直接对二叉树底部直接进行操作 - LC114, 不适合保存中间值
# 虽然也可以通过实现初始化self.tmp来进行保存, 但那只是O(1)的变量, 对于复杂的情况相对不适合
# 虽然也能写, 但会非常复杂
# 对于这种情况, 还是使用相对可控的迭代方法
# 1. 初始化 - 返回结果res, 当前结果stack: stack内元素为元组(节点, 当前路径), 同时保存当前路径, 规避了剪枝操作
# 2. 若果没有左右节点: 说明到达底部 - 记录当前路径
# 3. 对右节点和左节点进行操作(取巧的做法, 相当于不用写stack.pop(0), 执行速度会更快)
# 4. 返回所有路径res
class Solution:

    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        if not root:
            return []

        res, stack = [], [(root, "")]
        while stack:
            node, cur = stack.pop()

            if not node.left and not node.right:
                res.append(cur+str(node.val))
            
            if node.right:
                stack.append((node.right, cur + str(node.val) + "->"))
            if node.left:
                stack.append((node.left, cur + str(node.val) + "->"))

        return res










    #     # self.res = 0
    #     self.res = []
    #     # queue = [root]

    #     # while queue:
    #     #     level = []
    #     #     node = queue.pop()

    #     def check(root):
    #         level = []
    #         if not root:
    #             return 
    #         if root:
    #             self.res.append(root.val)
    #             if root.left:
    #                 check(root.left)
    #             if root.right:
    #                 check(root.right)
            
    #     check(root)
    #     return self.res


# @lc code=end

