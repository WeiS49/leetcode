#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
# 参数及返回值: 根节点root; 遍历计算结果res
# 终止条件: 还有节点没遍历完
# 单层递归逻辑: 循环获取该层所有节点, 求和后求平均值, 将结果添加至res

# Time: O(n) Space: O(n)

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        res = []
        queue = [root]

        while queue:

            n = len(queue)
            total = 0
            for _ in range(n):
                node = queue.pop(0)
                total += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


            res.append(total / n)

        return res




# @lc code=end

