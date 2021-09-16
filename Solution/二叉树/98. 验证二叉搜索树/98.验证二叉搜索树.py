#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 
# Time: O(n)  Space: O(1)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
    #     self.pre = None
    #     self.bool = True
    #     self.inorder(root)
    #     return self.bool
        
    # def inorder(self, root):
    #     if root and self.bool:
    #         self.inorder(root.left)
    #         if self.pre and root.val <= self.pre.val:
    #             self.bool = False
    #         self.pre = root
    #         self.inorder(root.right)



    # 添加一个bool用来控制结果很有用
        self.pre = -float("inf")
        self.bool = True
        self.inorder(root)
        return self.bool

    def inorder(self, root):
        if root and self.bool:
            self.inorder(root.left)
            if root.val <= self.pre:
                self.bool = False
            self.pre = root.val


            self.inorder(root.right)












    #     self.pre = None
    #     # self.pre = -float("inf")
    #     self.bool = True
    #     self.inorder(root)
    #     return self.bool
    #     # return True
    
    # def inorder(self, root):
    #     if root:
    #         self.inorder(root.left)
    #         if self.pre and root.val <= self.pre.val:
    #             # return False
    #             self.bool = False
    #         self.pre = root
    #         self.inorder(root.right)



# [5,1,4,null,null,3,6]













    #     self.res = []
    #     self.inorder(root)
    #     for i in range(1, len(self.res)):
    #         if self.res[i] <= self.res[i-1]:
    #             return False

    #     return True

    # def inorder(self, root):
    #     if root:
    #         self.inorder(root.left)
    #         self.res.append(root.val)
    #         self.inorder(root.right)

# @lc code=end

