#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N 叉树的最大深度
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# 参数及返回值: 根节点root, 最小深度depth(int)
# 终止条件: 当前节点为空
# 单层逻辑: 判断终止条件; 所有节点递归查找, 返回最小值
# 应该考虑一侧没有的情况(链表)



# 参数及返回值: 根节点root; 最大深度depth
# 递归终止条件: 当前节点为空
# 单层递归逻辑: (后序遍历) 判断终止条件, 

# 在二叉树中, 直接让左右比较即可
# 但在n叉树中, 没办法直接让左右节点进行比较, 所以设定depth变量保存当前高度, 进行比较

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.depth = 0
        x = self.postOrder(root)
        return x

    def postOrder(self, root):
        if not root:
            return 0
        
        depth = 0

        for child in root.children:
            depth = max(depth, self.postOrder(child))

        return depth + 1







































    #     return self.check(root)
    # def check(self, root):
    #     if not root:
    #         return 0
    #     left = 0
    #     right = 0
    #     if not root.left:
    #         left = self.check(root.left)
    #     if not root.right:
    #         right = self.check(root.right)
    #     if left == 0:
    #         return right
    #     if right == 0:
    #         return left

    #     return min(left, right) + 1




    #     return self.check(root)

    # def check(self, root):
    #     if not root:
    #         return 0
    #     depth = 0
    #     for child in root.children:
    #         depth = max(depth, self.check(child))
    #     return depth + 1


# @lc code=end

