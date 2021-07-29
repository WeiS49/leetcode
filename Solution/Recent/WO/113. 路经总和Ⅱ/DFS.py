#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# DFS解法
# 时间复杂度: O(n), 运行时长与节点个数呈线性关系
# 空间复杂度: O(n), 占用空间取决于树中节点个数

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(root, targetSum):

            if not root:
                return 

            path.append(root.val) # 保存当前处理的节点值
            targetSum -= root.val # 对节点值进行处理

            if not root.left and not root.right and targetSum == 0:
                res.append(path) # 添加值为[]
                res.append(len(path)) # 添加值为列表原长度
                # 这里因为path值在动态变化, 所以要用到切片保存当前状态
                res.append(path[:]) # 添加值为列表本身的内容

            dfs(root.left, targetSum)
            dfs(root.right, targetSum)
            path.pop()
        dfs(root, targetSum)
        # return path
        return res
















































        # res = []
        # path = []

        # def dfs(node, total):

        #     if not node:
        #         return

        #     path.append(node.val) # 将当前处理的路径值保存下来
        #     total -= node.val # 对当前路径值进行处理

        #     if not node.left and not node.right and total == 0: # 判断是否符合条件
        #         res.append(path[:])
            
        #     dfs(node.left, total) # 对左节点如此处理
        #     dfs(node.right, total) 
        #     path.pop() # 剪枝操作
        
        # dfs(root, targetSum)
        # return res














        # ret = list()
        # path = list()
        
        # def dfs(node: TreeNode, targetSum: int):
        #     if not root:
        #         return
        #     path.append(root.val)
        #     targetSum -= root.val
        #     if not root.left and not root.right and targetSum == 0:
        #         ret.append(path[:])
        #     dfs(root.left, targetSum)
        #     dfs(root.right, targetSum)
        #     path.pop() # 遇到不符合要求的结果就进行剪枝 - 回退到上一状态
        
        # dfs(root, targetSum)
        # return ret


# @lc code=end

