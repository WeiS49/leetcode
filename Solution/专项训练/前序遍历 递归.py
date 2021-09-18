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

# 给定的参数及返回值: 参数 - 根节点root, 用以遍历整棵树; 返回值(list): 遍历的结果
# 递归的终止条件: 当前节点为空时, 返回None
# 递归的逻辑: 前序遍历 - 中 -> 左 -> 右, 对于中间节点root, 添加至res, 另外两侧继续遍历
#           因为在一层中, 只有root的值确定, 左右孩子需要通过root去递归查找. 

# Time: O(n) 需要遍历所有节点
# Space: O(n) res即为返回值, 不计入空间复杂度
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = [] # 保存返回的结果
        self.preorder(root)
        return self.res

    def preorder(self, root):
        if not root:
            return 
        self.res.append(root.val)
        if root.left:
            self.preorder(root.left)
        if root.right:
            self.preorder(root.right)





























        
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
