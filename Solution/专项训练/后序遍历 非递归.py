#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 非递归解法
# 1. 参数及返回值: 根节点root, 遍历结果res
# 2. 循环进行条件: 当节点没有遍历完
# 3. 循环执行操作: 
#   1. 获取节点
#   2. 判断节点是否存在
#   3. 后序遍历

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [(root, 0)]
        while stack:
            node, flag = stack.pop()
            if not node:
                continue
            if flag == 0:
                stack.append((node, 1))
                stack.append((node.right, 0))
                stack.append((node.left, 0))
            else:
                res.append(node.val)

        return res






        # res = []
        # stack = [(0, root)]

        # while stack:
        #     flag, node = stack.pop()
        #     if node is None:
        #         continue
        #     if flag == 1:
        #         res.append(node.val)
        #     else:
        #         stack.append((1, node))
        #         stack.append((0, node.right))
        #         stack.append((0, node.left))

        # return res

    #     res = []
    #     self.helper(root, res)
    #     return res

    # def helper(self, root, res):
    #     if root:
    #         self.helper(root.left, res)
    #         self.helper(root.right, res)
    #         res.append(root.val)


# @lc code=end
