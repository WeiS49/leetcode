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


# 1. 初始化 - 返回结果res, 当前结果stack: stack内元素为元组(节点, 当前路径), 同时保存当前路径, 规避了剪枝操作
# 2. 若果没有左右节点: 说明到达底部 - 记录当前路径
# 3. 对右节点和左节点进行操作(取巧的做法, 相当于不用写stack.pop(0), 执行速度会更快)
# 4. 返回所有路径res



# 参数及返回值: 根节点root; 遍历结果res
# 循环执行条件: 还有节点没有完全遍历
# 循环操作: 获取节点, 记录路径, 若没有左右节点, 说明到底, 添加至res

# 涉及到回溯的题目, 需要用额外变量来保持路径
# 或者说, 需不需要中间值取决于是否要记录中间状态

class Solution:

    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        if not root:
            return []

        res = []
        queue = [(root, "")]

        while queue:
            node, ls = queue.pop()

            if not node.left and not node.right:
                res.append(ls + str(node.val))
            
            ls = ls + str(node.val) + "->"

            if node.right:
                queue.append((node.right, ls))

            if node.left:
                queue.append((node.left, ls))

        return res

        # if not root:
        #     return []

        # res, stack = [], [(root, "")]
        # while stack:
        #     node, cur = stack.pop()

        #     if not node.left and not node.right:
        #         res.append(cur+str(node.val))
            
        #     if node.right:
        #         stack.append((node.right, cur + str(node.val) + "->"))
        #     if node.left:
        #         stack.append((node.left, cur + str(node.val) + "->"))

        # return res



















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

