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

# 1. 参数及返回值: 根节点root; 返回值res(list)
# 2. 循环进行条件: 当节点没有完全遍历完时
# 3. 循环操作: 获取节点及flag - 中序遍历
#   1. 判断 - 无节点时 continue
#   2.  flag == 0 -> 没有遍历过, 中序遍历的顺序将节点添加进stack中
#       flag = =1 -> 已经遍历, 将值添加进res

# def inorder(self, root):
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [(root, 0)]
        while stack:
            node, flag = stack.pop()
            if not node:
                continue
            if flag:
                res.append(node.val)
            else:
                stack.append((node.right, 0))
                stack.append((node, 1))
                stack.append((node.left, 0))

        return res





































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
