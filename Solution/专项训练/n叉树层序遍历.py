#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# BFS
# 参数及返回值: 根节点root, 遍历结果res(list)
# 循环进行条件: 当还有节点没有遍历完
# 循环操作: 获取当前节点, 将值添加到res中
    # 分别获取节点的孩子节点, 将其添加到queue中

# Time: O(n) 总共遍历n个节点
# Space: O(n)
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if not root:
            return []

        res = []
        queue =[root]

        while queue:
            level = []
            n = len(queue)
            for _ in range(n):
                node = queue.pop(0)
                level.append(node.val)

                for child in node.children:
                    queue.append(child)
            res.append(level)
            
        return res




























        # if not root:
        #     return []

        # queue = [root]
        # res = []

        # while queue:
        #     level = []
        #     n = len(queue)
        #     for _ in range(n):
        #         node = queue.pop(0)
        #         level.append(node.val)
        #         # if node.left:
        #         #     queue.append(node.left)
        #         # if node.right:
        #         #     queue.append(node.right)
        #         # for child in node.children:
        #         #     queue.append(child)
        #         queue.extend(node.children)
        #     res.append(level)

        # return res
        
# @lc code=end

