#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []
        

        queue = [root]
        res = []
        

        while queue:
            res.append([node.val for node in queue])
            
            current = []
            
            for node in queue:
                if node.left:
                    current.append(node.left)
                if node.right:
                    current.append(node.right)
            
            queue = current

        return res






        # def level(root):
        #     while queue:
        #         # for i in range(len(queue)):
        #         #     q = queue.pop()
        #         #     current.append(q.val)
        #         for node in queue:
        #             current.append(node.val)
        #         res.append(current)
        #         current = []
        #         if root.left:
        #             queue.append(root.left)
        #         if root.right:
        #             queue.append(root.right)
            


# @lc code=end

