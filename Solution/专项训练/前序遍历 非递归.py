#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 非递归写法
# 用一个额外的flag来判断当前是否进行过遍历
# 
# 1. 参数与返回值: 根节点root; 遍历结果(list)
# 2. 循环条件: 当前树中还有节点
# 3. 单层循环逻辑: 
#   1. 从栈中取出flag及节点
#   2. 判断节点是否存在
#   3. 根据节点是否遍历过执行操作: 遍历过 - 添加至res中; 没遍历过 - 将节点及其左右孩子入栈(注意遍历顺序)

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        res = []
        stack = [(root, 0)]

        while stack:
            node, flag = stack.pop()
            if not node:
                continue
            if flag == 1:
                res.append(node.val)
            else:
                stack.append((node.right, 0))
                stack.append((node.left, 0))
                stack.append((node, 1))

        return res

































        
        # res = []
        # stack = [(0, root)]
        # while stack:
        #     flag, node = stack.pop()
        #     if node is None: continue
        #     if flag == 1:
        #         res.append(node.val)
        #     else:
                
        #         stack.append((0, node.right))
        #         stack.append((0, node.left))
        #         stack.append((1, node))

        # return res













        # checked, not_checked = 1, 0
        # res = []
        # stack = [(not_checked, root)]

        # while root:

        #     i, node = stack.pop()
        #     if node is None:
        #         continue
        #     if i == checked:
        #         res.append(node.val)
        #     else:
        #         stack.append((not_checked, node.right))
        #         stack.append((checked, node))
        #         stack.append((not_checked, node.left))
        # return res

    #     res = []
    #     self.helper(root, res)
    #     return res

    # def helper(self, root, res):
    #     if root:
    #         res.append(root.val)
    #         self.helper(root.left, res)
    #         self.helper(root.right, res)


# @lc code=end
