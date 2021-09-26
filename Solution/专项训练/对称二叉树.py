#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 参数及返回值: 根节点root; 是否镜像对称(bool)
# 递归终止条件: 节点没有; 发现不对称
# 单层逻辑: 判断是否对称, 若对称, 添加左右节点

# Time: O(n)  Space: O(n)

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # self.bool = True
        return self.check(root.left, root.right)
        # return self.bool

    def check(self, left, right):


        if not left and not right: return True
        elif not left or not right: return False
        elif left and right: 
            if left.val != right.val: return False
            
            inside = self.check(left.left, right.right)
            outside = self.check(left.right, right.left)
            return inside and outside

        # return self.check(left.left, right.right) and self.check(left.right, right.left)


















    #     self.bool = True
    #     self.check(root)
    #     return self.bool
    # def check(self, root):
    #     if not root:
    #         return 
    #     if root.left != root.right:
    #         self.bool = False
    #     left = self.check(root.left)
    #     right = self.check(root.right)
        
        
        





# @lc code=end

