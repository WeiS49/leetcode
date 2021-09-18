#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 保存中间值, 与targetSum进行比较
# Time: O(n) Space: O(n)
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:

        self.count = 0

        def dfs(root, sumlist):

            if not root:
                return 

            sumlist = [sumx + root.val for sumx in sumlist]
            sumlist.append(root.val)

            for num in sumlist:
                if num == targetSum:
                    self.count += 1

            dfs(root.left, sumlist)
            dfs(root.right, sumlist)

        dfs(root, [])

        return self.count


# @lc code=end

