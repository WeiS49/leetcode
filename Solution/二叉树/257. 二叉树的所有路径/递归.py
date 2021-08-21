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
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        
        def DFS(root):

            if not root:
                return
            path.append(str(root.val))

            if not root.left and not root.right:
                res.append("->".join(path))

            DFS(root.left)
            DFS(root.right)
            path.pop()


        path = []
        res = []
        DFS(root)
        return res
        


# @lc code=end

