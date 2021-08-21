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

        res = [root]
        answer = []
        path = []
        while res:

            current = res.pop()
            if not current:
                continue
            path.append(str(current.val))
            if not current.left and not current.right:
                answer.append("->".join(path))
            else:
                if current.left:
                    res.append(current.left)
                if current.right:
                    res.append(current.right)
            path.pop()
            
            
        return answer


# @lc code=end

