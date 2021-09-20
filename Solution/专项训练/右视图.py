#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS
# 参数及返回值: 根节点root; 右视图扁你结果res
# 循环执行逻辑: 还有节点层没有遍历完
# 循环操作逻辑: 循环获取当前层的节点, 将最后一个添加至res中

# Time: O(n) Space: O(n)
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        res = []
        queue = [root]

        while queue:
            # level = []
            n = len(queue)
            tmp = queue[n-1].val

            for _ in range(n):
                node = queue.pop(0)
                # level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # res.append(level[-1])
            res.append(tmp)

        return res
        



































        # if not root:
        #     return []

        # queue = [root]
        # res = []
        # while queue:
        #     current = []
        #     # node = queue.pop(0)
        #     for node in queue:
        #         current.append(node)
        #     res.append(current[-1].val)

        #     current = []
        #     for node in queue:
        #         if node.left:
        #             current.append(node.left)
        #         if node.right:
        #             current.append(node.right)

        #     queue = current

        # return res




# @lc code=end

