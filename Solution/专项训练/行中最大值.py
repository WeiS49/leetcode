#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 参数及返回值: 根节点root: 每一层的最大值res(list) []
# 循环执行条件: 还有节点层没有遍历完 
# 循环操作: 获取该层节点, 对比最大值, 添加进res中; 添加左右节点至queue

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        res = []
        queue = [root]

        while queue:
            cur = -float("inf")
            n = len(queue)
            for _ in range(n):
                node = queue.pop(0)
                cur = max(cur, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(cur)

        return res








# @lc code=end

