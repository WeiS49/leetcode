#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (64.22%)
# Likes:    851
# Dislikes: 0
# Total Accepted:    296.2K
# Total Submissions: 461.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
#
#
#
# 示例：
# 二叉树：[3,9,20,null,null,15,7],


# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7


# 返回其层序遍历结果：


# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
#
#
#
# [102] 二叉树的层序遍历
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 参数及返回值: 根节点root; 遍历结果res
# 2. 循环进行条件: 还有节点层没有遍历完
# 3. 循环执行条件: 
#   1. 获取当前层的节点, 并添加到res中
#   2. 将当前层的节点的左右孩子添加进queue中

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        res = []
        queue = [root]

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(level)
        return res



# @lc code=end
