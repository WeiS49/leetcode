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
from typing import AnyStr


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = list()  
        if not root:
            return paths


        paths = []
        if not root:
            return paths

        node_queue = [root]
        path_queue = [str(root.val)]

        while node_queue:
            node = node_queue.pop()
            path = path_queue.pop()

            if not node.left and not node.right:
                paths.append(path)

            else:
                if node.left:
                    node_queue.append(node.left)
                    path_queue.append(path + "->" + str(node.left.val))

                if node.right:
                    node_queue.append(node.right)
                    path_queue.append(path + "->" + str(node.right.val))

        return paths
        


# @lc code=end

