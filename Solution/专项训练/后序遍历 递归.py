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

# 1. 参数及返回值: 根节点root; 遍历结果self.res(list)
# 2. 终止条件: 当前节点为空 -> return None
# 3. 单层递归逻辑: 后序遍历 - 左 -> 右 -> 中
#   1. 执行条件: 将节点值添加进self.res
#   2. 递归进行条件: 将左右孩子继续递归

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.postorder(root)
        return self.res
    
    def postorder(self, root):
        if not root:
            return
        if root.left:
            self.postorder(root.left)
        if root.right:
            self.postorder(root.right)
        self.res.append(root.val)






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
