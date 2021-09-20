#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 参数及返回值: 根节点root; 遍历结果res(list) [[], []]
# 循环执行逻辑: 当还有节点层没有遍历完
# 循环操作逻辑: 循环获取当前层的节点, 将其添加到tmp中, 循环结束, 添加进res中

# Time: O(n) Space: O(n)

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        res = []
        queue = [root]

        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(tmp)
        
        return res[::-1]




























        # if not root:
        #     return [] 
        # res = []
        # queue = [root]
        # while queue:
        #     current = []
        #     for i in range(len(queue)):
        #         node = queue.pop(0)
        #         if not node:
        #             continue
        #         current.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     res.append(current)

        # return res[::-1]


# @lc code=end

