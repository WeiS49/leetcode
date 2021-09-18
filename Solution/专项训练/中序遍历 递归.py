#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归解法:
# 1. 参数及返回值: 根节点root, 遍历结果self.res
# 2. 终止条件: 当前遍历节点为空
# 3. 单层递归逻辑: 中序遍历 - 左 -> 中 -> 右
#   执行条件: 添加root.val至self.res
#   递归进行条件: 将左右孩子继续递归
# def inorder(self, root):
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.inorder(root)
        return self.res
    
    def inorder(self, root):
        if not root:
            return 
        if root.left:
            self.inorder(root.left)
        self.res.append(root.val)
        if root.right:
            self.inorder(root.right)



































        # if not root:
        #     return[]

        # res = []
        # stack = [(0, root)]

        # while stack:

        #     flag, node = stack.pop(0)
        #     if node is None:
        #         continue
        #     if flag == 0:
        #         stack.append((0, node.right))
        #         stack.append((1, node))
        #         stack.append((0, node.left))
        #     else:
        #         res.append(node.val)

        # return res

# 关键问题 不要向栈中添加节点值

        # res, stack = [], []
        # while True:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     if not stack:
        #         return res
        #     node = stack.pop()
        #     res.append(node.val)
        #     root = node.right

    #     res = []
    #     self.helper(root, res)
    #     return res

    # def helper(self, root, res):
    #     if root:
    #         self.helper(root.left, res)
    #         res.append(root.val)
    #         self.helper(root.right, res)




# @lc code=end
