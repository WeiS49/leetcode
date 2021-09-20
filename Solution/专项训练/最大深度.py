#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度

# 类似题目还有543.二叉树的直径
# 套路写法, 适用于LC104
# Time: O(n) - n为节点个数
# Space: O(height) - height为树的高度

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 参数和返回值: 根节点root, 最大深度length(int)
# 递归终止条件: 当前节点为空
# 单层递归逻辑: 判断终止条件, 继续递归, 当前部分的层数+1

class Solution:
    def maxDepth(self, root: TreeNode) -> int: 
        self.length = 0
        return self.check(root)

    def check(self, root):
        if not root:
            return 0

        # 如果这么写, 相当于对同时对两边+1
        # 而题目要求的是分别处理
        # self.length += 1
        
        left = self.check(root.left)
        right = self.check(root.right)
        return max(left, right) + 1






        # def check(node):
        #     if not node:
        #         return 0
        #     left = check(node.left)
        #     right = check(node.right)
        #     if not left:
        #         return right + 1
        #     if not right:
        #         return left + 1
        #     return max(left, right) + 1
        # return check(root)

        # def check(root):
        #     if not root:
        #         return 0
        #     l = check(root.left)
        #     r = check(root.right)
        #     return max(l, r) + 1
        # return check(root)
        

        # def check(node):
        #     # 有限定条件, 所以遍历到底部, 结果为0
        #     # 递归都是从下到上的, 所以写的时候一定考虑这点
        #     if not node:
        #         return 0
        #     l = check(node.left)
        #     r = check(node.right)
        #     return max(l, r) + 1
        # return check(root)



# @lc code=end

# return 1 + max(map(self.maxDepth, (root.left, root.right)) if root else 0


        # if root == None:
        #     return 0
        # else:
        #     return max(map(self.maxDepth, (root.left, root.right))) + 1

        # return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0